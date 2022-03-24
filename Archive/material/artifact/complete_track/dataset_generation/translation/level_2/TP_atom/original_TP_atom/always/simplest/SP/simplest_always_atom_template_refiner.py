from translation.level_1.atom.atom_template_refiner import AtomTemplateRefiner


class SimplestAlwaysAtomTemplateRefiner(AtomTemplateRefiner):
    def __init__(self, info_dict, predicate_cmd_dict, positive_predicate_version, whether_from_not_eventually=False):
        self.positive_predicate_version = positive_predicate_version
        self.whether_from_not_eventually = whether_from_not_eventually
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

    # override function 'se_not_event_refine' in class AtomTemplateRefiner
    def se_not_event_refine(self, category, sub_category):
        # 1. subject_refined is the real subject
        # process the template of subject
        subject_refined = self.sub_obj_extractor.se_sub_process()

        # process the template of predicate
        template_key, mood = 'predicate_action', 'negative'
        predicate_refined = self.predicate_refine(template_key, mood)

        # process the template of object
        object_refined = self.sub_obj_extractor.se_obj_process(category, sub_category, mood)

        # combine all English templates plus clause type and mood
        # the value of key 'clause_type' means there are no prefix or suffix in the translation
        refined_template_dict = {'clause_type': 'NoPrefixNoSuffix',
                                 'mood': mood,
                                 'subject_refined': subject_refined,
                                 'predicate_refined': predicate_refined,
                                 'object_refined': object_refined
                                 }
        self.assemble_guide.append(refined_template_dict)

        # 2. do not consider the scenario that prefix is the real subject
