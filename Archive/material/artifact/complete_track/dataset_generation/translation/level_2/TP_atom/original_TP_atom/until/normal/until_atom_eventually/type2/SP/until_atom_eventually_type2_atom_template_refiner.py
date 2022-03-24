from translation.level_1.atom.atom_template_refiner import AtomTemplateRefiner


class UntilAtomEventuallyType2AtomTemplateRefiner(AtomTemplateRefiner):

    def se_not_event_refine(self, category, sub_category):
        # 1. subject_refined is the real subject
        # process the template of subject
        subject_refined = self.sub_obj_extractor.se_sub_process()

        # process the template of predicate
        template_key, mood = 'predicate_action', 'negative'
        predicate_refined = self.predicate_refine(template_key, mood)

        # process the template of object
        object_refined = self.sub_obj_extractor.se_obj_process(category, sub_category, mood)

        # combine all English templates plus clause type and mood
        # the value of key 'clause_type' means there are no prefix or suffix in the translation
        refined_template_dict = {'clause_type': 'NoPrefixNoSuffix',
                                 'mood': mood,
                                 'subject_refined': subject_refined,
                                 'predicate_refined': predicate_refined,
                                 'object_refined': object_refined
                                 }
        self.assemble_guide.append(refined_template_dict)

        # 2. do not consider the scenario that prefix is the real subject

    def ere_refine(self, category):
        # replace the template of subject and object with actual words, numbers, etc.
        [subject_refined, object_refined] = self.sub_obj_extractor.ere_sub_obj_process(category)

        # 1. subject_refined is the real subject
        template_key, mood = 'predicate_action', 'positive'
        predicate_refined = self.predicate_refine(template_key, mood)

        # combine all English templates plus clause type and mood
        # the value of key 'clause_type' means there are no prefix or suffix in the translation
        refined_template_dict = {'clause_type': 'NoPrefixNoSuffix',
                                 'mood': mood,
                                 'subject_refined': subject_refined,
                                 'predicate_refined': predicate_refined,
                                 'object_refined': object_refined
                                 }
        self.assemble_guide.append(refined_template_dict)

        # 2. do not consider the scenario that prefix is the real subject
