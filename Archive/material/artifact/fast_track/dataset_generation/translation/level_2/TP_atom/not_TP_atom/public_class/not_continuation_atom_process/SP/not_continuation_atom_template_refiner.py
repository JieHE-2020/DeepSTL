from translation.level_1.atom.atom_template_refiner import AtomTemplateRefiner
from translation.level_1.atom.predicate_operation.not_continuation_predicate_refiner \
    import NotContinuationPredicateRefiner
import copy


class NotContinuationAtomTemplateRefiner(AtomTemplateRefiner):
    def __init__(self, info_dict, predicate_cmd_dict, positive_predicate_version):
        self.positive_predicate_version = positive_predicate_version
        self.not_continuation_predicate_refiner = NotContinuationPredicateRefiner()
        super().__init__(info_dict, predicate_cmd_dict)

    # override function 'positive_predicate_select' in class AtomTemplateRefiner
    def positive_predicate_select(self, channel):
        # for main_type1:
        # positive_predicate_version == 'alwaysUseDuration'
        # for main_type2_main_part:
        # positive_predicate_version == 'alwaysUseLogic'

        template_key = ''
        mood = ''

        if channel == 'pure_positive':
            ######################################################################################
            # This is the only executed part in this class, hence only need to modify this part!
            # when channel == 'pure_positive', deliberately set the mood as 'negative'
            # so that the negation operation in the predicate part can be started!
            if self.positive_predicate_version == 'alwaysUseDuration':
                template_key, mood = 'predicate_duration', 'negative'
            ######################################################################################
            if self.positive_predicate_version == 'alwaysUseLogic':
                template_key, mood = 'predicate_logic', 'positive'

        if channel == 'positive_expr_for_negative_clause':
            if self.positive_predicate_version == 'alwaysUseDuration':
                template_key, mood = 'predicate_positive_duration', 'positive'
            if self.positive_predicate_version == 'alwaysUseLogic':
                template_key, mood = 'predicate_positive_logic', 'positive'

        return template_key, mood

    # override function 'predicate_refine' in class AtomTemplateRefiner
    def predicate_refine(self, key, mood, appositive='appositiveDisabled'):
        predicate_template = copy.deepcopy(self.template[key])
        if appositive == 'appositiveDisabled':  # by default
            commands_selected = copy.deepcopy(self.main_predicate_cmd[mood])
        else:  # appositive == 'appositiveEnabled'
            commands_selected = copy.deepcopy(self.appositive_predicate_cmd[mood])
        predicate_refined = self.not_continuation_predicate_refiner.predicate_process(predicate_template, mood,
                                                                                      commands_selected)
        return predicate_refined
