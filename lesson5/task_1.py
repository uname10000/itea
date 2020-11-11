from threading import Thread
import time


def decorator(name='default', is_daemon=False):
    def actual_decorator(func):
        def wrapper(*value):
            # func(*value)
            t = Thread(target=func, args=value, name=name, daemon=is_daemon)
            t.start()
            print(f'Thread name: {t.getName()}')
            print(f'Tread is daemon: {t.isDaemon()}')
        return wrapper
    return actual_decorator


@decorator('func_name', False)
def some_function(sec):
    print('some_function start')
    time.sleep(sec)
    print('some_function stop')


some_function(5)
