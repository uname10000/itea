from threading import Thread
import urllib.request

files = list()

files.append('https://github.com/uname10000/itea/raw/master/lesson1/task_1.py')
files.append('https://github.com/uname10000/itea/raw/master/lesson1/task_2.py')
files.append('https://github.com/uname10000/itea/raw/master/lesson1/task_3.py')
files.append('https://github.com/uname10000/itea/raw/master/lesson1/task_4.py')
files.append('https://github.com/uname10000/itea/raw/master/lesson2/task_1.py')
files.append('https://github.com/uname10000/itea/raw/master/lesson2/task_2.py')
files.append('https://github.com/uname10000/itea/raw/master/lesson2/task_3.py')
files.append('https://github.com/uname10000/itea/raw/master/homework1/task_1.py')
files.append('https://github.com/uname10000/itea/raw/master/homework1/task_2.py')
files.append('https://github.com/uname10000/itea/raw/master/homework1/task_3.py')


def decorator(func):
    def wrapper(value):
        # func(value)
        t = Thread(target=func, args=(value, ))
        t.start()
    return wrapper


@decorator
def download(link):
    print(f'Downloading file: {link} started')
    file_name = link.split('/')
    file_name = 'download/' + file_name[-2] + '-' + file_name[-1]
    # print(file_name)
    urllib.request.urlretrieve(link, filename=file_name)

    print(f'Downloading file: {link} done')


for file in files:
    download(file)
