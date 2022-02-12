from translation.level_1.atom.atom_assembler import AtomAssembler


class EventuallyAtomAssembler(AtomAssembler):

    # override function 'random_adverbial_augment' in class AtomAssembler
    def random_adverbial_augment(self, clause_para, string_para):
        # extract variables from function parameters
        mood = string_para[0]
        clause_type = string_para[1]
        eng_list_adverbialAdded = []

        """
        The position of adverbs and adverbial phrases are considered as follows:
        For 'eventually' temporal operator:
        1. adverbs and adverbial phrases can be added to both the beginning or 
           the end of the clause no matter whether the clause is positive or negative
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

        return eng_list_adverbialAdded
