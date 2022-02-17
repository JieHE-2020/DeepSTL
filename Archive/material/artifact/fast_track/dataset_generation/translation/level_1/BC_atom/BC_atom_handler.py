from commands.command_pureSP import PreCmdPureSP
from corpus import adverbial_modifiers
from selection.level_1.BC_atom.BC_atom_selector import BCAtomSelector
from translation.level_1.BC_atom.BC_atom_translator import BCAtomTranslator
from public import parameters
import copy


class BCAtomHandler:

    def __init__(self, position, atom_type='random', limit_num=1000):
        self.position = position
        # only two options for atom_type: 'random', 'SE'
        self.atom_type = atom_type
        # the number of randomly selected translations
        self.limit_num = limit_num

        # prepare materials for translation
        self.instruction_dict = self.instruction_assemble()
        self.bc_atom_info_dict = self.bc_atom_select()
        self.adverbial_dict = self.adverbial_prepare()
        self.predicate_cmd_dict = self.command_process()

        self.bc_atom_translator = self.translate_process()

    def instruction_assemble(self):
        instruction_dict = {}
        if self.position == 'before_imply':
            instruction_dict['position'] = self.position
            instruction_dict['adverbial_query'] = 'adverbialDisabled'
        else:  # self.position == 'after_imply'
            instruction_dict['position'] = self.position
            instruction_dict['adverbial_query'] = 'adverbialEnabled'

        return instruction_dict

    def bc_atom_select(self):

        bc_atom_selector = BCAtomSelector(self.atom_type)
        bc_atom_info_dict = bc_atom_selector.bc_atom_info_dict

        return bc_atom_info_dict

    @staticmethod
    def adverbial_prepare():
        adv_refine_dict = copy.deepcopy(adverbial_modifiers.adv_simultaneously)

        adv_list = adverbial_modifiers.adv_simultaneously['adverb']
        adv_phrase_list = adverbial_modifiers.adv_phrase_simultaneously['adverbial_phrase']
        adv_assemble_list = [adv_list, adv_phrase_list]

        adverbial_dict = {
            'refine_dict': adv_refine_dict,
            'assemble_list': adv_assemble_list
        }

        return adverbial_dict

    def command_process(self):
        adverb_dict = copy.deepcopy(self.adverbial_dict['refine_dict'])
        pre_cmd = PreCmdPureSP(adverb_dict)

        if self.position == 'before_imply':
            main_cmd_dict = copy.deepcopy(pre_cmd.cmd_dic_before_imply)
        else:  # self.position == 'after_imply'
            main_cmd_dict = copy.deepcopy(pre_cmd.cmd_dic_after_imply)
        appositive_cmd_dict = copy.deepcopy(pre_cmd.cmd_dic_appositive)

        predicate_cmd_dict = {
            'main': main_cmd_dict,
            'appositive': appositive_cmd_dict
        }

        return predicate_cmd_dict

    def translate_process(self):
        translate_guide = [self.instruction_dict, self.bc_atom_info_dict, self.adverbial_dict, self.predicate_cmd_dict]
        bc_atom_translator = BCAtomTranslator(translate_guide, self.limit_num)

        return bc_atom_translator


# for i in range(1):
#     # there are two options for position
#     # 1 - 'before imply'
#     # 2 - 'after imply'
#     position = 'after_imply'
#     # only two options for type_preference: 'random', 'SE'
#     atom_type = 'random'
#     limit_num = parameters.limit_num_bc_atom
#     bc_atom_handler = BCAtomHandler(position, atom_type, limit_num)
#     print(bc_atom_handler.bc_atom_info_dict)
    # print('\n')
    # # bc_atom_handler.bc_atom_translator.display_translation()
    # bc_atom_handler.bc_atom_translator.display_random_translation()
    # print(bc_atom_handler.bc_atom_info_dict['type'][1])
    # print(i)
