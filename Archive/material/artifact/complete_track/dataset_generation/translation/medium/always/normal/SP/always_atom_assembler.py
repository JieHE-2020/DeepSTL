from translation.level_1.atom.atom_assembler import AtomAssembler
import copy


class AlwaysAtomAssembler(AtomAssembler):

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
        For 'always' temporal operator:
        1. for positive clause, adverbs can be added to both the beginning or the end of the clause;
           it is the same with adverbial phrases except 'all the time', which can be only added to the 
           end of the clause
        2. for negative clause, only adverbs are added to the beginning of the clause; adverbial phrases 
           can not be added 
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
                eng_update = eng + ' ' + phrase
                eng_list_adverbialAdded.append(eng_update)

                if phrase != 'all the time':   # do not add 'all the time' in the front of the clause
                    eng = self.random_select(clause_para, clause_type)
                    eng_update = phrase + ' ' + eng
                    eng_list_adverbialAdded.append(eng_update)

        else:  # mood == 'negative':
            for word in self.adverbial_para[0]:
                eng = self.random_select(clause_para, clause_type)
                eng_update = word + ' ' + eng
                eng_list_adverbialAdded.append(eng_update)

            for phrase in self.adverbial_para[1]:
                if phrase != 'all the time':  # do not add 'all the time' in the front of the clause
                    eng = self.random_select(clause_para, clause_type)
                    eng_update = phrase + ' ' + eng
                    eng_list_adverbialAdded.append(eng_update)

        return eng_list_adverbialAdded
