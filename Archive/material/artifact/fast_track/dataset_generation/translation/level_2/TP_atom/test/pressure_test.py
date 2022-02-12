from translation.TP.OriginalTP.eventually.normal.eventually_handler import EventuallyHandler
from translation.TP.OriginalTP.always.normal.always_handler import AlwaysHandler
from translation.TP.OriginalTP.once.normal.once_handler import OnceHandler
from translation.TP.OriginalTP.historically.normal.historically_handler import HistoricallyHandler
from translation.TP.OriginalTP.until.normal.until_handler import UntilHandler
from translation.TP.OriginalTP.since.normal.since_handler import SinceHandler
from translation.TP.NotTP.not_until.not_until_handler import NotUntilHandler
from translation.TP.NotTP.not_since.not_since_handler import NotSinceHandler


group_num = 100
abnormal_record = {
    'eventually': [],
    'always': [],
    'once': [],
    'historically': [],
    'until': [],
    'since': [],
    'not_until': [],
    'not_since': []
}


# until
# information of position: two options
# 1 - 'before_imply'
# 2 - 'after_imply'
position = 'after_imply'

# information of nesting
nest_info_dict = {
    'whetherNest': False,
    'nestLayer': 1,
    'whetherBottom': True,
    'hasParallelSuccessor': False,
    'tense': 'present'
}

for i in range(group_num):
    until_handler = UntilHandler(position, nest_info_dict)
    print(until_handler.tp_info_dict['until'])
    print('\n')
    until_handler.until_translator.display_random_translation()
    num = len(until_handler.until_translator.random_selected_translations)
    if num != 1000:
        abnormal_record['until'].append(i+1)
        abnormal_record['until'].append(until_handler.tp_info_dict['expression'])
    print('until:', i+1)


# since
# information of position: two options
# 1 - 'before_imply'
# 2 - 'after_imply'
position = 'after_imply'

# information of nesting
nest_info_dict = {
    'whetherNest': False,
    'nestLayer': 1,
    'whetherBottom': True,
    'hasParallelSuccessor': False,
    'tense': 'present'
}

for i in range(group_num):
    since_handler = SinceHandler(position, nest_info_dict)
    print(since_handler.tp_info_dict['since'])
    print('\n')
    since_handler.since_translator.display_random_translation()
    num = len(since_handler.since_translator.random_selected_translations)
    if num != 1000:
        abnormal_record['since'].append(i+1)
        abnormal_record['since'].append(since_handler.tp_info_dict['expression'])
    print('since:', i+1)


# not_until
# information of position: two options
# 1 - 'before_imply'
# 2 - 'after_imply'
position = 'after_imply'

# information of nesting
nest_info_dict = {
    'whetherNest': False,
    'nestLayer': 1,
    'whetherBottom': True,
    'hasParallelSuccessor': False,
    'tense': 'present'
}

for i in range(group_num):
    not_until_handler = NotUntilHandler(position, nest_info_dict)
    print(not_until_handler.not_tp_info_dict)
    print(not_until_handler.not_tp_info_dict['expression'])
    print('\n')
    not_until_handler.not_until_translator.display_random_translation()
    num = len(not_until_handler.not_until_translator.random_selected_translations)
    if num != 1000:
        abnormal_record['not_until'].append(i+1)
        abnormal_record['not_until'].append(not_until_handler.not_tp_info_dict['expression'])
    print('not_until:', i+1)


# not_since
# information of position: two options
# 1 - 'before_imply'
# 2 - 'after_imply'
position = 'after_imply'

# information of nesting
nest_info_dict = {
    'whetherNest': False,
    'nestLayer': 1,
    'whetherBottom': True,
    'hasParallelSuccessor': False,
    'tense': 'present'
}

for i in range(group_num):
    not_since_handler = NotSinceHandler(position, nest_info_dict)
    print(not_since_handler.not_tp_info_dict)
    print(not_since_handler.not_tp_info_dict['expression'])
    print('\n')
    not_since_handler.not_since_translator.display_random_translation()
    num = len(not_since_handler.not_since_translator.random_selected_translations)
    if num != 1000:
        abnormal_record['not_since'].append(i+1)
        abnormal_record['not_since'].append(not_since_handler.not_tp_info_dict['expression'])
    print('not_since:', i+1)


# eventually
# information of position: two options
# 1 - 'before_imply'
# 2 - 'after_imply'
position = 'after_imply'

# information of nesting
nest_info_dict = {
    'whetherNest': False,
    'nestLayer': 1,
    'whetherBottom': True,
    'hasParallelSuccessor': False,
    'tense': 'present'
}

for i in range(group_num):
    eventually_handler = EventuallyHandler(position, nest_info_dict)
    print(eventually_handler.tp_info_dict)
    print(eventually_handler.tp_info_dict['expression'])
    print('\n')
    eventually_handler.eventually_translator.display_random_translation()
    num = len(eventually_handler.eventually_translator.random_selected_translations)
    if num != 1000:
        abnormal_record['eventually'].append(i+1)
        abnormal_record['eventually'].append(eventually_handler.tp_info_dict['expression'])
    print('eventually:', i+1)


# always
# information of position: two options
# 1 - 'before_imply'
# 2 - 'after_imply'
position = 'after_imply'

# information of nesting
nest_info_dict = {
    'whetherNest': False,
    'nestLayer': 1,
    'whetherBottom': True,
    'hasParallelSuccessor': False,
    'tense': 'present'
}

for i in range(group_num):
    always_handler = AlwaysHandler(position, nest_info_dict)
    print(always_handler.tp_info_dict)
    print(always_handler.tp_info_dict['expression'])
    print('\n')
    always_handler.always_translator.display_random_translation()
    num = len(always_handler.always_translator.random_selected_translations)
    if num != 1000:
        abnormal_record['always'].append(i+1)
        abnormal_record['always'].append(always_handler.tp_info_dict['expression'])
    print('always:', i+1)


# once
# information of position: two options
# 1 - 'before_imply'
# 2 - 'after_imply'
position = 'after_imply'

# information of nesting
nest_info_dict = {
    'whetherNest': False,
    'nestLayer': 1,
    'whetherBottom': True,
    'hasParallelSuccessor': False,
    'tense': 'present'
}

for i in range(group_num):
    once_handler = OnceHandler(position, nest_info_dict)
    print(once_handler.tp_info_dict)
    print(once_handler.tp_info_dict['expression'])
    print('\n')
    once_handler.once_translator.display_random_translation()
    num = len(once_handler.once_translator.random_selected_translations)
    if num != 1000:
        abnormal_record['once'].append(i+1)
        abnormal_record['once'].append(once_handler.tp_info_dict['expression'])
    print('once:', i+1)


# historically
# information of position: two options
# 1 - 'before_imply'
# 2 - 'after_imply'
position = 'after_imply'

# information of nesting
nest_info_dict = {
    'whetherNest': False,
    'nestLayer': 1,
    'whetherBottom': True,
    'hasParallelSuccessor': False,
    'tense': 'present'
}

for i in range(group_num):
    historically_handler = HistoricallyHandler(position, nest_info_dict)
    print(historically_handler.tp_info_dict)
    print(historically_handler.tp_info_dict['expression'])
    print('\n')
    historically_handler.historically_translator.display_random_translation()
    num = len(historically_handler.historically_translator.random_selected_translations)
    if num != 1000:
        abnormal_record['historically'].append(i+1)
        abnormal_record['historically'].append(historically_handler.tp_info_dict['expression'])
    print('historically:', i+1)

print(abnormal_record)
