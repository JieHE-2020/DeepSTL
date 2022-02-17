from corpus import basic_words
import copy


class PredicateRefiner:
    def __init__(self):
        self.predicate_refined = list()

    def predicate_process(self, predicate_template, mood, commands_selected):
        """
        Function:
        Input:
        1. predicate_template
        This is a list containing raw predicates that have not been refined
        2. mood
        This is a string with only two options: 'positive' and 'negative'.
        If mood = 'positive', the clause is positive and vice versa.
        3. commands_selected
        This is a dictionary structure which contains the refinement commands of the predicate. These commands
        describes: (1) the tense the verb in the predicate can be used; (2) the modal verbs that can be used;
        (3) information about how adverbs are added in (1) and (2) if they are supported.

        Output: predicate_refined
        This is a list containing all the predicates that have been refined, e.g., change of tense, modal verb addition,
        adverb modification.
        For each of the predicate in "predicate_template", e.g. 'be set to', there is a specific list in
        "predicate_refined" to store its various refined variations.

        e.g.
        Input:
        predicate_template = ['be', 'be equal to', 'be set to', 'equal to']
        Output:
        -- Assume the tense considered is only present tense of Third Person Singular (TPS)
        -- Assume the adverbs that can be added are only 'eventually' and 'finally'
        predicate_refined = [ ['is', 'is eventually', 'is finally'],
                              ['is equal to', 'is eventually equal to', 'is finally equal to'],
                              ['is set to', 'is eventually set to', 'is finally set to'],
                              ['equals to', 'eventually equals to', 'finally equals to']
                            ]
        """
        self.predicate_refined = []
        predicate_template.reverse()

        while len(predicate_template) != 0:
            # change string to list
            # for the convenient of operation in function "predicate_refine_positive" and "predicate_refine_negative"
            # 1. pop 'be' -> raw_list = ['be']
            # 2. pop 'be equal to' -> raw_list = ['be', 'equal', 'to']
            # 3. pop 'be set to' -> raw_list = ['be', 'set', 'to']
            # 4. pop 'equal to' -> raw_list = ['equal', 'to']
            raw_list = predicate_template.pop().split(' ')
            total_commands = copy.deepcopy(commands_selected)

            if mood == 'positive':
                refined_list = self.predicate_refine_positive(raw_list, total_commands)
            else:  # mood == 'negative'
                refined_list = self.predicate_refine_negative(raw_list, total_commands)

            self.predicate_refined.append(refined_list)

        return self.predicate_refined

    def predicate_refine_positive(self, raw_list, total_commands):
        """
        e.g.
        Input:
        raw_list = raw_list = ['be', 'set', 'to']
        total_commands = [{'simple_present': ['singular', adv_dic]},
                          {'simple_future': ['will', adv_dic]},
                          {'modal': ['should', adv_dic]}]
        adv_dic = {'adverb': ['eventually', 'finally']}

        Output:
        refined_list = ['is set to', 'is eventually set to, is finally set to',
                        'will be set to', 'will be eventually set to', 'will be finally set to',
                        'should be set to, should be eventually set to, should be finally set to']
        """

        refined_list = []
        total_commands.reverse()

        # In the following, pay attention to the meaning of command_dic, command_dic_value and command
        while len(total_commands) != 0:  # process all the command types in the total_commands list
            command_dic = total_commands.pop()
            # pop out a single type of commands which is stored in a dictionary
            # In the first time, command_dic = {'simple_present': ['singular', adv_refined]}
            # In the second time, command_dic = {'simple_future': ['will', adv_refined]}
            # .......

            if 'simple_present' in command_dic:  # if the type is 'simple_present'
                command_dic['simple_present'].reverse()
                # command_dic_value = [adv_dic, 'singular'] since command_dic['present'] has been reversed
                command_dic_value = command_dic['simple_present']

                # prepare strings
                v_changed = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    command = command_dic_value.pop()
                    # In the first time, command = 'singular', which is a string
                    # in the second time, command = adv_dic, which is a dictionary

                    if command == 'singular':
                        v_code = 'TPS'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_changed)
                        new_str = ' '.join(raw_list_copy)  # change list to string
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_positive(raw_list, new_str, v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'simple_past' in command_dic:  # if the type is 'simple_past'
                command_dic['simple_past'].reverse()
                command_dic_value = command_dic['simple_past']

                # prepare strings
                v_changed = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    command = command_dic_value.pop()

                    if command == 'singular':
                        v_code = 'PT'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_changed)
                        new_str = ' '.join(raw_list_copy)  # change list to string
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_positive(raw_list, new_str, v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'simple_future' in command_dic:  # if the type is 'simple_future'
                command_dic['simple_future'].reverse()
                command_dic_value = command_dic['simple_future']
                # prepare strings
                v_changed = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    command = command_dic_value.pop()
                    if command == 'will':
                        v_code = 'OTPP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)
                        v_replaced = 'will ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_positive(raw_list, new_str, v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'past_future' in command_dic:  # if the type is 'past_future'
                command_dic['past_future'].reverse()
                command_dic_value = command_dic['past_future']
                # prepare strings
                v_changed = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    command = command_dic_value.pop()
                    if command == 'would':
                        v_code = 'OTPP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)
                        v_replaced = 'would ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_positive(raw_list, new_str, v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'future_progressive' in command_dic:  # if the type is 'future_progressive'
                # if raw_list[0] == 'be':
                #     point = random.randint(1, 100)
                #     if point <= 80:
                #         continue
                command_dic['future_progressive'].reverse()
                command_dic_value = command_dic['future_progressive']
                # prepare strings
                v_changed = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    command = command_dic_value.pop()
                    if command == 'will_be':
                        v_code = 'PresP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)
                        v_replaced = 'will be ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_positive(raw_list, new_str, v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'past_future_progressive' in command_dic:  # if the type is 'past_future_progressive'
                # if raw_list[0] == 'be':
                #     point = random.randint(1, 100)
                #     if point <= 80:
                #         continue
                command_dic['past_future_progressive'].reverse()
                command_dic_value = command_dic['past_future_progressive']
                # prepare strings
                v_changed = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    command = command_dic_value.pop()
                    if command == 'would_be':
                        v_code = 'PresP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)
                        v_replaced = 'would be ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_positive(raw_list, new_str, v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'present_perfect' in command_dic:  # if the type is 'present_perfect'
                command_dic['present_perfect'].reverse()
                command_dic_value = command_dic['present_perfect']
                # prepare strings
                v_changed = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    command = command_dic_value.pop()
                    if command == 'singular':
                        v_code = 'PastP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)
                        v_replaced = 'has ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_positive(raw_list, new_str, v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'past_perfect' in command_dic:  # if the type is 'past_perfect'
                command_dic['past_perfect'].reverse()
                command_dic_value = command_dic['past_perfect']
                # prepare strings
                v_changed = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    command = command_dic_value.pop()
                    if command == 'had':
                        v_code = 'PastP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)
                        v_replaced = 'had ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_positive(raw_list, new_str, v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'future_perfect' in command_dic:  # if the type is 'future_perfect'
                command_dic['future_perfect'].reverse()
                command_dic_value = command_dic['future_perfect']
                # prepare strings
                v_changed = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    command = command_dic_value.pop()
                    if command == 'will_have_done':
                        v_code = 'PastP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)
                        v_replaced = 'will have ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_positive(raw_list, new_str, v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'past_future_perfect' in command_dic:  # if the type is 'past_future_perfect'
                command_dic['past_future_perfect'].reverse()
                command_dic_value = command_dic['past_future_perfect']
                # prepare strings
                v_changed = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    command = command_dic_value.pop()
                    if command == 'would_have_done':
                        v_code = 'PastP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)
                        v_replaced = 'would have ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_positive(raw_list, new_str, v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'present_perfect_continuous' in command_dic:  # if the type is 'present_perfect_continuous'
                # if raw_list[0] == 'be':
                #     point = random.randint(1, 100)
                #     if point <= 80:
                #         continue
                command_dic['present_perfect_continuous'].reverse()
                command_dic_value = command_dic['present_perfect_continuous']
                # prepare strings
                v_changed = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    command = command_dic_value.pop()
                    if command == 'singular':
                        v_code = 'PresP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)
                        v_replaced = 'has been ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_positive(raw_list, new_str, v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'past_perfect_continuous' in command_dic:  # if the type is 'past_perfect_continuous'
                # if raw_list[0] == 'be':
                #     point = random.randint(1, 100)
                #     if point <= 80:
                #         continue
                command_dic['past_perfect_continuous'].reverse()
                command_dic_value = command_dic['past_perfect_continuous']
                # prepare strings
                v_changed = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    command = command_dic_value.pop()
                    if command == 'had_been_doing':
                        v_code = 'PresP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)
                        v_replaced = 'had been ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_positive(raw_list, new_str, v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'future_perfect_continuous' in command_dic:  # if the type is 'future_perfect_continuous'
                # if raw_list[0] == 'be':
                #     point = random.randint(1, 100)
                #     if point <= 80:
                #         continue
                command_dic['future_perfect_continuous'].reverse()
                command_dic_value = command_dic['future_perfect_continuous']
                # prepare strings
                v_changed = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    command = command_dic_value.pop()
                    if command == 'will_have_been_doing':
                        v_code = 'PresP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)
                        v_replaced = 'will have been ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_positive(raw_list, new_str, v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'past_future_perfect_continuous' in command_dic:  # if the type is 'past_future_perfect_continuous'
                # if raw_list[0] == 'be':
                #     point = random.randint(1, 100)
                #     if point <= 80:
                #         continue
                command_dic['past_future_perfect_continuous'].reverse()
                command_dic_value = command_dic['past_future_perfect_continuous']
                # prepare strings
                v_changed = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    command = command_dic_value.pop()
                    if command == 'would_have_been_doing':
                        v_code = 'PresP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)
                        v_replaced = 'would have been ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_positive(raw_list, new_str, v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'modal' in command_dic:  # if the type is 'modal'
                command_dic['modal'].reverse()
                command_dic_value = command_dic['modal']
                # prepare strings
                v_changed = ''
                v_replaced = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    command = command_dic_value.pop()

                    if 'adverb' not in command:
                        v_code = 'OTPP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)
                        if command == 'should' or command == 'must' or command == 'shall':
                            v_replaced = command + ' ' + v_changed
                        if command == 'ought_to':
                            v_replaced = 'ought to' + ' ' + v_changed
                        if command == 'present_singular_have_to':
                            v_replaced = 'has to' + ' ' + v_changed
                        if command == 'future_have_to':
                            v_replaced = 'will have to' + ' ' + v_changed
                        if command == 'present_singular_need_to':
                            v_replaced = 'needs to' + ' ' + v_changed
                        if command == 'past_have_to':
                            v_replaced = 'had to' + ' ' + v_changed
                        if command == 'past_future_have_to':
                            v_replaced = 'would have to' + ' ' + v_changed
                        if command == 'past_need_to':
                            v_replaced = 'needed to' + ' ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_positive(raw_list, new_str, v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

        return refined_list

    def predicate_refine_negative(self, raw_list, total_commands):
        refined_list = []
        total_commands.reverse()

        while len(total_commands) != 0:  # process all the command types in the total_commands list
            command_dic = total_commands.pop()  # pop out a singular type of commands which is stored in a dictionary

            if 'simple_present' in command_dic:  # if the type is 'simple_present'
                command_dic['simple_present'].reverse()
                command_dic_value = command_dic['simple_present']
                # prepare strings
                command = ''
                v_replaced = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    last_command = command
                    command = command_dic_value.pop()

                    if 'adverb' not in command:
                        v_extracted = raw_list[0]

                        if command == 'singular_not_without_abbreviation':
                            if v_extracted == 'be':
                                v_code = 'TPS'
                                v_changed = self.replace_verb(v_extracted, v_code)
                                v_replaced = v_changed + ' ' + 'not'
                            else:
                                v_code = 'OTPP'
                                v_changed = self.replace_verb(v_extracted, v_code)
                                v_replaced = 'does not' + ' ' + v_changed

                        if command == 'singular_not_with_abbreviation':
                            if v_extracted == 'be':
                                v_replaced = "isn't"
                            else:
                                v_code = 'OTPP'
                                v_changed = self.replace_verb(v_extracted, v_code)
                                v_replaced = "doesn't" + ' ' + v_changed

                        if command == 'singular_never':
                            v_code = 'TPS'
                            v_changed = self.replace_verb(v_extracted, v_code)
                            if v_extracted == 'be':
                                v_replaced = v_changed + ' ' + 'never'
                            else:
                                v_replaced = 'never' + ' ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_negative(new_str, last_command, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'simple_past' in command_dic:  # if the type is 'simple_past'
                command_dic['simple_past'].reverse()
                command_dic_value = command_dic['simple_past']
                # prepare strings
                command = ''
                v_replaced = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    last_command = command
                    command = command_dic_value.pop()

                    if 'adverb' not in command:
                        v_extracted = raw_list[0]

                        if command == 'singular_not_without_abbreviation':
                            if v_extracted == 'be':
                                v_code = 'PT'
                                v_changed = self.replace_verb(v_extracted, v_code)
                                v_replaced = v_changed + ' ' + 'not'
                            else:
                                v_code = 'OTPP'
                                v_changed = self.replace_verb(v_extracted, v_code)
                                v_replaced = 'did not' + ' ' + v_changed

                        if command == 'singular_not_with_abbreviation':
                            if v_extracted == 'be':
                                v_replaced = "wasn't"
                            else:
                                v_code = 'OTPP'
                                v_changed = self.replace_verb(v_extracted, v_code)
                                v_replaced = "didn't" + ' ' + v_changed

                        if command == 'singular_never':
                            v_code = 'PT'
                            v_changed = self.replace_verb(v_extracted, v_code)
                            if v_extracted == 'be':
                                v_replaced = v_changed + ' ' + 'never'
                            else:
                                v_replaced = 'never' + ' ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_negative(new_str, last_command, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'simple_future' in command_dic:  # if the type is 'simple_future'
                command_dic['simple_future'].reverse()
                command_dic_value = command_dic['simple_future']
                # prepare strings
                command = ''
                v_replaced = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    last_command = command
                    command = command_dic_value.pop()

                    if 'adverb' not in command:
                        v_code = 'OTPP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)

                        if command == 'will_not_without_abbreviation':
                            v_replaced = 'will not' + ' ' + v_changed
                        if command == 'will_not_with_abbreviation':
                            v_replaced = "won't" + ' ' + v_changed
                        if command == 'will_never':
                            v_replaced = 'will never' + ' ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_negative(new_str, last_command, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'past_future' in command_dic:  # if the type is 'past_future'
                command_dic['past_future'].reverse()
                command_dic_value = command_dic['past_future']
                # prepare strings
                command = ''
                v_replaced = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    last_command = command
                    command = command_dic_value.pop()

                    if 'adverb' not in command:
                        v_code = 'OTPP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)

                        if command == 'would_not_without_abbreviation':
                            v_replaced = 'would not' + ' ' + v_changed
                        if command == 'would_not_with_abbreviation':
                            v_replaced = "wouldn't" + ' ' + v_changed
                        if command == 'would_never':
                            v_replaced = 'would never' + ' ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_negative(new_str, last_command, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'present_perfect' in command_dic:  # if the type is 'present_perfect'
                command_dic['present_perfect'].reverse()
                command_dic_value = command_dic['present_perfect']
                # prepare strings
                command = ''
                v_replaced = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    last_command = command
                    command = command_dic_value.pop()

                    if 'adverb' not in command:
                        v_code = 'PastP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)

                        if command == 'singular_not_without_abbreviation':
                            v_replaced = 'has not' + ' ' + v_changed
                        if command == 'singular_not_with_abbreviation':
                            v_replaced = "hasn't" + ' ' + v_changed
                        if command == 'singular_never':
                            v_replaced = 'has never' + ' ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_negative(new_str, last_command, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'past_perfect' in command_dic:  # if the type is 'past_perfect'
                command_dic['past_perfect'].reverse()
                command_dic_value = command_dic['past_perfect']
                # prepare strings
                command = ''
                v_replaced = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    last_command = command
                    command = command_dic_value.pop()

                    if 'adverb' not in command:
                        v_code = 'PastP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)

                        if command == 'had_not_without_abbreviation':
                            v_replaced = 'had not' + ' ' + v_changed
                        if command == 'had_not_with_abbreviation':
                            v_replaced = "hadn't" + ' ' + v_changed
                        if command == 'had_never':
                            v_replaced = 'had never' + ' ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_negative(new_str, last_command, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'future_perfect' in command_dic:  # if the type is 'future_perfect'
                command_dic['future_perfect'].reverse()
                command_dic_value = command_dic['future_perfect']
                # prepare strings
                command = ''
                v_replaced = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    last_command = command
                    command = command_dic_value.pop()

                    if 'adverb' not in command:
                        v_code = 'PastP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)

                        if command == 'will_not_have_without_abbreviation':
                            v_replaced = 'will not have' + ' ' + v_changed
                        if command == 'will_not_have_with_abbreviation':
                            v_replaced = "won't have" + ' ' + v_changed
                        if command == 'will_never_have':
                            v_replaced = 'will never have' + ' ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_negative(new_str, last_command, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'past_future_perfect' in command_dic:  # if the type is 'past_future_perfect'
                command_dic['past_future_perfect'].reverse()
                command_dic_value = command_dic['past_future_perfect']
                # prepare strings
                command = ''
                v_replaced = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    last_command = command
                    command = command_dic_value.pop()

                    if 'adverb' not in command:
                        v_code = 'PastP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)

                        if command == 'would_not_have_without_abbreviation':
                            v_replaced = 'would not have' + ' ' + v_changed
                        if command == 'would_not_have_with_abbreviation':
                            v_replaced = "wouldn't have" + ' ' + v_changed
                        if command == 'would_never_have':
                            v_replaced = 'would never have' + ' ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_negative(new_str, last_command, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'modal' in command_dic:  # if the type is 'modal'
                command_dic['modal'].reverse()
                command_dic_value = command_dic['modal']
                # prepare strings
                command = ''
                v_replaced = ''
                new_str = ''
                while len(command_dic_value) != 0:
                    last_command = command
                    command = command_dic_value.pop()

                    if 'adverb' not in command:
                        v_code = 'OTPP'
                        v_extracted = raw_list[0]
                        v_changed = self.replace_verb(v_extracted, v_code)

                        if command == 'should_not_without_abbreviation':
                            v_replaced = 'should not' + ' ' + v_changed
                        if command == 'should_not_with_abbreviation':
                            v_replaced = "shouldn't" + ' ' + v_changed
                        if command == 'should_never':
                            v_replaced = 'should never' + ' ' + v_changed
                        if command == 'ought_not_to_without_abbreviation':
                            v_replaced = 'ought not to' + ' ' + v_changed
                        if command == 'ought_not_to_with_abbreviation':
                            v_replaced = "oughtn't to" + ' ' + v_changed
                        if command == 'ought_never_to':
                            v_replaced = 'ought never to' + ' ' + v_changed
                        if command == 'must_not_without_abbreviation':
                            v_replaced = 'must not' + ' ' + v_changed
                        if command == 'must_not_with_abbreviation':
                            v_replaced = "mustn't" + ' ' + v_changed
                        if command == 'must_never':
                            v_replaced = 'must never' + ' ' + v_changed
                        if command == 'shall_not_without_abbreviation':
                            v_replaced = 'shall not' + ' ' + v_changed
                        if command == 'shall_not_with_abbreviation':
                            v_replaced = "shan't" + ' ' + v_changed
                        if command == 'shall_never':
                            v_replaced = 'shall never' + ' ' + v_changed

                        raw_list_copy = copy.deepcopy(raw_list)
                        del raw_list_copy[0]
                        raw_list_copy.insert(0, v_replaced)
                        new_str = ' '.join(raw_list_copy)
                        refined_list.append(new_str)

                    if 'adverb' in command:
                        command_copy = copy.deepcopy(command)
                        adverb_modified_list = self.adverb_modifier_negative(new_str, last_command, command_copy)
                        refined_list = refined_list + adverb_modified_list

        return refined_list

    @staticmethod
    def adverb_modifier_positive(raw_list, new_str, v_changed, command):
        """
        adverb addition rules:
        1. For verb belonging to 'be' like is, are, was, were..., put the adverb behind it.
        2. For notional verbs, put the adverb in front of it
        """
        adverb_modified_list = []

        v_extracted = raw_list[0]
        command['adverb'].reverse()
        adv_list = command['adverb']

        while len(adv_list) != 0:
            adv = adv_list.pop()
            string_list = new_str.split(' ')  # string -> list
            key_index = string_list.index(v_changed)
            if v_extracted == 'be':
                string_list.insert(key_index + 1, adv)
            else:
                string_list.insert(key_index, adv)
            string_modified = ' '.join(string_list)  # list -> string
            adverb_modified_list.append(string_modified)

        return adverb_modified_list

    @staticmethod
    def adverb_modifier_negative(new_str, last_command, command):
        """
        adverb addition rules:
        Only supported for negative negative clauses without the appearance of abbreviation like isn't, doesn't...
        1. put the adverb in front of 'not' if there is no appearance of 'does not' or 'do not' or 'did not' originally
        """
        adverb_modified_list = []

        if 'without_abbreviation' in last_command:
            command['adverb'].reverse()
            adv_list = command['adverb']
            while len(adv_list) != 0:
                adv = adv_list.pop()
                string_list = new_str.split(' ')  # string -> list
                key_index = string_list.index('not')
                if string_list[key_index - 1] != 'does' and string_list[key_index - 1] != 'do' and \
                        string_list[key_index - 1] != 'did':
                    string_list.insert(key_index, adv)
                    string_modified = ' '.join(string_list)  # list -> string
                    adverb_modified_list.append(string_modified)

        return adverb_modified_list

    @staticmethod
    def replace_verb(verb_extracted, v_code, extra_info=''):
        """
        Format of verb:
        1. OTPP - Original & Third Person Plural (Present Tense)
        2. TPS - Third Person Singular (Present Tense)
        3. PT - Past Tense
        4. PresP - Present Participle
        5. PastP - Past Participle

        The default value of the third parameter, 'extra_info', is an empty string.
        -- Only when the subject is plural, this parameter will be stuffed with string 'plural'.
        -- Otherwise, when this function is called, this parameter should not be specified.
        -- The function of parameter 'extra_info' is used as a auxiliary guide to process verb 'be'
           which is different from other notional verbs.
        """
        v_changed = str()

        if verb_extracted == 'be':
            if v_code == 'OTPP' and extra_info != 'plural':
                v_changed = basic_words.verb_bank['be_singular'][0]  # v_changed = 'be'
            if v_code == 'OTPP' and extra_info == 'plural':
                v_changed = basic_words.verb_bank['be_plural'][1]  # v_changed = 'are'
            if v_code == 'TPS':
                v_changed = basic_words.verb_bank['be_singular'][1]  # v_changed = 'is'
            if v_code == 'PT' and extra_info != 'plural':
                v_changed = basic_words.verb_bank['be_singular'][2]  # v_changed = 'was'
            if v_code == 'PT' and extra_info == 'plural':
                v_changed = basic_words.verb_bank['be_plural'][2]  # v_changed = 'were'
            if v_code == 'PresP':
                v_changed = basic_words.verb_bank['be_singular'][3]  # v_changed = 'being'
            if v_code == 'PastP':
                v_changed = basic_words.verb_bank['be_singular'][4]  # v_changed = 'been'

        if verb_extracted != 'be':
            if v_code == 'OTPP' and extra_info != 'plural':
                v_changed = basic_words.verb_bank[verb_extracted][0]
            if v_code == 'OTPP' and extra_info == 'plural':
                v_changed = basic_words.verb_bank[verb_extracted][0]
            if v_code == 'TPS':
                v_changed = basic_words.verb_bank[verb_extracted][1]
            if v_code == 'PT' and extra_info != 'plural':
                v_changed = basic_words.verb_bank[verb_extracted][2]
            if v_code == 'PT' and extra_info == 'plural':
                v_changed = basic_words.verb_bank[verb_extracted][2]
            if v_code == 'PresP':
                v_changed = basic_words.verb_bank[verb_extracted][3]
            if v_code == 'PastP':
                v_changed = basic_words.verb_bank[verb_extracted][4]

        return v_changed
