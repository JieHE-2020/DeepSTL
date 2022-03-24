import random
from public import parameters
import global_variables_num


def atom_value_find():
    # flag = random.randint(0, 1)
    # # flag = 0
    #
    # if flag == 0:  # generate integer number
    #     value = random.randint(0, 10000)
    # else:  # generate decimal number
    #     value = random.uniform(0, 10000)
    #     decimal_len = random.randint(1, 4)
    #     value = round(value, decimal_len)

    index = global_variables_num.get_value('NUM_COUNTER')
    index = index + 1
    global_variables_num.set_value('NUM_COUNTER', index)
    value = 'num' + str(index) + 'value#'
    return value


def atom_value_range_find():
    # flag = random.randint(0, 1)
    # # flag = 0
    #
    # if flag == 0:  # generate integer number
    #     value1 = random.randint(0, 9998)
    #     value2 = random.randint(value1 + 1, 10000)
    # else:  # generate real number
    #     value1 = random.uniform(0, 9999)
    #     decimal_len = random.randint(1, 4)
    #     value1 = round(value1, decimal_len)
    #
    #     value2 = random.uniform(value1 + 0.1, 10000)
    #     decimal_len = random.randint(1, 4)
    #     value2 = round(value2, decimal_len)

    # value_a = value1
    # value_b = value2

    index = global_variables_num.get_value('NUM_COUNTER')
    index = index + 1
    global_variables_num.set_value('NUM_COUNTER', index)
    value_a = 'num' + str(index) + 'valuea#'
    value_b = 'num' + str(index) + 'valueb#'
    return [value_a, value_b]


def t_value_find():
    # flag = random.randint(0, 1)
    #
    # if flag == 0:  # generate integer number
    #     value = random.randint(1, 10000)
    # else:  # generate decimal number
    #     value = random.uniform(0.2, 10000)
    #     decimal_len = random.randint(1, 4)
    #     value = round(value, decimal_len)

    index = global_variables_num.get_value('NUM_COUNTER')
    index = index + 1
    global_variables_num.set_value('NUM_COUNTER', index)
    value = 'num' + str(index) + 'temporal#'
    return value


def t_value_range_find():
    # flag = random.randint(0, 1)
    #
    # if flag == 0:  # generate integer number
    #     t_value_a = random.randint(1, 9998)
    #     t_value_b = random.randint(t_value_a + 1, 10000)
    # else:  # generate real number
    #     t_value_a = random.uniform(0.2, 9999)
    #     decimal_len = random.randint(1, 4)
    #     t_value_a = round(t_value_a, decimal_len)
    #
    #     t_value_b = random.uniform(t_value_a + 0.1, 10000)
    #     decimal_len = random.randint(1, 4)
    #     t_value_b = round(t_value_b, decimal_len)

    index = global_variables_num.get_value('NUM_COUNTER')
    index = index + 1
    global_variables_num.set_value('NUM_COUNTER', index)
    t_value_a = 'num' + str(index) + 'temporala#'
    t_value_b = 'num' + str(index) + 'temporalb#'
    return [t_value_a, t_value_b]


def atom_value_substitute():
    flag = random.randint(1, 100)

    if flag <= 75:  # generate integer number with 0.75 prob
        point = random.randint(1, 10)
        if 1 <= point <= 4:  # with 0.4 prob
            value = random.randint(0, 10)
        elif 5 <= point <= 8:  # with 0.4 prob
            value = random.randint(0, 100)
        else:  # with 0.2 prob
            value = random.randint(0, 3000)
    else:  # generate decimal number with 0.25 prob
        point = random.randint(1, 10)
        if 1 <= point <= 4:  # with 0.4 prob
            value = random.uniform(0, 10)
        elif 5 <= point <= 8:  # with 0.4 prob
            value = random.uniform(0, 100)
        else:  # with 0.2 prob
            value = random.uniform(0, 3000)
        decimal_len = random.randint(1, 2)
        value = round(value, decimal_len)

    value = str(value)
    return value


