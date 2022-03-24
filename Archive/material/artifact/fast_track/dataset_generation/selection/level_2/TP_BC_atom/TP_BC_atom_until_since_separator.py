from grammar.level_2.TP_atom_BC_atom import original_TP_SP_rules
import copy


class TPBCAtomUntilSinceSeparator:
    def __init__(self, tp_info_dict):
        self.tp_info_dict = tp_info_dict
        if self.tp_info_dict['type'][1] == 'until':
            [self.always_info_dict, self.eventually_info_dict] = self.until_separate()
        else:  # self.tp_info_dict['type'][1] == 'since':
            [self.historically_info_dict, self.once_info_dict] = self.since_separate()

    def until_separate(self):
        until_info_dict = copy.deepcopy(self.tp_info_dict)
        # create a dictionary with 'always' information
        always_info_dict = copy.deepcopy(original_TP_SP_rules.TP[1][0])
        del always_info_dict['probability']
        if until_info_dict['ingredient'][0]['type'][0] == 'BC_Atom':  # type of SP for 'always' operator
            always_info_dict['type'][0] = always_info_dict['type'][0] + '_BC_Atom'
        else:
            always_info_dict['type'][0] = always_info_dict['type'][0] + '_Atom'
        # assemble the newly created 'always' dictionary
        always_info_dict['ingredient'][0] = until_info_dict['ingredient'][0]  # sp_dict for always
        # replace expression
        sp_expr_always = always_info_dict['ingredient'][0]['expression']      # sp expression
        always_info_dict['expression'] = \
            always_info_dict['expression'].replace('SP_expr', sp_expr_always)

        if until_info_dict['index'] == [4, 0]:
            # create a dictionary with 'eventually' information
            eventually_info_dict = copy.deepcopy(original_TP_SP_rules.TP[0][0])
            del eventually_info_dict['probability']
            if until_info_dict['ingredient'][1]['type'][0] == 'BC_Atom':  # type of SP for 'eventually' operator
                eventually_info_dict['type'][0] = eventually_info_dict['type'][0] + '_BC_Atom'
            else:
                eventually_info_dict['type'][0] = eventually_info_dict['type'][0] + '_Atom'
            # assemble the newly created 'eventually' dictionary
            eventually_info_dict['ingredient'][0] = until_info_dict['ingredient'][1]  # sp_dict for eventually
            # replace expression
            sp_expr_eventually = eventually_info_dict['ingredient'][0]['expression']  # sp expression
            eventually_info_dict['expression'] = \
                eventually_info_dict['expression'].replace('SP_expr', sp_expr_eventually)

        elif until_info_dict['index'] == [4, 1]:
            # create a dictionary with 'eventually' information
            eventually_info_dict = copy.deepcopy(original_TP_SP_rules.TP[0][1])
            del eventually_info_dict['probability']
            if until_info_dict['ingredient'][1]['type'][0] == 'BC_Atom':  # type of SP for 'eventually' operator
                eventually_info_dict['type'][0] = eventually_info_dict['type'][0] + '_BC_Atom'
            else:
                eventually_info_dict['type'][0] = eventually_info_dict['type'][0] + '_Atom'
            # assemble the newly created 'eventually' dictionary
            eventually_info_dict['ingredient'][0] = until_info_dict['ingredient'][1]  # sp_dict for eventually
            eventually_info_dict['ingredient'][1] = until_info_dict['ingredient'][2]  # t_value for eventually
            # replace expression
            sp_expr_eventually = eventually_info_dict['ingredient'][0]['expression']  # sp expression
            eventually_info_dict['expression'] = \
                eventually_info_dict['expression'].replace('t_value', eventually_info_dict['ingredient'][1])
            eventually_info_dict['expression'] = \
                eventually_info_dict['expression'].replace('SP_expr', sp_expr_eventually)

        else:  # until_info_dict['index'] == [4, 2]
            eventually_info_dict = copy.deepcopy(original_TP_SP_rules.TP[0][2])
            del eventually_info_dict['probability']
            if until_info_dict['ingredient'][1]['type'][0] == 'BC_Atom':  # type of SP for 'eventually' operator
                eventually_info_dict['type'][0] = eventually_info_dict['type'][0] + '_BC_Atom'
            else:
                eventually_info_dict['type'][0] = eventually_info_dict['type'][0] + '_Atom'
            # assemble the newly created 'eventually' dictionary
            eventually_info_dict['ingredient'][0] = until_info_dict['ingredient'][1]  # sp_dict for eventually
            eventually_info_dict['ingredient'][1] = until_info_dict['ingredient'][2]  # t_value_a for eventually
            eventually_info_dict['ingredient'][2] = until_info_dict['ingredient'][3]  # t_value_b for eventually
            # replace expression
            sp_expr_eventually = eventually_info_dict['ingredient'][0]['expression']  # sp expression
            eventually_info_dict['expression'] = \
                eventually_info_dict['expression'].replace('t_value_a', eventually_info_dict['ingredient'][1])
            eventually_info_dict['expression'] = \
                eventually_info_dict['expression'].replace('t_value_b', eventually_info_dict['ingredient'][2])
            eventually_info_dict['expression'] = \
                eventually_info_dict['expression'].replace('SP_expr', sp_expr_eventually)

        return [always_info_dict, eventually_info_dict]

    def since_separate(self):
        since_info_dict = copy.deepcopy(self.tp_info_dict)
        # create a dictionary with 'historically' information
        historically_info_dict = copy.deepcopy(original_TP_SP_rules.TP[3][0])
        del historically_info_dict['probability']
        if since_info_dict['ingredient'][0]['type'][0] == 'BC_Atom':  # type of SP for 'historically' operator
            historically_info_dict['type'][0] = historically_info_dict['type'][0] + '_BC_Atom'
        else:
            historically_info_dict['type'][0] = historically_info_dict['type'][0] + '_Atom'
        # assemble the newly created 'historically' dictionary
        historically_info_dict['ingredient'][0] = since_info_dict['ingredient'][0]    # sp_dict for historically
        # replace expression
        sp_expr_historically = historically_info_dict['ingredient'][0]['expression']  # sp expression
        historically_info_dict['expression'] = \
            historically_info_dict['expression'].replace('SP_expr', sp_expr_historically)

        if since_info_dict['index'] == [5, 0]:
            # create a dictionary with 'once' information
            once_info_dict = copy.deepcopy(original_TP_SP_rules.TP[2][0])
            del once_info_dict['probability']
            if since_info_dict['ingredient'][1]['type'][0] == 'BC_Atom':  # type of SP for 'once' operator
                once_info_dict['type'][0] = once_info_dict['type'][0] + '_BC_Atom'
            else:
                once_info_dict['type'][0] = once_info_dict['type'][0] + '_Atom'
            # assemble the newly created 'once' dictionary
            once_info_dict['ingredient'][0] = since_info_dict['ingredient'][1]  # sp_dict for once
            # replace expression
            sp_expr_once = once_info_dict['ingredient'][0]['expression']  # sp expression
            once_info_dict['expression'] = \
                once_info_dict['expression'].replace('SP_expr', sp_expr_once)

        elif since_info_dict['index'] == [5, 1]:
            # create a dictionary with 'once' information
            once_info_dict = copy.deepcopy(original_TP_SP_rules.TP[2][1])
            del once_info_dict['probability']
            if since_info_dict['ingredient'][1]['type'][0] == 'BC_Atom':  # type of SP for 'once' operator
                once_info_dict['type'][0] = once_info_dict['type'][0] + '_BC_Atom'
            else:
                once_info_dict['type'][0] = once_info_dict['type'][0] + '_Atom'
            # assemble the newly created 'once' dictionary
            once_info_dict['ingredient'][0] = since_info_dict['ingredient'][1]  # sp_dict for once
            once_info_dict['ingredient'][1] = since_info_dict['ingredient'][2]  # t_value for once
            # replace expression
            sp_expr_once = once_info_dict['ingredient'][0]['expression']  # sp expression
            once_info_dict['expression'] = \
                once_info_dict['expression'].replace('t_value', once_info_dict['ingredient'][1])
            once_info_dict['expression'] = \
                once_info_dict['expression'].replace('SP_expr', sp_expr_once)

        else:  # since_info_dict['index'] == [5, 2]
            once_info_dict = copy.deepcopy(original_TP_SP_rules.TP[2][2])
            del once_info_dict['probability']
            if since_info_dict['ingredient'][1]['type'][0] == 'BC_Atom':  # type of SP for 'once' operator
                once_info_dict['type'][0] = once_info_dict['type'][0] + '_BC_Atom'
            else:
                once_info_dict['type'][0] = once_info_dict['type'][0] + '_Atom'
            # assemble the newly created 'once' dictionary
            once_info_dict['ingredient'][0] = since_info_dict['ingredient'][1]  # sp_dict for once
            once_info_dict['ingredient'][1] = since_info_dict['ingredient'][2]  # t_value_a for once
            once_info_dict['ingredient'][2] = since_info_dict['ingredient'][3]  # t_value_b for once
            # replace expression
            sp_expr_once = once_info_dict['ingredient'][0]['expression']  # sp expression
            once_info_dict['expression'] = \
                once_info_dict['expression'].replace('t_value_a', once_info_dict['ingredient'][1])
            once_info_dict['expression'] = \
                once_info_dict['expression'].replace('t_value_b', once_info_dict['ingredient'][2])
            once_info_dict['expression'] = \
                once_info_dict['expression'].replace('SP_expr', sp_expr_once)

        return [historically_info_dict, once_info_dict]

