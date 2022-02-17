# layer 1 - original TP
from translation.level_2.TP_atom.original_TP_atom.eventually.normal.eventually_atom_handler \
    import EventuallyAtomHandler
from translation.level_2.TP_atom.original_TP_atom.always.normal.always_atom_handler \
    import AlwaysAtomHandler
from translation.level_2.TP_atom.original_TP_atom.once.normal.once_atom_handler \
    import OnceAtomHandler
from translation.level_2.TP_atom.original_TP_atom.historically.normal.historically_atom_handler \
    import HistoricallyAtomHandler
from translation.level_2.TP_atom.original_TP_atom.until.normal.until_atom_handler \
    import UntilAtomHandler
from translation.level_2.TP_atom.original_TP_atom.since.normal.since_atom_handler \
    import SinceAtomHandler

# layer 2 - not TP
from translation.level_2.TP_atom.not_TP_atom.not_eventually.not_eventually_atom_handler \
    import NotEventuallyAtomHandler
from translation.level_2.TP_atom.not_TP_atom.not_always.not_always_atom_handler \
    import NotAlwaysAtomHandler
from translation.level_2.TP_atom.not_TP_atom.not_once.not_once_atom_handler \
    import NotOnceAtomHandler
from translation.level_2.TP_atom.not_TP_atom.not_historically.not_historically_atom_handler \
    import NotHistoricallyAtomHandler
from translation.level_2.TP_atom.not_TP_atom.not_until.not_until_atom_handler \
    import NotUntilAtomHandler
from translation.level_2.TP_atom.not_TP_atom.not_since.not_since_atom_handler \
    import NotSinceAtomHandler

# layer 3 - rise TP
from translation.level_2.TP_atom.rise_TP_atom.rise_eventually.rise_eventually_atom_handler \
    import RiseEventuallyAtomHandler
from translation.level_2.TP_atom.rise_TP_atom.rise_always.rise_always_atom_handler \
    import RiseAlwaysAtomHandler
from translation.level_2.TP_atom.rise_TP_atom.rise_once.rise_once_atom_handler \
    import RiseOnceAtomHandler
from translation.level_2.TP_atom.rise_TP_atom.rise_historically.rise_historically_atom_handler \
    import RiseHistoricallyAtomHandler
from translation.level_2.TP_atom.rise_TP_atom.rise_until.rise_until_atom_handler \
    import RiseUntilAtomHandler
from translation.level_2.TP_atom.rise_TP_atom.rise_since.rise_since_atom_handler \
    import RiseSinceAtomHandler

# layer 4 - fall TP
from translation.level_2.TP_atom.fall_TP_atom.fall_eventually.fall_eventually_atom_handler \
    import FallEventuallyAtomHandler
from translation.level_2.TP_atom.fall_TP_atom.fall_always.fall_always_atom_handler \
    import FallAlwaysAtomHandler
from translation.level_2.TP_atom.fall_TP_atom.fall_once.fall_once_atom_handler \
    import FallOnceAtomHandler
from translation.level_2.TP_atom.fall_TP_atom.fall_historically.fall_historically_atom_handler \
    import FallHistoricallyAtomHandler
from translation.level_2.TP_atom.fall_TP_atom.fall_until.fall_until_atom_handler \
    import FallUntilAtomHandler
from translation.level_2.TP_atom.fall_TP_atom.fall_since.fall_since_atom_handler \
    import FallSinceAtomHandler

# layer 5 - not rise TP
from translation.level_2.TP_atom.not_rise_TP_atom.not_rise_eventually.not_rise_eventually_atom_handler \
    import NotRiseEventuallyAtomHandler
from translation.level_2.TP_atom.not_rise_TP_atom.not_rise_always.not_rise_always_atom_handler \
    import NotRiseAlwaysAtomHandler
from translation.level_2.TP_atom.not_rise_TP_atom.not_rise_once.not_rise_once_atom_handler \
    import NotRiseOnceAtomHandler
from translation.level_2.TP_atom.not_rise_TP_atom.not_rise_historically.not_rise_historically_atom_handler \
    import NotRiseHistoricallyAtomHandler
