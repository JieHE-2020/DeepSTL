from translation.level_1.atom.atom_assembler import AtomAssembler
import copy
import random
import math


class NotContinuationAtomAssembler(AtomAssembler):

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
                        #################################################################################
                        # Note:
                        # has to pop out the last assembled translation that has no adverbial modifiers
                        # because the negation is on the adverbial modifiers but not on the predicate!
                        self.eng_list.pop()
                        #################################################################################
                        # prepare and assemble the parameters for the downstream function
                        string_para = [mood, clause_type]
                        eng_list_adverbialAdded = self.random_adverbial_augment(clause_para, string_para)
                        # if anomaly is detected but it has not been dropped, the translations added by
                        # adverbial modifiers should be cut down to a limited number
                        if abnormal_result:
                            eng_list_adverbialAdded = random.sample(eng_list_adverbialAdded,
                                                                    math.ceil(len(eng_list_adverbialAdded) / 5))
                        self.eng_list = self.eng_list + eng_list_adverbialAdded

    # override function 'check_adverb_existence' in class AtomAssembler
    def check_adverb_existence(self, predicate):
        adverb_list_checked = copy.deepcopy(self.adverbial_para[0])
        adverb_list_checked.append('always')

        flag = 0
        for scanned_word in adverb_list_checked:
            if scanned_word in predicate:
                flag = 1

        return flag

    # override function 'random_adverbial_augment' in class AtomAssembler
    def random_adverbial_augment(self, clause_para, string_para):
        # extract variables from function parameters
        mood = string_para[0]
        clause_type = string_para[1]
        eng_list_adverbialAdded = []

        """
        The position of adverbs and adverbial phrases are considered as follows:
        For 'always' and 'historically' temporal operator, the mood of the clause has been deliberately 
        set to 'negative'. In order to negate continuation: 
        Adverbs and adverbial phrases are only added to the end of the clause. 
        """

        if mood == 'negative':
            for word in self.adverbial_para[0]:
                eng = self.random_select(clause_para, clause_type)
                eng_update = eng + ' ' + word
                eng_list_adverbialAdded.append(eng_update)

            for phrase in self.adverbial_para[1]:
                eng = self.random_select(clause_para, clause_type)
                eng_update = eng + ' ' + phrase
                eng_list_adverbialAdded.append(eng_update)

        return eng_list_adverbialAdded
