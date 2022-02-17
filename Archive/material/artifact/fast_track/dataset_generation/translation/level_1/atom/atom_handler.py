from commands.command_pureSP import PreCmdPureSP
from corpus import adverbial_modifiers
from selection.level_1.atom.atom_selector import AtomSelector
from translation.level_1.atom.atom_translator import AtomTranslator
from public import parameters
import random
import copy


class AtomHandler:

    def __init__(self, position, type_preference, limit_num):
        self.position = position
        self.type_preference = type_preference
        # the number of randomly selected translations
        self.limit_num = limit_num

        # prepare materials for translation
        self.instruction_dict = self.instruction_assemble()
        self.atom_info_dict = self.atom_select()
        self.adverbial_dict = self.adverbial_prepare()
        self.predicate_cmd_dict = self.command_process()

        self.atom_translator = self.translate_process()

    def instruction_assemble(self):
        instruction_dict = {}
        if self.position == 'before_imply':
            instruction_dict['position'] = self.position
            instruction_dict['adverbial_query'] = 'adverbialDisabled'
        else:  # self.position == 'after_imply'
            instruction_dict['position'] = self.position
            instruction_dict['adverbial_query'] = 'adverbialEnabled'

        return instruction_dict

    def atom_select(self):
        atom_type = ''

        if self.type_preference == 'default':
            select_cmd = random.randint(0, 1)
            if select_cmd == 0:
                atom_type = 'SE'
            else:
                atom_type = 'ERE'

        if self.type_preference == 'positional':
            if self.position == 'before_imply':
                select_cmd = random.randint(1, 10)
                if select_cmd <= 8:
                    atom_type = 'ERE'
                else:
                    atom_type = 'SE'
            else:
                select_cmd = random.randint(1, 10)
                if select_cmd <= 9:
                    atom_type = 'SE'
                else:
                    atom_type = 'ERE'

        if self.type_preference == 'SE' or self.type_preference == 'ERE':
            atom_type = self.type_preference

        atom_selector = AtomSelector(atom_type)
        atom_info_dict = atom_selector.info_dict

        return atom_info_dict

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
        translate_guide = [self.instruction_dict, self.atom_info_dict, self.adverbial_dict, self.predicate_cmd_dict]
        atom_translator = AtomTranslator(translate_guide, self.limit_num)

        return atom_translator


# # there are two options for position
# # 1 - 'before imply'
# # 2 - 'after imply'
# position = 'after_imply'
# # there are three options for position
# # 1 - 'default'
# # 2 - 'SE'
# # 3 - 'ERE'
# type_preference = 'default'
# limit_num = parameters.limit_num_atom
#
# atom_handler = AtomHandler(position, type_preference, limit_num)
# print(atom_handler.atom_translator.atom_info_dict)
# print('\n')
# atom_handler.atom_translator.display_assemble_guide()
# # atom_handler.atom_translator.display_translation()
# atom_handler.atom_translator.display_random_translation()
