from translation.level_2.TP_atom.original_TP_atom.eventually.simplest.simplest_eventually_atom_handler \
    import SimplestEventuallyAtomHandler
from translation.level_2.TP_atom.original_TP_atom.always.simplest.simplest_always_atom_handler \
    import SimplestAlwaysAtomHandler
from translation.level_2.TP_atom.original_TP_atom.once.simplest.simplest_once_atom_handler \
    import SimplestOnceAtomHandler
from translation.level_2.TP_atom.original_TP_atom.historically.simplest.simplest_historically_atom_handler \
    import SimplestHistoricallyAtomHandler
from translation.level_2.TP_atom.original_TP_atom.until.simplest.simplest_until_atom_handler \
    import SimplestUntilAtomHandler
from translation.level_2.TP_atom.original_TP_atom.since.simplest.simplest_since_atom_handler \
    import SimplestSinceAtomHandler
from translation.level_2.TP_atom.fall_TP_atom.public_class.fall_tp_atom_process.type1.\
    fall_tp_atom_type1_refiner_assembler import FallTPAtomType1RefinerAssembler
import copy


class NotFallTPAtomType1RefinerAssembler(FallTPAtomType1RefinerAssembler):

    def main_sentence_refine(self):
        subject_refined = copy.deepcopy(self.template['subject'])

        # get the simplest translation version of the temporal operator
        simplest_material = self.translate_guide['original_tp_instruction']
        limit_num = self.translate_guide['tp_operator_limit_num']
        tp_operator_type = self.translate_guide['tp_operator_type']
        if tp_operator_type == 'eventually':
            simplest_eventually_atom_handler \
                = SimplestEventuallyAtomHandler(simplest_material, limit_num)
            appositive_refined = \
                simplest_eventually_atom_handler.simplest_eventually_atom_translator.random_selected_translations
        elif tp_operator_type == 'always':
            simplest_always_atom_handler = \
                SimplestAlwaysAtomHandler(simplest_material, limit_num)
            appositive_refined = \
                simplest_always_atom_handler.simplest_always_atom_translator.random_selected_translations
        elif tp_operator_type == 'once':
            simplest_once_atom_handler = \
                SimplestOnceAtomHandler(simplest_material, limit_num)
            appositive_refined = \
                simplest_once_atom_handler.simplest_once_atom_translator.random_selected_translations
        elif tp_operator_type == 'historically':
            simplest_historically_atom_handler = \
                SimplestHistoricallyAtomHandler(simplest_material, limit_num)
            appositive_refined = \
                simplest_historically_atom_handler.simplest_historically_atom_translator.random_selected_translations
        elif tp_operator_type == 'until':
            simplest_until_atom_handler = \
                SimplestUntilAtomHandler(simplest_material, limit_num)
            appositive_refined = \
                simplest_until_atom_handler.simplest_until_atom_translator.random_selected_translations
        else:  # tp_operator_type == 'since':
            simplest_since_atom_handler = \
                SimplestSinceAtomHandler(simplest_material, limit_num)
            appositive_refined = \
                simplest_since_atom_handler.simplest_since_atom_translator.random_selected_translations

        template_key, mood = 'predicate', 'negative'
        predicate_refined = self.predicate_refine(template_key, mood)

        object_refined = copy.deepcopy(self.template['object'])

        refined_template_dict = {'mood': mood,
                                 'subject_refined': subject_refined,
                                 'appositive_refined': appositive_refined,
                                 'predicate_refined': predicate_refined,
                                 'object_refined': object_refined
                                 }
        self.assemble_guide.append(refined_template_dict)

        return self.assemble_guide

    def adverbial_augment(self, main_para):
        eng_list_adverbialAdded = []

        for word in self.adverbial_para:
            eng_main = self.random_select_assemble(main_para)
            eng_update = word + ' ' + eng_main
            eng_list_adverbialAdded.append(eng_update)

            # # the mood of the sentence is negative,
            # # so do not put adverbs or adverbial phrases to the end of the sentence
            # eng_main = self.random_select_assemble(main_para)
            # eng_update = eng_main + ' ' + word
            # eng_list_adverbialAdded.append(eng_update)

        return eng_list_adverbialAdded

