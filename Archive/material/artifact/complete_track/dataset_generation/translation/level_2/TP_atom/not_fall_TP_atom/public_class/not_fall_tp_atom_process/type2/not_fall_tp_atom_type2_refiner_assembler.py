from translation.level_2.TP_atom.original_TP_atom.eventually.normal.eventually_atom_hook import EventuallyAtomHook
from translation.level_2.TP_atom.original_TP_atom.always.normal.always_atom_hook import AlwaysAtomHook
from translation.level_2.TP_atom.original_TP_atom.once.normal.once_atom_hook import OnceAtomHook
from translation.level_2.TP_atom.original_TP_atom.historically.normal.historically_atom_hook import HistoricallyAtomHook
from translation.level_2.TP_atom.original_TP_atom.until.normal.until_atom_hook import UntilAtomHook
from translation.level_2.TP_atom.original_TP_atom.since.normal.since_atom_hook import SinceAtomHook
from translation.level_2.TP_atom.fall_TP_atom.public_class.fall_tp_atom_process.type2.\
    fall_tp_atom_type2_refiner_assembler import FallTPAtomType2RefinerAssembler
import copy


class NotFallTPAtomType2RefinerAssembler(FallTPAtomType2RefinerAssembler):

    def main_sentence_refine(self):
        subject_refined = copy.deepcopy(self.template['subject'])
        template_key, mood = 'predicate', 'negative'
        predicate_refined = self.predicate_refine(template_key, mood)
        object_refined = copy.deepcopy(self.template['object'])

        # get the normal translation version of the temporal operator
        normal_material = self.translate_guide['original_tp_instruction']
        limit_num = self.translate_guide['tp_operator_limit_num']
        tp_operator_type = self.translate_guide['tp_operator_type']
        if tp_operator_type == 'eventually':
            eventually_atom_hook = EventuallyAtomHook(normal_material, limit_num)
            appendix_refined = eventually_atom_hook.eventually_atom_translator.random_selected_translations
        elif tp_operator_type == 'always':
            always_atom_hook = AlwaysAtomHook(normal_material, limit_num)
            appendix_refined = always_atom_hook.always_atom_translator.random_selected_translations
        elif tp_operator_type == 'once':
            once_atom_hook = OnceAtomHook(normal_material, limit_num)
            appendix_refined = once_atom_hook.once_atom_translator.random_selected_translations
        elif tp_operator_type == 'historically':
            historically_atom_hook = HistoricallyAtomHook(normal_material, limit_num)
            appendix_refined = historically_atom_hook.historically_atom_translator.random_selected_translations
        elif tp_operator_type == 'until':
            until_atom_hook = UntilAtomHook(normal_material, limit_num)
            appendix_refined = until_atom_hook.until_atom_translator.random_selected_translations
        else:  # tp_operator_type == 'since':
            since_atom_hook = SinceAtomHook(normal_material, limit_num)
            appendix_refined = since_atom_hook.since_atom_translator.random_selected_translations

        refined_template_dict = {'mood': mood,
                                 'subject_refined': subject_refined,
                                 'predicate_refined': predicate_refined,
                                 'object_refined': object_refined,
                                 'appendix_refined': appendix_refined
                                 }
        self.assemble_guide.append(refined_template_dict)

        return self.assemble_guide

    def adverbial_augment(self, main_para, appendix):
        eng_list_adverbialAdded = []

        for word in self.adverbial_para:
            eng_main = self.random_select_assemble(main_para)
            eng_update = word + ' ' + eng_main + ': ' + appendix
            eng_list_adverbialAdded.append(eng_update)

            # # the mood of the sentence is negative,
            # # so do not put adverbs or adverbial phrases to the end of the sentence
            # eng_main = self.random_select_assemble(main_para)
            # eng_update = eng_main + ' ' + word + ': ' + appendix
            # eng_list_adverbialAdded.append(eng_update)

        return eng_list_adverbialAdded
