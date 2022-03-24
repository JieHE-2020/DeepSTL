from translation.level_1.atom.predicate_operation.predicate_refiner import PredicateRefiner
import copy


class NotContinuationPredicateRefiner(PredicateRefiner):

    def predicate_refine_negative(self, raw_list, total_commands):
        refined_list = []
        total_commands.reverse()

        while len(total_commands) != 0:  # process all the command types in the total_commands list
            command_dic = total_commands.pop()  # pop out a singular type of commands which is stored in a dictionary

            if 'simple_present' in command_dic:  # if the type is 'simple_present'
                command_dic['simple_present'].reverse()
                command_dic_value = command_dic['simple_present']
                # prepare strings
                key_name = 'simple_present'
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
                        adverb_modified_list = self.adverb_modifier_negative_type1(raw_list, new_str,
                                                                                   key_name, last_command, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'simple_past' in command_dic:  # if the type is 'simple_past'
                command_dic['simple_past'].reverse()
                command_dic_value = command_dic['simple_past']
                # prepare strings
                key_name = 'simple_past'
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
                        adverb_modified_list = self.adverb_modifier_negative_type1(raw_list, new_str,
                                                                                   key_name, last_command, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'simple_future' in command_dic:  # if the type is 'simple_future'
                command_dic['simple_future'].reverse()
                command_dic_value = command_dic['simple_future']
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
                        adverb_modified_list = self.adverb_modifier_negative_type2(raw_list, new_str,
                                                                                   v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'past_future' in command_dic:  # if the type is 'past_future'
                command_dic['past_future'].reverse()
                command_dic_value = command_dic['past_future']
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
                        adverb_modified_list = self.adverb_modifier_negative_type2(raw_list, new_str,
                                                                                   v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'present_perfect' in command_dic:  # if the type is 'present_perfect'
                command_dic['present_perfect'].reverse()
                command_dic_value = command_dic['present_perfect']
                # prepare strings
                v_changed = ''
                v_replaced = ''
                new_str = ''
                while len(command_dic_value) != 0:
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
                        adverb_modified_list = self.adverb_modifier_negative_type2(raw_list, new_str,
                                                                                   v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'past_perfect' in command_dic:  # if the type is 'past_perfect'
                command_dic['past_perfect'].reverse()
                command_dic_value = command_dic['past_perfect']
                # prepare strings
                v_changed = ''
                v_replaced = ''
                new_str = ''
                while len(command_dic_value) != 0:
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
                        adverb_modified_list = self.adverb_modifier_negative_type2(raw_list, new_str,
                                                                                   v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'future_perfect' in command_dic:  # if the type is 'future_perfect'
                command_dic['future_perfect'].reverse()
                command_dic_value = command_dic['future_perfect']
                # prepare strings
                v_changed = ''
                v_replaced = ''
                new_str = ''
                while len(command_dic_value) != 0:
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
                        adverb_modified_list = self.adverb_modifier_negative_type2(raw_list, new_str,
                                                                                   v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

            if 'past_future_perfect' in command_dic:  # if the type is 'past_future_perfect'
                command_dic['past_future_perfect'].reverse()
                command_dic_value = command_dic['past_future_perfect']
                # prepare strings
                v_changed = ''
                v_replaced = ''
                new_str = ''
                while len(command_dic_value) != 0:
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
                        adverb_modified_list = self.adverb_modifier_negative_type2(raw_list, new_str,
                                                                                   v_changed, command_copy)
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
                        adverb_modified_list = self.adverb_modifier_negative_type2(raw_list, new_str,
                                                                                   v_changed, command_copy)
                        refined_list = refined_list + adverb_modified_list

        return refined_list

    @staticmethod
    def adverb_modifier_negative_type1(raw_list, new_str, key_name, last_command, command):
        """
        This function is used when command == 'simple_present' or command == 'simple_past'
        adverb addition rules:
        1. If last_command includes 'without_abbreviation', put the adverb behind 'not';
        2. If last_command == 'singular_not_with_abbreviation', put the adverb behind the abbreviated word;
        3. If last_command includes 'never', put the adverb behind 'never';
        """
        adverb_modified_list = []

        v_extracted = raw_list[0]
        command['adverb'].reverse()
        adv_list = command['adverb']

        while len(adv_list) != 0:
            adv = adv_list.pop()
            string_list = new_str.split(' ')  # string -> list

            if 'without_abbreviation' in last_command:
                key_index = string_list.index('not')
                string_list.insert(key_index + 1, adv)

            if last_command == 'singular_not_with_abbreviation':
                if key_name == 'simple_present':
                    if v_extracted == 'be':
                        key_index = string_list.index("isn't")
                        string_list.insert(key_index + 1, adv)
                    else:
                        key_index = string_list.index("doesn't")
                        string_list.insert(key_index + 1, adv)
                if key_name == 'simple_past':
                    if v_extracted == 'be':
                        key_index = string_list.index("wasn't")
                        string_list.insert(key_index + 1, adv)
                    else:
                        key_index = string_list.index("didn't")
                        string_list.insert(key_index + 1, adv)

            if 'never' in last_command:
                key_index = string_list.index('never')
                string_list.insert(key_index + 1, adv)

            string_modified = ' '.join(string_list)  # list -> string
            adverb_modified_list.append(string_modified)

        return adverb_modified_list

    @staticmethod
    def adverb_modifier_negative_type2(raw_list, new_str, v_changed, command):
        """
        adverb addition rules:
        1. For verb belonging to 'be' like is, are, was, were..., put the adverb behind v_changed;
        2. For other verbs, put the adverb in front of v_changed.
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