from translation.level_2.TP_atom.not_rise_TP_atom.not_rise_until.not_rise_until_atom_handler \
    import NotRiseUntilAtomHandler
from translation.level_2.TP_atom.not_rise_TP_atom.not_rise_since.not_rise_since_atom_handler \
    import NotRiseSinceAtomHandler

# layer 6 - not fall TP
from translation.level_2.TP_atom.not_fall_TP_atom.not_fall_eventually.not_fall_eventually_atom_handler \
    import NotFallEventuallyAtomHandler
from translation.level_2.TP_atom.not_fall_TP_atom.not_fall_always.not_fall_always_atom_handler \
    import NotFallAlwaysAtomHandler
from translation.level_2.TP_atom.not_fall_TP_atom.not_fall_once.not_fall_once_atom_handler \
    import NotFallOnceAtomHandler
from translation.level_2.TP_atom.not_fall_TP_atom.not_fall_historically.not_fall_historically_atom_handler \
    import NotFallHistoricallyAtomHandler
from translation.level_2.TP_atom.not_fall_TP_atom.not_fall_until.not_fall_until_atom_handler \
    import NotFallUntilAtomHandler
from translation.level_2.TP_atom.not_fall_TP_atom.not_fall_since.not_fall_since_atom_handler \
    import NotFallSinceAtomHandler

from public import parameters
import random


