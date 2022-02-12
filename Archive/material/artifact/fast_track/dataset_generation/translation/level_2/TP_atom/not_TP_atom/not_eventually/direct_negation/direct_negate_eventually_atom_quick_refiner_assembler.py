from translation.level_2.TP_atom.original_TP_atom.eventually.normal.eventually_atom_quick_refiner_assembler \
    import EventuallyAtomQuickRefinerAssembler
import copy


class DirectNegateEventuallyAtomQuickRefinerAssembler(EventuallyAtomQuickRefinerAssembler):

    def clause_refine(self):
        subject_refined = copy.deepcopy(self.template['subject'])
        # the mood should be set as 'negative'
        template_key, mood = 'predicate', 'negative'
        predicate_refined = self.predicate_refine(template_key, mood)
        object_refined = copy.deepcopy(self.template['object'])
        conjunction_refined = copy.deepcopy(self.template['conjunction'])
        refined_template_dict = {'mood': mood,
                                 'subject_refined': subject_refined,
                                 'predicate_refined': predicate_refined,
                                 'object_refined': object_refined,
                                 'conjunction_refined': conjunction_refined
                                 }
        self.assemble_guide.append(refined_template_dict)

        return self.assemble_guide

    def assemble_process(self, refined_template_dict):
        subject_refined = refined_template_dict['subject_refined']
        predicate_refined = refined_template_dict['predicate_refined']
        object_refined = refined_template_dict['object_refined']
        conjunction_refined = refined_template_dict['conjunction_refined']

        for i in range(len(predicate_refined)):
            for predicate in predicate_refined[i]:
                clause_para = [subject_refined, predicate, object_refined]
                eng_main = self.random_select(clause_para)
                eng = eng_main + conjunction_refined
                self.eng_list.append(eng)
