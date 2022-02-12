from selection.level_2.TP_atom.not_TP_atom_selector import NotTPAtomSelector
from selection.level_2.TP_atom.TP_atom_transformer import TPAtomTransformer
from selection.level_2.TP_atom.TP_atom_restorer import TPAtomRestorer
from translation.level_2.TP_atom.not_TP_atom.not_historically.not_historically_atom_translator \
    import NotHistoricallyAtomTranslator
from public import parameters


class NotHistoricallyAtomHandler:

    def __init__(self, position, nest_info_dict, limit_num):
        self.position = position
        self.nest_info_dict = nest_info_dict
        # the number of randomly selected translations
        self.limit_num = limit_num
        self.distribution_vector = {
            # # option 1 - support transformation
            # # direct negate : appositive/appendix : transformation = 45 : 20 : 35
            # 'with_direct_negate': [0.45, 0.20, 0.35],
            # # appositive/appendix : transformation = 20 : 80
            # 'without_direct_negate': [0.20, 0.80]

            # option 2 - do not support transformation
            # direct negate : appositive/appendix : transformation = 80 : 20 : 0
            'with_direct_negate': [0.80, 0.20, 0],
            # appositive/appendix : transformation = 100 : 0
            'without_direct_negate': [1, 0]
        }

        # prepare materials for translation
        self.not_historically_info_dict = self.not_tp_select()
        self.historically_info_dict = self.tp_restore()
        self.once_not_info_dict = self.tp_transform()
        self.instruction_dict = self.instruction_assemble()

        self.not_historically_atom_translator = self.translate_process()

    @staticmethod
    def not_tp_select():
        not_tp_type = 'historically'
        not_tp_selector = NotTPAtomSelector(not_tp_type)
        not_tp_info_dict = not_tp_selector.not_tp_info_dict

        return not_tp_info_dict

    def tp_restore(self):
        tp_restorer = TPAtomRestorer(self.not_historically_info_dict)
        tp_info_dict = tp_restorer.tp_info_dict

        return tp_info_dict

    def tp_transform(self):
        tp_transformer = TPAtomTransformer(self.not_historically_info_dict)
        tp_info_dict = tp_transformer.tp_info_dict

        return tp_info_dict

    def instruction_assemble(self):
        instruction_dict = {
            'position': self.position,
            'nest_info_dict': self.nest_info_dict
        }

        return instruction_dict

    def translate_process(self):
        translate_guide = {
            'not_historically_info_dict': self.not_historically_info_dict,
            'historically_info_dict': self.historically_info_dict,
            'once_not_info_dict': self.once_not_info_dict,
            'instruction_dict': self.instruction_dict
        }
        not_historically_atom_translator = NotHistoricallyAtomTranslator(translate_guide, self.limit_num,
                                                                         self.distribution_vector)

        return not_historically_atom_translator


# group_num = 3
# abnormal_record = {
#     'not_historically_atom': []
# }
#
# # information of position: two options
# # 1 - 'before_imply'
# # 2 - 'after_imply'
# position = 'after_imply'
#
# # information of nesting
# nest_info_dict = {
#     'whetherNest': False,
#     'nestLayer': 1,
#     'whetherBottom': True,
#     'hasParallelSuccessor': False,
#     'tense': 'present'
# }
#
# for i in range(group_num):
#     limit_num = parameters.limit_num_tp_atom_normal
#     not_historically_atom_handler = NotHistoricallyAtomHandler(position, nest_info_dict, limit_num)
#     print(not_historically_atom_handler.not_historically_info_dict)
#     print(not_historically_atom_handler.not_historically_info_dict['expression'])
#     print(not_historically_atom_handler.historically_info_dict['expression'])
#     print(not_historically_atom_handler.once_not_info_dict['expression'])
#     print('\n')
#     not_historically_atom_handler.not_historically_atom_translator.display_random_translation()
#     num = len(not_historically_atom_handler.not_historically_atom_translator.random_shuffled_translations)
#     if num != 1000:
#         abnormal_record['not_historically_atom'].append(i+1)
#         abnormal_record['not_historically_atom'].\
#             append(not_historically_atom_handler.not_historically_info_dict['expression'])
#     print('not_historically_atom:', i+1)
#
# print(abnormal_record)
