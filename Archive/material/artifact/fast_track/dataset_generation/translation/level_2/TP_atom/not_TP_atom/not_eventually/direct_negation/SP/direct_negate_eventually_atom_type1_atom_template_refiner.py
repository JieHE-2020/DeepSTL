from translation.level_1.atom.atom_template_refiner import AtomTemplateRefiner


class DirectNegateEventuallyAtomType1AtomTemplateRefiner(AtomTemplateRefiner):

    def se_negative_refine(self, category, sub_category):
        # process the template of subject
        subject_refined = self.sub_obj_extractor.se_sub_process()

        # process the template of negative predicate
        template_key, mood = 'predicate_negative_logic', 'negative'
        predicate_refined = self.predicate_refine(template_key, mood)

        # process the template of object
        object_refined = self.sub_obj_extractor.se_obj_process(category, sub_category, mood)

        # combine all negative English templates plus clause type and mood into a dictionary
        # and append it into self.refined_template
        # the value of key 'clause_type' means there are no prefix or suffix in the translation
        refined_template_dict = {'clause_type': 'NoPrefixNoSuffix',
                                 'mood': mood,
                                 'subject_refined': subject_refined,
                                 'predicate_refined': predicate_refined,
                                 'object_refined': object_refined
                                 }
        self.assemble_guide.append(refined_template_dict)

        # do not process the template of the positive predicate
