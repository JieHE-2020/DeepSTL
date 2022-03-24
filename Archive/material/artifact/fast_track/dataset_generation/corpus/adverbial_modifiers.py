import random

# represent 'at the same time'
adv_simultaneously = {'adverb': ['immediately', 'promptly', 'simultaneously', 'instantly']}

adv_phrase_simultaneously = {'adverbial_phrase': ['at once', 'right away', 'without any delay', 'starting without any delay',
                                                  'in no time', 'at the same moment', 'at the same time', 'at the same time instant',
                                                  'at the same time point']}

# preparation for adverbial modifiers of TP
temporal_future_0t = ['within t_value time units',
                      'in the first t_value time units',
                      'during the first t_value time units',
                      'within the first t_value time units',
                      'in the next t_value time units',
                      'during the next t_value time units',
                      'within the next t_value time units',
                      'in the following t_value time units',
                      'during the following t_value time units',
                      'within the following t_value time units',
                      'in the subsequent t_value time units',
                      'during the subsequent t_value time units',
                      'within the subsequent t_value time units',
                      'in the coming t_value time units',
                      'during the coming t_value time units',
                      'within the coming t_value time units']

temporal_future_ab = ['within t_value_a to t_value_b time units',
                      'in the first t_value_a to t_value_b time units',
                      'during the first t_value_a to t_value_b time units',
                      'within the first t_value_a to t_value_b time units',
                      'in the next t_value_a to t_value_b time units',
                      'during the next t_value_a to t_value_b time units',
                      'within the next t_value_a to t_value_b time units',
                      'in the following t_value_a to t_value_b time units',
                      'during the following t_value_a to t_value_b time units',
                      'within the following t_value_a to t_value_b time units',
                      'in the subsequent t_value_a to t_value_b time units',
                      'during the subsequent t_value_a to t_value_b time units',
                      'within the subsequent t_value_a to t_value_b time units',
                      'in the coming t_value_a to t_value_b time units',
                      'during the coming t_value_a to t_value_b time units',
                      'within the coming t_value_a to t_value_b time units']

# preparation for adverbial modifiers of TP
temporal_past_0t = ['in the past t_value time units',
                    'during the past t_value time units',
                    'within the past t_value time units',
                    'in the last t_value time units',
                    'during the last t_value time units',
                    'within the last t_value time units',
                    'in the elapsed t_value time units',
                    'during the elapsed t_value time units',
                    'within the elapsed t_value time units']

temporal_past_ab = ['in the past t_value_a to t_value_b time units',
                    'during the past t_value_a to t_value_b time units',
                    'within the past t_value_a to t_value_b time units',
                    'in the last t_value_a to t_value_b time units',
                    'during the last t_value_a to t_value_b time units',
                    'within the last t_value_a to t_value_b time units',
                    'in the elapsed t_value_a to t_value_b time units',
                    'during the elapsed t_value_a to t_value_b time units',
                    'within the elapsed t_value_a to t_value_b time units']

# keyword eventually
adv_eventually = {'adverb': ['eventually', 'finally', 'ultimately']}

temporal_phrase_eventually_end = ['in the future',
                                  'in the future before the simulation ends',
                                  'in the future before the end of the simulation',
                                  'in the future before the execution ends',
                                  'in the future before the end of the execution'
                                  ]

temporal_phrase_eventually_0t = ['starting at most t_value time units',
                                 'after at most t_value time units',
                                 'in less than t_value time units'] + temporal_future_0t

temporal_phrase_eventually_ab = ['starting between t_value_a to t_value_b time units',
                                 'after between t_value_a to t_value_b time units'] + \
                                temporal_future_ab

# keyword always
adv_always_refine = {'adverb': ['continuously', 'consistently', 'uninterruptedly', 'consecutively', 'always']}
adv_always_assemble = {'adverb': ['continuously', 'consistently', 'uninterruptedly', 'consecutively']}
adv_phrase_always_assemble = {'adverbial_phrase': ['all the time', 'without interruption']}

semantics_overall = ['every', 'each']
semantics_time_point = ['time point', 'time instant', 'moment']
semantics_each_time_point = []

for item1 in semantics_overall:
    for item2 in semantics_time_point:
        semantics_each_time_point.append(item1 + ' ' + item2)

