from corpus import basic_words
import random
import copy
import math


class AtomAssembler:
    """
    Assembling rules:
    For English translations of an atom expression (SE or ERE):
    1. the format of subjects and objects is randomly chosen;
    2. the diversity of predicates and adverbial modifiers (i.e., adverbs
       and adverbial phrases) is reserved;
    3. all possible positions of adverbs and adverbial phrases are considered.
    """

    def __init__(self, adverbial_query, assemble_guide, adverbial_para):
        self.adverbial_query = copy.deepcopy(adverbial_query)
        self.assemble_guide = copy.deepcopy(assemble_guide)
        self.adverbial_para = copy.deepcopy(adverbial_para)
        self.eng_list = list()
        self.assemble_guide_extract()

    def assemble_guide_extract(self):
        assemble_guide = copy.deepcopy(self.assemble_guide)
        while len(assemble_guide) != 0:
            refined_template_dict = assemble_guide.pop()
            if refined_template_dict['clause_type'] == 'NoPrefixNoSuffix':
                self.atom_assemble_no_prefix_no_suffix(refined_template_dict)
            if refined_template_dict['clause_type'] == 'PrefixSuffix':
                self.atom_assemble_with_prefix_suffix(refined_template_dict)

    def atom_assemble_no_prefix_no_suffix(self, refined_template_dict):
        clause_type = refined_template_dict['clause_type']
        mood = refined_template_dict['mood']
        subject_refined = refined_template_dict['subject_refined']
        predicate_refined = refined_template_dict['predicate_refined']
        object_refined = refined_template_dict['object_refined']

        for i in range(len(predicate_refined)):
            for predicate in predicate_refined[i]:
                # detect whether there is anomaly
                abnormal_result = self.detect_anomaly_no_prefix_no_suffix(predicate)
                if abnormal_result:
                    # if anomaly is detected, adopt random dropping with a large probability
                    point = random.randint(1, 100)
                    if point <= 80:
                        continue
                clause_para = [subject_refined, predicate, object_refined]
                eng = self.random_select(clause_para, clause_type)
                self.eng_list.append(eng)

                # consider adverbial modification
                if self.adverbial_query == 'adverbialEnabled':
                    # check whether 'predicate' contains any adverb'
                    flag = self.check_adverb_existence(predicate)
                    """
                    If flag == 0, then 'predicate' doesn't contain any adverbs.
                    Generate new translations with adverbs and adverbial phrases added in
                    the beginning or end of the clause according to different scenarios
                    NOTE: In the following procedure, predicate is reserved while subject and object
                    are randomly chosen again.
                    """
                    if flag == 0:
                        # prepare and assemble the parameters for the downstream function
                        string_para = [mood, clause_type]
                        eng_list_adverbialAdded = self.random_adverbial_augment(clause_para, string_para)
                        # if anomaly is detected but it has not been dropped, the translations added by
                        # adverbial modifiers should be cut down to a limited number
                        if abnormal_result:
                            eng_list_adverbialAdded = random.sample(eng_list_adverbialAdded,
                                                                    math.ceil(len(eng_list_adverbialAdded) / 5))
                        self.eng_list = self.eng_list + eng_list_adverbialAdded

    def atom_assemble_with_prefix_suffix(self, refined_template_dict):
        clause_type = refined_template_dict['clause_type']
        mood = refined_template_dict['mood']
        prefix = refined_template_dict['prefix']
        subject_refined = refined_template_dict['subject_refined']
        slave_predicate_refined = refined_template_dict['slave_predicate_refined']
        object_refined = refined_template_dict['object_refined']
        master_predicate_refined = refined_template_dict['suffix']

        for i in range(len(slave_predicate_refined)):
            for slave_predicate in slave_predicate_refined[i]:
                for j in range(len(master_predicate_refined)):
                    for master_predicate in master_predicate_refined[j]:
                        # detect whether there is anomaly
                        abnormal_result = self.detect_anomaly_with_prefix_suffix(slave_predicate, master_predicate)
                        if abnormal_result:
                            # if anomaly is detected, adopt random dropping with a large probability
                            point = random.randint(1, 100)
                            if point <= 80:
                                continue
                        clause_para = [prefix, subject_refined, slave_predicate,
                                       object_refined, master_predicate]
                        eng = self.random_select(clause_para, clause_type)
                        self.eng_list.append(eng)

                        # consider adverbial modification
                        if self.adverbial_query == 'adverbialEnabled':
                            # check whether 'predicate' contains any adverbs
                            flag = self.check_adverb_existence(master_predicate)
                            """
                            If flag == 0, then 'predicate' doesn't contain any adverbs.
                            Generate new translations with adverbs and adverbial phrases added in
                            the beginning or end of the clause according to different scenarios
                            NOTE: In the following procedure, slave_predicate and master_predicate are
                            reserved while prefix, subject and object are randomly chosen again.
                            """
                            if flag == 0:
                                # prepare and assemble the parameters for the downstream function
                                string_para = [mood, clause_type]
                                eng_list_adverbialAdded = self.random_adverbial_augment(clause_para, string_para)
                                # if anomaly is detected but dropping has not been exerted, the translations added by
                                # adverbial modifiers should be cut down to a limited number
                                if abnormal_result:
                                    eng_list_adverbialAdded = random.sample(eng_list_adverbialAdded,
                                                                            math.ceil(len(eng_list_adverbialAdded) / 5))
                                self.eng_list = self.eng_list + eng_list_adverbialAdded

    @staticmethod
    def detect_anomaly_no_prefix_no_suffix(predicate):
        result = False
        # detection 1: 'be being' or 'been being' appears
        if 'be being' in predicate or 'been being' in predicate:
            result = True
        return result

    @staticmethod
    def detect_anomaly_with_prefix_suffix(slave_predicate, master_predicate):
        result = False

        # detection 1: 'get' and its variants are used in both slave_predicate and master_predicate
        get_variant_list = copy.deepcopy(basic_words.verb_bank['get'])
        get_variant_set = set(get_variant_list)

        slave_predicate_list = slave_predicate.split(' ')  # string -> list
        slave_predicate_set = set(slave_predicate_list)  # list -> set

        master_predicate_list = master_predicate.split(' ')  # string -> list
        master_predicate_set = set(master_predicate_list)  # list -> set

        if slave_predicate_set.intersection(get_variant_set) != set() \
                and master_predicate_set.intersection(get_variant_set) != set():
            result = True

        # detection 2: 'be being' or 'been being' appears
        if 'be being' in master_predicate or 'been being' in master_predicate:
            result = True

        return result

    def check_adverb_existence(self, predicate):
        adverb_list_checked = copy.deepcopy(self.adverbial_para[0])
        flag = 0
        for scanned_word in adverb_list_checked:
            if scanned_word in predicate:
                flag = 1

        return flag

    def random_adverbial_augment(self, clause_para, string_para):
        # extract variables from function parameters
        mood = string_para[0]
        clause_type = string_para[1]
        eng_list_adverbialAdded = []

        """
        The position of adverbs and adverbial phrases are considered as follows:
        Type 1: pure SP
        1. for positive clause, adverbs and adverbial phrases can be added to 
           both the beginning or the end of the clause
        2. for negative clause, adverbs and adverbial phrases are only added
           to the beginning of the clause
        """

        if mood == 'positive':
            for word in self.adverbial_para[0]:
                eng = self.random_select(clause_para, clause_type)
                eng_update = word + ' ' + eng
                eng_list_adverbialAdded.append(eng_update)

                eng = self.random_select(clause_para, clause_type)
                eng_update = eng + ' ' + word
                eng_list_adverbialAdded.append(eng_update)

            for phrase in self.adverbial_para[1]:
                eng = self.random_select(clause_para, clause_type)
                eng_update = phrase + ' ' + eng
                eng_list_adverbialAdded.append(eng_update)

                eng = self.random_select(clause_para, clause_type)
                eng_update = eng + ' ' + phrase
                eng_list_adverbialAdded.append(eng_update)

        else:  # mood == 'negative':
            for word in self.adverbial_para[0]:
                eng = self.random_select(clause_para, clause_type)
                eng_update = word + ' ' + eng
                eng_list_adverbialAdded.append(eng_update)

            for phrase in self.adverbial_para[1]:
                eng = self.random_select(clause_para, clause_type)
                eng_update = phrase + ' ' + eng
                eng_list_adverbialAdded.append(eng_update)

        return eng_list_adverbialAdded

    @staticmethod
    def random_select(clause_para, clause_type):
        eng = str()
        if clause_type == 'NoPrefixNoSuffix':
            # randomly choose a subject in the 'subject_refined' list
            eng_subject = random.choice(clause_para[0])
            eng_predicate = clause_para[1]
            # randomly choose an object in the 'object_refined' list
            eng_object = random.choice(clause_para[2])
            eng = eng_subject + ' ' + eng_predicate + ' ' + eng_object

        if clause_type == 'PrefixSuffix':
            # randomly choose a prefix in the 'prefix' list
            eng_prefix = random.choice(clause_para[0])
            # randomly choose a subject in the 'subject_refined' list
            eng_subject = random.choice(clause_para[1])
            eng_slave_predicate = clause_para[2]
            # randomly choose an object in the 'object_refined' list
            eng_object = random.choice(clause_para[3])
            eng_master_predicate = clause_para[4]
            eng = eng_prefix + ' ' \
                  + eng_subject + ' ' + eng_slave_predicate + ' ' + eng_object + ' ' \
                  + eng_master_predicate

        return eng
