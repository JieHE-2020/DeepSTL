from translation.level_2.TP_atom.original_TP_atom.always.simplest.simplest_always_atom_preprocessor \
    import SimplestAlwaysAtomPreprocessor


class SimplestUntilAtomAlwaysPreprocessor(SimplestAlwaysAtomPreprocessor):
    """
    functions:
    1. process main sentences of type 1:
       refine the templates of Atom expressions and assemble them into English translations
    """

    def temporal_phrase_process(self):
        blank_results = []

        return blank_results

    def display_key_list(self):
        count = 1
        for eng in self.eng_main_sentence_type1:
            print('%d: %s' % (count, eng))
            count = count + 1
        print('\n')

    def pack_key_list(self):
        return self.eng_main_sentence_type1


