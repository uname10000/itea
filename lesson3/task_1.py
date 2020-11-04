import time


def decorator(amount):
    def dec(func):
        def wrapper(value):
            info_dict = dict()

            info_dict['name'] = func.__name__
            info_dict['total_time'] = 0
            list_of_times = []

            for i in range(amount):
                start_time = time.time()
                result = func(value)
                diff_time = time.time() - start_time

                list_of_times.append(diff_time)
                info_dict['total_time'] += diff_time

            info_dict['list_of_times'] = list_of_times
            info_dict['last_result_of_func'] = result

            # for i in list_of_times:
            #     info_dict['total_time'] += i

            return info_dict
        return wrapper
    return dec


@decorator(10)
def some_function(amount):
    list_of_elements = []
    for i in range(amount):
        list_of_elements.append(i)

    sum_of_elements = 0
    for i in range(len(list_of_elements)):
        sum_of_elements += list_of_elements[i]

    return sum_of_elements


def show_info(info):
    print(f'function name: {info["name"]}')
    print(f'total_time: {info["total_time"]} sec')
    print(f'last_result: {info["last_result_of_func"]}')

    print('-'*20)
    print('function work time:')
    for elem in range(len(info['list_of_times'])):
        print(str(elem + 1) + ': ' + '{0:.20f}'.format(info['list_of_times'][elem]) + ' sec')


result = some_function(1000000)
show_info(result)

