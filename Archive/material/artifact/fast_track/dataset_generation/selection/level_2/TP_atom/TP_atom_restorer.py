from grammar.level_2.TP_atom_BC_atom import original_TP_SP_rules
from selection.level_2.TP_atom.not_TP_atom_selector import NotTPAtomSelector
from selection.level_2.TP_atom.rise_TP_atom_selector import RiseTPAtomSelector
from selection.level_2.TP_atom.fall_TP_atom_selector import FallTPAtomSelector
from selection.level_2.TP_atom.not_rise_TP_atom_selector import NotRiseTPAtomSelector
from selection.level_2.TP_atom.not_fall_TP_atom_selector import NotFallTPAtomSelector
import copy


class TPAtomRestorer:
    def __init__(self, modified_tp_info_dict):
        self.modified_tp_info_dict = copy.deepcopy(modified_tp_info_dict)

        category = self.modified_tp_info_dict['index'][0]
        sub_category = self.modified_tp_info_dict['index'][1]
        self.tp_info_dict = self.tp_restore_process(category, sub_category)

    def tp_restore_process(self, category, sub_category):
        tp_info_dict = copy.deepcopy(original_TP_SP_rules.TP[category][sub_category])
        del tp_info_dict['probability']
        tp_info_dict['type'][0] = tp_info_dict['type'][0] + '_Atom'

        # start transformation
        # key 'type' and key 'index' are set by default
        # process the value of key 'ingredient'
        tp_info_dict['ingredient'] = copy.deepcopy(self.modified_tp_info_dict['ingredient'])
        # process the value of key 'expression'
        if 0 <= category <= 3:
            updated_expression = self.tp_expression_update(tp_info_dict)
        else:  # category == 4 or category == 5
            updated_expression = self.until_since_expression_update(tp_info_dict)
        tp_info_dict['expression'] = updated_expression

        return tp_info_dict

    @staticmethod
    def tp_expression_update(tp_info_dict):
        sub_category = tp_info_dict['index'][1]
        ingredient = tp_info_dict['ingredient']
        sp_expr = ingredient[0]['expression']
        tp_expr = tp_info_dict['expression']

        if sub_category == 0:
            tp_expr = tp_expr.replace('SP_expr', sp_expr)
        if sub_category == 1:
            tp_expr = tp_expr.replace('t_value', ingredient[1])
            tp_expr = tp_expr.replace('SP_expr', sp_expr)
        if sub_category == 2:
            tp_expr = tp_expr.replace('t_value_a', ingredient[1])
            tp_expr = tp_expr.replace('t_value_b', ingredient[2])
            tp_expr = tp_expr.replace('SP_expr', sp_expr)

        return tp_expr

    @staticmethod
    def until_since_expression_update(tp_info_dict):
        sub_category = tp_info_dict['index'][1]
        ingredient = tp_info_dict['ingredient']
        sp_expr_1 = ingredient[0]['expression']
        sp_expr_2 = ingredient[1]['expression']
        tp_expr = tp_info_dict['expression']

        if sub_category == 0:
            tp_expr = tp_expr.replace('SP_expr_1', sp_expr_1)
            tp_expr = tp_expr.replace('SP_expr_2', sp_expr_2)
        if sub_category == 1:
            tp_expr = tp_expr.replace('t_value', ingredient[2])
            tp_expr = tp_expr.replace('SP_expr_1', sp_expr_1)
            tp_expr = tp_expr.replace('SP_expr_2', sp_expr_2)
        if sub_category == 2:
            tp_expr = tp_expr.replace('t_value_a', ingredient[2])
            tp_expr = tp_expr.replace('t_value_b', ingredient[3])
            tp_expr = tp_expr.replace('SP_expr_1', sp_expr_1)
            tp_expr = tp_expr.replace('SP_expr_2', sp_expr_2)

        return tp_expr


# modified_tp_atom_selector = RiseTPAtomSelector('random')
# tp_atom_restorer = TPAtomRestorer(modified_tp_atom_selector.rise_tp_info_dict)
# print(tp_atom_restorer.modified_tp_info_dict)
# print(tp_atom_restorer.tp_info_dict)
