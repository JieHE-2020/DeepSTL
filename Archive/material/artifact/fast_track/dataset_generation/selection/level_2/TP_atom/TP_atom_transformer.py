from grammar.level_2.TP_atom_BC_atom import not_TP_SP_rules
from grammar.level_1.atom import atom_rules
from selection.level_2.TP_atom.not_TP_atom_selector import NotTPAtomSelector
import copy


class TPAtomTransformer:
    def __init__(self, not_tp_info_dict):
        self.not_tp_info_dict = copy.deepcopy(not_tp_info_dict)

        category = self.not_tp_info_dict['index'][0]
        sub_category = self.not_tp_info_dict['index'][1]
        if 0 <= category <= 3:
            self.tp_info_dict = self.tp_transform_process(category, sub_category)
        else:  # category == 4 or category == 5
            print('error')

    def tp_transform_process(self, category, sub_category):
        tp_info_dict = copy.deepcopy(not_TP_SP_rules.negate_TP_matrix[category][sub_category])
        del tp_info_dict['probability']

        # start transformation
        # key 'type' and key 'index' are set by default
        # process the value of key 'ingredient'
        tp_info_dict['ingredient'] = copy.deepcopy(self.not_tp_info_dict['ingredient'])
        sp_info_dict = tp_info_dict['ingredient'][0]
        negate_sp_info_dict = self.atom_transform_process(sp_info_dict)
        tp_info_dict['ingredient'][0] = negate_sp_info_dict  # substitution

        # process the value of key 'expression'
        updated_expression = self.tp_expression_update(tp_info_dict)
        tp_info_dict['expression'] = updated_expression

        return tp_info_dict

    def atom_transform_process(self, sp_info_dict):
        category = sp_info_dict['index'][0]
        sub_category = sp_info_dict['index'][1]
        if sp_info_dict['type'] == 'SE':
            negate_sp_info_dict = copy.deepcopy(atom_rules.negate_SE_matrix[category][sub_category])
        else:  # sp_info_dict['type'] == 'ERE'
            negate_sp_info_dict = copy.deepcopy(atom_rules.negate_ERE_matrix[category][sub_category])
        del negate_sp_info_dict['probability']

        # start transformation
        # key 'type' and key 'index' are set by default
        # process the value of key 'ingredient'
        negate_sp_info_dict['ingredient'] = copy.deepcopy(sp_info_dict['ingredient'])
        # process the value of key 'expression'
        updated_expression = self.sp_expression_update(negate_sp_info_dict)
        negate_sp_info_dict['expression'] = updated_expression

        return negate_sp_info_dict

    @staticmethod
    def sp_expression_update(negate_sp_info_dict):
        category = negate_sp_info_dict['index'][0]
        ingredient = negate_sp_info_dict['ingredient']
        expression = negate_sp_info_dict['expression']

        if category == 0 or category == 1 or category == 2:
            expression = expression.replace('sig', ingredient[0])
            expression = expression.replace('value', ingredient[1])

        elif category == 3:
            expression = expression.replace('sig', ingredient[0])
            expression = expression.replace('value1', ingredient[1])
            expression = expression.replace('value2', ingredient[2])

        elif category == 4:
            expression = expression.replace('sig', ingredient[0])
            expression = expression.replace('mode', ingredient[1])

        else:  # category == 5
            expression = expression.replace('sig', ingredient[0])
            expression = expression.replace('mode1', ingredient[1])
            expression = expression.replace('mode2', ingredient[2])

        return expression

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


# not_tp_atom_selector = NotTPAtomSelector('eventually')
# tp_atom_transformer = TPAtomTransformer(not_tp_atom_selector.not_tp_info_dict)
# print(tp_atom_transformer.not_tp_info_dict)
# print(tp_atom_transformer.tp_info_dict)