class TPAtomScheduler:

    def __init__(self, position, nest_info_dict, limit_num):
        self.position = position
        self.nest_info_dict = nest_info_dict
        self.limit_num = limit_num
        # select type of temporal phrase
        self.layer_selected = self.layer_select()

        # start generating temporal phrase and its translations
        self.tp_atom_expression = str()
        self.tp_atom_translation = []
        self.signal_name_list = []
        self.tp_atom_distribute()

    @staticmethod
    def layer_select():
        layer_selected = 0
        prob_tp_layer = parameters.prob_tp_layer
        prob_acc = []
        sum = 0.0

        for i in range(len(prob_tp_layer)):
            sum = sum + prob_tp_layer[i]
            prob_acc.append(sum)

        # select layer
        point = random.random()
        if 0 <= point < prob_acc[0]:
            layer_selected = 0
        else:
            for i in range(len(prob_acc) - 1):
                if prob_acc[i] <= point < prob_acc[i + 1]:
                    layer_selected = i + 1

        layer_selected = layer_selected + 1

        return layer_selected

    def tp_atom_distribute(self):
        if self.layer_selected == 1:
            self.original_tp_atom_process()
        elif self.layer_selected == 2:
            self.not_tp_atom_process()
        elif self.layer_selected == 3:
            self.rise_tp_atom_process()
        elif self.layer_selected == 4:
            self.fall_tp_atom_process()
        elif self.layer_selected == 5:
            self.not_rise_tp_atom_process()
        else:  # self.layer_selected == 6
            self.not_fall_tp_atom_process()

    def operator_select(self):
        point_1 = random.randint(1, 10)
        if self.position == 'before_imply':
            if point_1 <= 8:  # with 80% probability to choose past operators
                temporal_indicated = 'past'
            else:
                temporal_indicated = 'future'
        else:  # self.position == 'after_imply':
            if point_1 <= 8:  # with 80% probability to choose future operators
                temporal_indicated = 'future'
            else:
                temporal_indicated = 'past'

        point_2 = random.randint(1, 3)
        if temporal_indicated == 'past':
            if point_2 == 1:
                operator_selected = 'once'
            elif point_2 == 2:
                operator_selected = 'historically'
            else:
                operator_selected = 'since'
        else:  # temporal_indicated == 'future'
            if point_2 == 1:
                operator_selected = 'eventually'
            elif point_2 == 2:
                operator_selected = 'always'
            else:
                operator_selected = 'until'

        return operator_selected

    def original_tp_atom_process(self):
        operator_selected = self.operator_select()

        if operator_selected == 'eventually':
            eventually_atom_handler = \
                EventuallyAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = eventually_atom_handler.tp_info_dict['expression']
            self.tp_atom_translation = \
                eventually_atom_handler.eventually_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(eventually_atom_handler.tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'always':
            always_atom_handler = \
                AlwaysAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = always_atom_handler.tp_info_dict['expression']
            self.tp_atom_translation = \
                always_atom_handler.always_atom_translator.random_selected_translations
            self.signal_name_list. \
                append(always_atom_handler.tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'once':
            once_atom_handler = \
                OnceAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = once_atom_handler.tp_info_dict['expression']
            self.tp_atom_translation = \
                once_atom_handler.once_atom_translator.random_selected_translations
            self.signal_name_list. \
                append(once_atom_handler.tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'historically':
            historically_atom_handler = \
                HistoricallyAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = historically_atom_handler.tp_info_dict['expression']
            self.tp_atom_translation = \
                historically_atom_handler.historically_atom_translator.random_selected_translations
            self.signal_name_list. \
                append(historically_atom_handler.tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'until':
            until_atom_handler = \
                UntilAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = until_atom_handler.tp_info_dict['until']['expression']
            self.tp_atom_translation = \
                until_atom_handler.until_atom_translator.random_selected_translations
            self.signal_name_list. \
                append(until_atom_handler.tp_info_dict['until']['ingredient'][0]['ingredient'][0])
            self.signal_name_list. \
                append(until_atom_handler.tp_info_dict['until']['ingredient'][1]['ingredient'][0])

        else:  # operator_selected == 'since'
            since_atom_handler = \
                SinceAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = since_atom_handler.tp_info_dict['since']['expression']
            self.tp_atom_translation = \
                since_atom_handler.since_atom_translator.random_selected_translations
            self.signal_name_list. \
                append(since_atom_handler.tp_info_dict['since']['ingredient'][0]['ingredient'][0])
            self.signal_name_list. \
                append(since_atom_handler.tp_info_dict['since']['ingredient'][1]['ingredient'][0])

    def not_tp_atom_process(self):
        operator_selected = self.operator_select()

        if operator_selected == 'eventually':
            not_eventually_atom_handler = \
                NotEventuallyAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = not_eventually_atom_handler.not_eventually_info_dict['expression']
            self.tp_atom_translation = \
                not_eventually_atom_handler.not_eventually_atom_translator.random_shuffled_translations
            self.signal_name_list.\
                append(not_eventually_atom_handler.not_eventually_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'always':
            not_always_atom_handler = \
                NotAlwaysAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = not_always_atom_handler.not_always_info_dict['expression']
            self.tp_atom_translation = \
                not_always_atom_handler.not_always_atom_translator.random_shuffled_translations
            self.signal_name_list.\
                append(not_always_atom_handler.not_always_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'once':
            not_once_atom_handler = \
                NotOnceAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = not_once_atom_handler.not_once_info_dict['expression']
            self.tp_atom_translation = \
                not_once_atom_handler.not_once_atom_translator.random_shuffled_translations
            self.signal_name_list.\
                append(not_once_atom_handler.not_once_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'historically':
            not_historically_atom_handler = \
                NotHistoricallyAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = not_historically_atom_handler.not_historically_info_dict['expression']
            self.tp_atom_translation = \
                not_historically_atom_handler.not_historically_atom_translator.random_shuffled_translations
            self.signal_name_list.\
                append(not_historically_atom_handler.not_historically_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'until':
            not_until_atom_handler = \
                NotUntilAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = not_until_atom_handler.not_tp_info_dict['expression']
            self.tp_atom_translation = \
                not_until_atom_handler.not_until_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(not_until_atom_handler.not_tp_info_dict['ingredient'][0]['ingredient'][0])
            self.signal_name_list.\
                append(not_until_atom_handler.not_tp_info_dict['ingredient'][1]['ingredient'][0])

        else:  # operator_selected == 'since'
            not_since_atom_handler = \
                NotSinceAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = not_since_atom_handler.not_tp_info_dict['expression']
            self.tp_atom_translation = \
                not_since_atom_handler.not_since_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(not_since_atom_handler.not_tp_info_dict['ingredient'][0]['ingredient'][0])
            self.signal_name_list.\
                append(not_since_atom_handler.not_tp_info_dict['ingredient'][1]['ingredient'][0])

    def rise_tp_atom_process(self):
        operator_selected = self.operator_select()

        if operator_selected == 'eventually':
            rise_eventually_atom_handler = \
                RiseEventuallyAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = rise_eventually_atom_handler.rise_tp_info_dict['expression']
            self.tp_atom_translation = \
                rise_eventually_atom_handler.rise_eventually_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(rise_eventually_atom_handler.rise_tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'always':
            rise_always_atom_handler = \
                RiseAlwaysAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = rise_always_atom_handler.rise_tp_info_dict['expression']
            self.tp_atom_translation = \
                rise_always_atom_handler.rise_always_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(rise_always_atom_handler.rise_tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'once':
            rise_once_atom_handler = \
                RiseOnceAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = rise_once_atom_handler.rise_tp_info_dict['expression']
            self.tp_atom_translation = \
                rise_once_atom_handler.rise_once_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(rise_once_atom_handler.rise_tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'historically':
            rise_historically_atom_handler = \
                RiseHistoricallyAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = rise_historically_atom_handler.rise_tp_info_dict['expression']
            self.tp_atom_translation = \
                rise_historically_atom_handler.rise_historically_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(rise_historically_atom_handler.rise_tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'until':
            rise_until_atom_handler = \
                RiseUntilAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = rise_until_atom_handler.rise_tp_info_dict['expression']
            self.tp_atom_translation = \
                rise_until_atom_handler.rise_until_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(rise_until_atom_handler.rise_tp_info_dict['ingredient'][0]['ingredient'][0])
            self.signal_name_list.\
                append(rise_until_atom_handler.rise_tp_info_dict['ingredient'][1]['ingredient'][0])

        else:  # operator_selected == 'since'
            rise_since_atom_handler = \
                RiseSinceAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = rise_since_atom_handler.rise_tp_info_dict['expression']
            self.tp_atom_translation = \
                rise_since_atom_handler.rise_since_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(rise_since_atom_handler.rise_tp_info_dict['ingredient'][0]['ingredient'][0])
            self.signal_name_list.\
                append(rise_since_atom_handler.rise_tp_info_dict['ingredient'][1]['ingredient'][0])

    def fall_tp_atom_process(self):
        operator_selected = self.operator_select()

        if operator_selected == 'eventually':
            fall_eventually_atom_handler = \
                FallEventuallyAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = fall_eventually_atom_handler.fall_tp_info_dict['expression']
            self.tp_atom_translation = \
                fall_eventually_atom_handler.fall_eventually_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(fall_eventually_atom_handler.fall_tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'always':
            fall_always_atom_handler = \
                FallAlwaysAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = fall_always_atom_handler.fall_tp_info_dict['expression']
            self.tp_atom_translation = \
                fall_always_atom_handler.fall_always_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(fall_always_atom_handler.fall_tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'once':
            fall_once_atom_handler = \
                FallOnceAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = fall_once_atom_handler.fall_tp_info_dict['expression']
            self.tp_atom_translation = \
                fall_once_atom_handler.fall_once_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(fall_once_atom_handler.fall_tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'historically':
            fall_historically_atom_handler = \
                FallHistoricallyAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = fall_historically_atom_handler.fall_tp_info_dict['expression']
            self.tp_atom_translation = \
                fall_historically_atom_handler.fall_historically_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(fall_historically_atom_handler.fall_tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'until':
            fall_until_atom_handler = \
                FallUntilAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = fall_until_atom_handler.fall_tp_info_dict['expression']
            self.tp_atom_translation = \
                fall_until_atom_handler.fall_until_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(fall_until_atom_handler.fall_tp_info_dict['ingredient'][0]['ingredient'][0])
            self.signal_name_list.\
                append(fall_until_atom_handler.fall_tp_info_dict['ingredient'][1]['ingredient'][0])

        else:  # operator_selected == 'since'
            fall_since_atom_handler = \
                FallSinceAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = fall_since_atom_handler.fall_tp_info_dict['expression']
            self.tp_atom_translation = \
                fall_since_atom_handler.fall_since_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(fall_since_atom_handler.fall_tp_info_dict['ingredient'][0]['ingredient'][0])
            self.signal_name_list.\
                append(fall_since_atom_handler.fall_tp_info_dict['ingredient'][1]['ingredient'][0])

    def not_rise_tp_atom_process(self):
        operator_selected = self.operator_select()

        if operator_selected == 'eventually':
            not_rise_eventually_atom_handler = \
                NotRiseEventuallyAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = not_rise_eventually_atom_handler.not_rise_tp_info_dict['expression']
            self.tp_atom_translation = \
                not_rise_eventually_atom_handler.not_rise_eventually_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(not_rise_eventually_atom_handler.not_rise_tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'always':
            not_rise_always_atom_handler = \
                NotRiseAlwaysAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = not_rise_always_atom_handler.not_rise_tp_info_dict['expression']
            self.tp_atom_translation = \
                not_rise_always_atom_handler.not_rise_always_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(not_rise_always_atom_handler.not_rise_tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'once':
            not_rise_once_atom_handler = \
                NotRiseOnceAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = not_rise_once_atom_handler.not_rise_tp_info_dict['expression']
            self.tp_atom_translation = \
                not_rise_once_atom_handler.not_rise_once_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(not_rise_once_atom_handler.not_rise_tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'historically':
            not_rise_historically_atom_handler = \
                NotRiseHistoricallyAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = not_rise_historically_atom_handler.not_rise_tp_info_dict['expression']
            self.tp_atom_translation = \
                not_rise_historically_atom_handler.not_rise_historically_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(not_rise_historically_atom_handler.not_rise_tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'until':
            not_rise_until_atom_handler = \
                NotRiseUntilAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = not_rise_until_atom_handler.not_rise_tp_info_dict['expression']
            self.tp_atom_translation = \
                not_rise_until_atom_handler.not_rise_until_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(not_rise_until_atom_handler.not_rise_tp_info_dict['ingredient'][0]['ingredient'][0])
            self.signal_name_list.\
                append(not_rise_until_atom_handler.not_rise_tp_info_dict['ingredient'][1]['ingredient'][0])

        else:  # operator_selected == 'since'
            not_rise_since_atom_handler = \
                NotRiseSinceAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = not_rise_since_atom_handler.not_rise_tp_info_dict['expression']
            self.tp_atom_translation = \
                not_rise_since_atom_handler.not_rise_since_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(not_rise_since_atom_handler.not_rise_tp_info_dict['ingredient'][0]['ingredient'][0])
            self.signal_name_list.\
                append(not_rise_since_atom_handler.not_rise_tp_info_dict['ingredient'][1]['ingredient'][0])

    def not_fall_tp_atom_process(self):
        operator_selected = self.operator_select()

        if operator_selected == 'eventually':
            not_fall_eventually_atom_handler = \
                NotFallEventuallyAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = not_fall_eventually_atom_handler.not_fall_tp_info_dict['expression']
            self.tp_atom_translation = \
                not_fall_eventually_atom_handler.not_fall_eventually_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(not_fall_eventually_atom_handler.not_fall_tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'always':
            not_fall_always_atom_handler = \
                NotFallAlwaysAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = not_fall_always_atom_handler.not_fall_tp_info_dict['expression']
            self.tp_atom_translation = \
                not_fall_always_atom_handler.not_fall_always_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(not_fall_always_atom_handler.not_fall_tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'once':
            not_fall_once_atom_handler = \
                NotFallOnceAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = not_fall_once_atom_handler.not_fall_tp_info_dict['expression']
            self.tp_atom_translation = \
                not_fall_once_atom_handler.not_fall_once_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(not_fall_once_atom_handler.not_fall_tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'historically':
            not_fall_historically_atom_handler = \
                NotFallHistoricallyAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = not_fall_historically_atom_handler.not_fall_tp_info_dict['expression']
            self.tp_atom_translation = \
                not_fall_historically_atom_handler.not_fall_historically_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(not_fall_historically_atom_handler.not_fall_tp_info_dict['ingredient'][0]['ingredient'][0])

        elif operator_selected == 'until':
            not_fall_until_atom_handler = \
                NotFallUntilAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = not_fall_until_atom_handler.not_fall_tp_info_dict['expression']
            self.tp_atom_translation = \
                not_fall_until_atom_handler.not_fall_until_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(not_fall_until_atom_handler.not_fall_tp_info_dict['ingredient'][0]['ingredient'][0])
            self.signal_name_list.\
                append(not_fall_until_atom_handler.not_fall_tp_info_dict['ingredient'][1]['ingredient'][0])

        else:  # operator_selected == 'since'
            not_fall_since_atom_handler = \
                NotFallSinceAtomHandler(self.position, self.nest_info_dict, self.limit_num)
            self.tp_atom_expression = not_fall_since_atom_handler.not_fall_tp_info_dict['expression']
            self.tp_atom_translation = \
                not_fall_since_atom_handler.not_fall_since_atom_translator.random_selected_translations
            self.signal_name_list.\
                append(not_fall_since_atom_handler.not_fall_tp_info_dict['ingredient'][0]['ingredient'][0])
            self.signal_name_list.\
                append(not_fall_since_atom_handler.not_fall_tp_info_dict['ingredient'][1]['ingredient'][0])

#
# group_num = 100
# abnormal_record = {
#     'eventually': [],
#     'always': [],
#     'once': [],
#     'historically': [],
#     'until': [],
#     'since': [],
#     'not_until': [],
#     'not_since': []
# }
#
#
# # until
# # information of position: two options
# # 1 - 'before_imply'
# # 2 - 'after_imply'
# position = 'after_imply'
#
# # information of nesting
# nest_info_dict = {
#     'whetherNest': False,
#     'nestLayer': 1,
#     'whetherBottom': True,
#     'hasParallelSuccessor': False,
#     'tense': 'present'
# }
#
# for i in range(group_num):
#     until_handler = UntilHandler(position, nest_info_dict)
#     print(until_handler.tp_info_dict['until'])
#     print('\n')
#     until_handler.until_translator.display_random_translation()
#     num = len(until_handler.until_translator.random_selected_translations)
#     if num != 1000:
#         abnormal_record['until'].append(i+1)
#         abnormal_record['until'].append(until_handler.tp_info_dict['expression'])
#     print('until:', i+1)
#
#
# # since
# # information of position: two options
# # 1 - 'before_imply'
# # 2 - 'after_imply'
# position = 'after_imply'
#
# # information of nesting
# nest_info_dict = {
#     'whetherNest': False,
#     'nestLayer': 1,
#     'whetherBottom': True,
#     'hasParallelSuccessor': False,
#     'tense': 'present'
# }
#
# for i in range(group_num):
#     since_handler = SinceHandler(position, nest_info_dict)
#     print(since_handler.tp_info_dict['since'])
#     print('\n')
#     since_handler.since_translator.display_random_translation()
#     num = len(since_handler.since_translator.random_selected_translations)
#     if num != 1000:
#         abnormal_record['since'].append(i+1)
#         abnormal_record['since'].append(since_handler.tp_info_dict['expression'])
#     print('since:', i+1)
#
#
# # not_until
# # information of position: two options
# # 1 - 'before_imply'
# # 2 - 'after_imply'
# position = 'after_imply'
#
# # information of nesting
# nest_info_dict = {
#     'whetherNest': False,
#     'nestLayer': 1,
#     'whetherBottom': True,
#     'hasParallelSuccessor': False,
#     'tense': 'present'
# }
#
# for i in range(group_num):
#     not_until_handler = NotUntilHandler(position, nest_info_dict)
#     print(not_until_handler.not_tp_info_dict)
#     print(not_until_handler.not_tp_info_dict['expression'])
#     print('\n')
#     not_until_handler.not_until_translator.display_random_translation()
#     num = len(not_until_handler.not_until_translator.random_selected_translations)
#     if num != 1000:
#         abnormal_record['not_until'].append(i+1)
#         abnormal_record['not_until'].append(not_until_handler.not_tp_info_dict['expression'])
#     print('not_until:', i+1)
#
#
# # not_since
# # information of position: two options
# # 1 - 'before_imply'
# # 2 - 'after_imply'
# position = 'after_imply'
#
# # information of nesting
# nest_info_dict = {
#     'whetherNest': False,
#     'nestLayer': 1,
#     'whetherBottom': True,
#     'hasParallelSuccessor': False,
#     'tense': 'present'
# }
#
# for i in range(group_num):
#     not_since_handler = NotSinceHandler(position, nest_info_dict)
#     print(not_since_handler.not_tp_info_dict)
#     print(not_since_handler.not_tp_info_dict['expression'])
#     print('\n')
#     not_since_handler.not_since_translator.display_random_translation()
#     num = len(not_since_handler.not_since_translator.random_selected_translations)
#     if num != 1000:
#         abnormal_record['not_since'].append(i+1)
#         abnormal_record['not_since'].append(not_since_handler.not_tp_info_dict['expression'])
#     print('not_since:', i+1)
#
#
# # eventually
# # information of position: two options
# # 1 - 'before_imply'
# # 2 - 'after_imply'
# position = 'after_imply'
#
# # information of nesting
# nest_info_dict = {
#     'whetherNest': False,
#     'nestLayer': 1,
#     'whetherBottom': True,
#     'hasParallelSuccessor': False,
#     'tense': 'present'
# }
#
# for i in range(group_num):
#     eventually_handler = EventuallyHandler(position, nest_info_dict)
#     print(eventually_handler.tp_info_dict)
#     print(eventually_handler.tp_info_dict['expression'])
#     print('\n')
#     eventually_handler.eventually_translator.display_random_translation()
#     num = len(eventually_handler.eventually_translator.random_selected_translations)
#     if num != 1000:
#         abnormal_record['eventually'].append(i+1)
#         abnormal_record['eventually'].append(eventually_handler.tp_info_dict['expression'])
#     print('eventually:', i+1)
#
#
# # always
# # information of position: two options
# # 1 - 'before_imply'
# # 2 - 'after_imply'
# position = 'after_imply'
#
# # information of nesting
# nest_info_dict = {
#     'whetherNest': False,
#     'nestLayer': 1,
#     'whetherBottom': True,
#     'hasParallelSuccessor': False,
#     'tense': 'present'
# }
#
# for i in range(group_num):
#     always_handler = AlwaysHandler(position, nest_info_dict)
#     print(always_handler.tp_info_dict)
#     print(always_handler.tp_info_dict['expression'])
#     print('\n')
#     always_handler.always_translator.display_random_translation()
#     num = len(always_handler.always_translator.random_selected_translations)
#     if num != 1000:
#         abnormal_record['always'].append(i+1)
#         abnormal_record['always'].append(always_handler.tp_info_dict['expression'])
#     print('always:', i+1)
#
#
# # once
# # information of position: two options
# # 1 - 'before_imply'
# # 2 - 'after_imply'
# position = 'after_imply'
#
# # information of nesting
# nest_info_dict = {
#     'whetherNest': False,
#     'nestLayer': 1,
#     'whetherBottom': True,
#     'hasParallelSuccessor': False,
#     'tense': 'present'
# }
#
# for i in range(group_num):
#     once_handler = OnceHandler(position, nest_info_dict)
#     print(once_handler.tp_info_dict)
#     print(once_handler.tp_info_dict['expression'])
#     print('\n')
#     once_handler.once_translator.display_random_translation()
#     num = len(once_handler.once_translator.random_selected_translations)
#     if num != 1000:
#         abnormal_record['once'].append(i+1)
#         abnormal_record['once'].append(once_handler.tp_info_dict['expression'])
#     print('once:', i+1)
#
#
# # historically
# # information of position: two options
# # 1 - 'before_imply'
# # 2 - 'after_imply'
# position = 'after_imply'
#
# # information of nesting
# nest_info_dict = {
#     'whetherNest': False,
#     'nestLayer': 1,
#     'whetherBottom': True,
#     'hasParallelSuccessor': False,
#     'tense': 'present'
# }
#
# for i in range(group_num):
#     historically_handler = HistoricallyHandler(position, nest_info_dict)
#     print(historically_handler.tp_info_dict)
#     print(historically_handler.tp_info_dict['expression'])
#     print('\n')
#     historically_handler.historically_translator.display_random_translation()
#     num = len(historically_handler.historically_translator.random_selected_translations)
#     if num != 1000:
#         abnormal_record['historically'].append(i+1)
#         abnormal_record['historically'].append(historically_handler.tp_info_dict['expression'])
#     print('historically:', i+1)
#
# print(abnormal_record)