temporal_phrase_always_end = ['in the future',
                              'in the future until the simulation ends',
                              'in the future until the end of the simulation',
                              'in the future until the execution ends',
                              'in the future until the end of the execution',
                              'in the future till the simulation ends',
                              'in the future till the end of the simulation',
                              'in the future till the execution ends',
                              'in the future before the simulation ends',
                              'in the future before the end of the simulation',
                              'in the future before the execution ends',
                              'in the future before the end of the execution'
                              ]

temporal_phrase_always_end_each_time = []
for item1 in semantics_each_time_point:
    for item2 in temporal_phrase_always_end:
        temporal_phrase_always_end_each_time.append('for' + ' ' + item1 + ' ' + item2)

# for i in temporal_phrase_always_end_each_time:
#     print(i)

point = random.randint(0, 1)
if point == 1:
    temporal_phrase_always_end = temporal_phrase_always_end + temporal_phrase_always_end_each_time
# for i in temporal_phrase_always_end:
#     print(i)

temporal_phrase_always_0t = ['for at least t_value time units',
                             'for more than t_value time units',
                             'for the first t_value time units',
                             'for the next t_value time units',
                             'for the following t_value time units',
                             'for the subsequent t_value time units',
                             'for the coming t_value time units'] + temporal_future_0t

temporal_phrase_always_0t_each_time = []
for item1 in semantics_each_time_point:
    for item2 in temporal_future_0t:
        temporal_phrase_always_0t_each_time.append('for' + ' ' + item1 + ' ' + item2)

# for i in temporal_phrase_always_0t_each_time:
#     print(i)

point = random.randint(0, 1)
if point == 1:
    temporal_phrase_always_0t = temporal_phrase_always_0t + temporal_phrase_always_0t_each_time
# for i in temporal_phrase_always_0t:
#     print(i)

temporal_phrase_always_ab = ['for the first t_value_a to t_value_b time units',
                             'for the next t_value_a to t_value_b time units',
                             'for the following t_value_a to t_value_b time units',
                             'for the subsequent t_value_a to t_value_b time units',
                             'for the coming t_value_a to t_value_b time units',
                             'between t_value_a to t_value_b time units'] + \
                            temporal_future_ab

temporal_phrase_always_ab_each_time = []
for item1 in semantics_each_time_point:
    for item2 in temporal_future_ab:
        temporal_phrase_always_ab_each_time.append('for' + ' ' + item1 + ' ' + item2)

# for i in temporal_phrase_always_ab_each_time:
#     print(i)

point = random.randint(0, 1)
if point == 1:
    temporal_phrase_always_ab = temporal_phrase_always_ab + temporal_phrase_always_ab_each_time
# for i in temporal_phrase_always_ab:
#     print(i)

# keyword once
adv_once = {'adverb': ['once']}

temporal_phrase_once_start = ['in the past',
                              'during the past',
                              'in the past from the start of the execution',
                              'in the past from the beginning of the execution',
                              'in the past starting from the beginning of the execution',
                              'in the past from the start of the simulation',
                              'in the past from the beginning of the simulation',
                              'in the past starting from the beginning of the simulation'
                              ]

temporal_phrase_once_0t = ['before at most t_value time units',
                           'before less than t_value time units'] + temporal_past_0t

temporal_phrase_once_ab = ['before between t_value_a to t_value_b time units'] + temporal_past_ab

# keyword historically
adv_historically_refine = {'adverb': ['continuously', 'consistently', 'uninterruptedly', 'consecutively', 'always']}
adv_historically_assemble = {'adverb': ['continuously', 'consistently', 'uninterruptedly', 'consecutively']}
adv_phrase_historically_assemble = {'adverbial_phrase': ['all the time', 'without interruption']}

temporal_phrase_historically_start = ['in the past',
                                      'during the past',
                                      'in the past since the start of the execution',
                                      'in the past since the beginning of the execution',
                                      'in the past since the start of the simulation',
                                      'in the past since the beginning of the simulation'
                                      ]

temporal_phrase_historically_0t = ['for the past t_value time units',
                                   'for the last t_value time units',
                                   'for the elapsed t_value time units'] + temporal_past_0t

temporal_phrase_historically_ab = ['for the past t_value_a to t_value_b time units',
                                   'for the last t_value_a to t_value_b time units',
                                   'for the elapsed t_value_a to t_value_b time units'] + temporal_past_ab
