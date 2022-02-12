from grammar.level_2.TP_atom_BC_atom import original_TP_SP_rules
from selection.level_2.TP_atom.TP_atom_restorer import TPAtomRestorer
from selection.level_2.TP_BC_atom.not_TP_BC_atom_selector import NotTPBCAtomSelector
from selection.level_2.TP_BC_atom.rise_TP_BC_atom_selector import RiseTPBCAtomSelector
from selection.level_2.TP_BC_atom.fall_TP_BC_atom_selector import FallTPBCAtomSelector
from selection.level_2.TP_BC_atom.not_rise_TP_BC_atom_selector import NotRiseTPBCAtomSelector
from selection.level_2.TP_BC_atom.not_fall_TP_BC_atom_selector import NotFallTPBCAtomSelector
import copy


class TPBCAtomRestorer(TPAtomRestorer):

    def tp_restore_process(self, category, sub_category):
        tp_info_dict = copy.deepcopy(original_TP_SP_rules.TP[category][sub_category])
        del tp_info_dict['probability']
        tp_info_dict['type'][0] = tp_info_dict['type'][0] + '_BC_Atom'

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


modified_tp_bc_atom_selector = RiseTPBCAtomSelector('random')
tp_bc_atom_restorer = TPBCAtomRestorer(modified_tp_bc_atom_selector.rise_tp_info_dict)
print(tp_bc_atom_restorer.modified_tp_info_dict)
print(tp_bc_atom_restorer.tp_info_dict)
