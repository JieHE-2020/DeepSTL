import copy


class SubObjExtractor:
    def __init__(self, info_dict, template):
        self.info_dict = copy.deepcopy(info_dict)
        self.template = copy.deepcopy(template)
        self.subject_refined = list()
        self.object_refined = list()

    def se_sub_process(self):
        self.subject_refined = []

        sig = self.info_dict['ingredient'][0]
        for i in range(len(self.template['subject'])):
            subject_modified = self.template['subject'][i].replace('s#i#g', sig)
            self.subject_refined.append(subject_modified)

        return self.subject_refined

    def se_obj_process(self, category, sub_category, mood):
        self.object_refined = []

        # for category = 0, 1, 2, 4, only category is needed for object processing
        if 0 <= category <= 2:
            value = self.info_dict['ingredient'][1]
            for i in range(len(self.template['object'])):
                object_modified = self.template['object'][i].replace('value', value)
                self.object_refined.append(object_modified)

        if category == 4:
            mode = self.info_dict['ingredient'][1]
            for i in range(len(self.template['object'])):
                object_modified = self.template['object'][i].replace('mode', mode)
                self.object_refined.append(object_modified)

        # for category = 3, 5, category, sub_category and mood are all used for object processing
        if category == 3:
            value1 = self.info_dict['ingredient'][1]
            value2 = self.info_dict['ingredient'][2]

            if sub_category <= 3 or (4 <= sub_category <= 7 and mood == 'negative'):
                # object 1
                for i in range(len(self.template['object_1_adj_1'])):
                    for j in range(len(self.template['object_1_noun_1'])):
                        for k in range(len(self.template['object_1_conj'])):
                            for m in range(len(self.template['object_1_adj_2'])):
                                for n in range(len(self.template['object_1_noun_2'])):
                                    object_template = self.template['object_1_adj_1'][i] + ' ' + \
                                                      self.template['object_1_noun_1'][j] + ' ' + \
                                                      self.template['object_1_conj'][k] + ' ' + \
                                                      self.template['object_1_adj_2'][m] + ' ' + \
                                                      self.template['object_1_noun_2'][n]
                                    object_modified = object_template.replace('value1', value1)
                                    object_modified = object_modified.replace('value2', value2)
                                    self.object_refined.append(object_modified)

                # object 2
                for i in range(len(self.template['object_2_prep'])):
                    for j in range(len(self.template['object_2_noun'])):
                        object_template = self.template['object_2_prep'][i] + ' ' + self.template['object_2_noun'][j]
                        object_modified = object_template.replace('value1', value1)
                        object_modified = object_modified.replace('value2', value2)
                        self.object_refined.append(object_modified)

                # object 3
                for i in range(len(self.template['object_3_prep'])):
                    for j in range(len(self.template['object_3_noun'])):
                        object_template = self.template['object_3_prep'][i] + ' ' + self.template['object_3_noun'][j]
                        object_modified = object_template.replace('value1', value1)
                        object_modified = object_modified.replace('value2', value2)
                        self.object_refined.append(object_modified)

            if 4 <= sub_category <= 7 and mood == 'positive':
                for i in range(len(self.template['object_4_noun'])):
                    object_modified = self.template['object_4_noun'][i].replace('value1', value1)
                    object_modified = object_modified.replace('value2', value2)
                    self.object_refined.append(object_modified)

            if sub_category >= 8:
                for i in range(len(self.template['object'])):
                    object_modified = self.template['object'][i].replace('value1', value1)
                    object_modified = object_modified.replace('value2', value2)
                    self.object_refined.append(object_modified)

        if category == 5:
            mode1 = self.info_dict['ingredient'][1]
            mode2 = self.info_dict['ingredient'][2]

            if sub_category != 1 or (sub_category == 1 and mood == 'negative'):
                for i in range(len(self.template['object'])):
                    object_modified = self.template['object'][i].replace('mode1', mode1)
                    object_modified = object_modified.replace('mode2', mode2)
                    self.object_refined.append(object_modified)

            if sub_category == 1 and mood == 'positive':
                for i in range(len(self.template['object_special'])):
                    object_modified = self.template['object_special'][i].replace('mode1', mode1)
                    object_modified = object_modified.replace('mode2', mode2)
                    self.object_refined.append(object_modified)

        return self.object_refined

    def ere_sub_obj_process(self, category):
        self.subject_refined = []
        self.object_refined = []

        # process subject
        sig = self.info_dict['ingredient'][0]
        for i in range(len(self.template['subject'])):
            subject_modified = self.template['subject'][i].replace('s#i#g', sig)
            self.subject_refined.append(subject_modified)

        # process object
        if 0 <= category <= 2:
            value = self.info_dict['ingredient'][1]
            for i in range(len(self.template['object'])):
                object_modified = self.template['object'][i].replace('value', value)
                self.object_refined.append(object_modified)

        if category == 4:
            mode = self.info_dict['ingredient'][1]
            for i in range(len(self.template['object'])):
                object_modified = self.template['object'][i].replace('mode', mode)
                self.object_refined.append(object_modified)

        if category == 3:
            value1 = self.info_dict['ingredient'][1]
            value2 = self.info_dict['ingredient'][2]
            for i in range(len(self.template['object'])):
                object_modified = self.template['object'][i].replace('value1', value1)
                object_modified = object_modified.replace('value2', value2)
                self.object_refined.append(object_modified)

        if category == 5:
            mode1 = self.info_dict['ingredient'][1]
            mode2 = self.info_dict['ingredient'][2]
            for i in range(len(self.template['object'])):
                object_modified = self.template['object'][i].replace('mode1', mode1)
                object_modified = object_modified.replace('mode2', mode2)
                self.object_refined.append(object_modified)

        return [self.subject_refined, self.object_refined]