def atom_value_range_substitute():
    flag = random.randint(1, 100)

    if flag <= 75:  # generate integer number with 0.75 prob
        point = random.randint(1, 10)
        if 1 <= point <= 4:  # with 0.4 prob
            value_a = random.randint(0, 8)
            value_b = random.randint(value_a + 1, 10)
        elif 5 <= point <= 8:  # with 0.4 prob
            value_a = random.randint(0, 98)
            value_b = random.randint(value_a + 1, 100)
        else:  # with 0.2 prob
            value_a = random.randint(0, 2998)
            value_b = random.randint(value_a + 1, 3000)
    else:  # generate decimal number with 0.25 prob
        point = random.randint(1, 10)
        if 1 <= point <= 4:  # with 0.4 prob
            value1 = random.uniform(0, 9.5)
            value2 = random.uniform(value1 + 0.1, 10)
        elif 5 <= point <= 8:  # with 0.4 prob
            value1 = random.uniform(0, 99.5)
            value2 = random.uniform(value1 + 0.1, 100)
        else:  # with 0.2 prob
            value1 = random.uniform(0, 2999.5)
            value2 = random.uniform(value1 + 0.1, 3000)
        decimal_len = random.randint(1, 2)
        value_a = round(value1, decimal_len)
        value_b = round(value2, decimal_len)

    value_a = str(value_a)
    value_b = str(value_b)
    return [value_a, value_b]


def t_value_substitute():
    flag = random.randint(1, 100)

    if flag <= 75:  # generate integer number with 0.75 prob
        point = random.randint(1, 10)
        if 1 <= point <= 4:  # with 0.4 prob
            value = random.randint(1, 10)
        elif 5 <= point <= 8:  # with 0.4 prob
            value = random.randint(1, 100)
        else:  # with 0.2 prob
            value = random.randint(1, 3000)
    else:  # generate decimal number with 0.25 prob
        point = random.randint(1, 10)
        if 1 <= point <= 4:  # with 0.4 prob
            value = random.uniform(0.2, 10)
        elif 5 <= point <= 8:  # with 0.4 prob
            value = random.uniform(0.2, 100)
        else:  # with 0.2 prob
            value = random.uniform(0.2, 3000)
        decimal_len = random.randint(1, 2)
        value = round(value, decimal_len)

    t_value = str(value)
    return t_value


def t_value_range_substitute():
    flag = random.randint(1, 100)

    if flag <= 75:  # generate integer number with 0.75 prob
        point = random.randint(1, 10)
        if 1 <= point <= 4:  # with 0.4 prob
            value_a = random.randint(1, 8)
            value_b = random.randint(value_a + 1, 10)
        elif 5 <= point <= 8:  # with 0.4 prob
            value_a = random.randint(1, 98)
            value_b = random.randint(value_a + 1, 100)
        else:  # with 0.2 prob
            value_a = random.randint(1, 2998)
            value_b = random.randint(value_a + 1, 3000)
    else:  # generate decimal number with 0.25 prob
        point = random.randint(1, 10)
        if 1 <= point <= 4:  # with 0.4 prob
            value1 = random.uniform(0.2, 9.5)
            value2 = random.uniform(value1 + 0.1, 10)
        elif 5 <= point <= 8:  # with 0.4 prob
            value1 = random.uniform(0.2, 99.5)
            value2 = random.uniform(value1 + 0.1, 100)
        else:  # with 0.2 prob
            value1 = random.uniform(0.2, 2999.5)
            value2 = random.uniform(value1 + 0.1, 3000)
        decimal_len = random.randint(1, 2)
        value_a = round(value1, decimal_len)
        value_b = round(value2, decimal_len)

    t_value_a = str(value_a)
    t_value_b = str(value_b)
    return [t_value_a, t_value_b]
