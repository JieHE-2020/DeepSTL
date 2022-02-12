from translation.level_1.atom.atom_template_refiner import AtomTemplateRefiner


class AlwaysAtomTemplateRefiner(AtomTemplateRefiner):
    def __init__(self, info_dict, predicate_cmd_dict, positive_predicate_version):
        self.positive_predicate_version = positive_predicate_version
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
            if self.positive_predicate_version == 'alwaysUseDuration':
                template_key, mood = 'predicate_duration', 'positive'
            if self.positive_predicate_version == 'alwaysUseLogic':
                template_key, mood = 'predicate_logic', 'positive'

        if channel == 'positive_expr_for_negative_clause':
            if self.positive_predicate_version == 'alwaysUseDuration':
                template_key, mood = 'predicate_positive_duration', 'positive'
            if self.positive_predicate_version == 'alwaysUseLogic':
                template_key, mood = 'predicate_positive_logic', 'positive'

        return template_key, mood
