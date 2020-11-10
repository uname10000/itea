import datetime


class Article:
    def __init__(self, username, title, text):
        self.username = username
        self.title = title
        self.text = text


class Person:
    def __init__(self, name, password, is_admin, register_date):
        # self.person = {
        #     'name': None,
        #     'password': None,
        #     'is_admin': None,
        #     'register-date': None,
        # }
        self.name = name
        self.password = password
        self.is_admin = is_admin
        self.register_date = register_date


class Authorization:
    # users { user1: password, user2, password }
    # users = dict()
    users = list()

    def __init__(self):
        self.name = None
        self.password = None
        self.is_admin = None
        self.is_registered = None
        # print('Autorization init')

    @classmethod
    def user_register(cls, username, password, is_admin=False):
        # cls.users[username] = password
        cls.users.append(Person(username, password, is_admin, register_date=datetime.datetime.now()))
        print('user successfully registered')

    @classmethod
    def authentication(cls, username, password):
        # if user in cls.users.keys() and password in cls.users[user]:
        #     return True
        # return False
        if cls.users:
            for user in cls.users:
                if username == user.name:
                    if password == user.password:
                        return True

        return False

    @classmethod
    def is_user_admin(cls, username):
        print(f'is_user_admin: {username}')
        if cls.users:
            for user in cls.users:
                if username == user.name:
                    if user.is_admin:
                        # print(f'is_user_admin: name: {user.name}, admin:{user.is_admin}')
                        return True
        # print('is_user_admin: return false')
        return False

    @classmethod
    def validation_password_check(cls, password):
        digits = 0
        symbols = 0
        for i in range(len(password)):
            if password[i].isnumeric():
                digits += 1
            else:
                symbols += 1

        if digits == 0:
            return False, 'In password must be at least one digit'
        if symbols == 0:
            return False, 'In password must be at least one symbol'

        return True, 'Password validated'

    @classmethod
    def is_unique_login(cls, login):
        # if login not in cls.users:
        #     return True
        # else:
        #     return False

        if cls.users:
            for user in cls.users:
                if login not in user.name:
                    return True
                else:
                    return False
        else:
            # list is empty
            return True



class User(Authorization):
    # def __new__(cls, *args, **kwargs):
    #     # new_user = User(name, password, is_admin=False)
    #     # print(kwargs['user'])
    #     # check is created
    #     if Authorization.is_unique_login(args[0]):
    #         # user is not register
    #         # check password
    #         if Authorization.validation_password_check(args[1]):
    #             # register user
    #             Authorization.user_register(args[0], args[1])
    #             pass
    #         else:
    #             # return false
    #             return "Error in password validation"
    #     else:
    #         return "Login already exists"
    #
    #     new_user = super().__new__()
    #     return new_user

    def __init__(self):
        # self.name = None
        # self.password = None
        # self.is_admin = None
        # self.is_registered = None
        super().__init__()
        # print('user init')

    def login(self, username, password):
        # print(f'user.login: name: {username}, password:{password}')
        if self.authentication(username, password):
            self.name = username
            self.is_registered = True

            # print(f'user.login: is admin name: {username}, password:{password}')
            if self.is_user_admin(username):
                self.is_admin = True
            else:
                self.is_admin = False
            return True
        else:
            return False

    def logout(self):
        self.name = None
        self.is_registered = None
        self.is_admin = None


def show_message(user):
    system_message = """commands:
        register - register new user,
        register admin - register admin user
        login - login user ( username, password )
        help - show this message again
        exit - exit from program"""
    user_message = """commands:
        logout - user logout
        list - list articles
        create - create article
        exit - exit from program"""
    admin_message = """commands:
        logout - user logout
        list users - list all user
        list articles - list all articles
        exit - exit from program"""
    if user.is_registered:
        if user.is_admin:
            print(admin_message)
        else:
            print(user_message)
    else:
        print(system_message)


def show_input(user):
    if user.is_registered:
        if user.is_admin:
            return f'{user.name}# '
        else:
            return f'{user.name}> '
    else:
        return '> '


def show_user_articles(user, articles):
    count = 0
    if articles:
        for article in articles:
            if user.name == article.username:
                count += 1
                print(f'Article {count}:')
                print(f'title: {article.title}')
                print(f'text: {article.text}')
                print('-'*40)

    if count == 0:
        print(f'user: {user.name} have not articles')


def create_user_articles(user, articles):
    title = input('Enter title> ')
    text = input('Enter text> ')
    articles.append(Article(user.name, title, text))


def show_admin_articles(user, articles):
    count = 0
    if articles:
        for article in articles:
            count += 1
            print(f'number: {count}')
            print(f'user: {article.username}')
            print(f'title: {article.title}')
            print(f'text: {article.text}')
            print('-'*40)


def show_users():
    count = 0
    if User.users:
        for user in User.users:
            count += 1
            if user.is_admin:
                admin = 'Yes'
            else:
                admin = 'No'
            print(f'user: {count}')
            print(f'name: {user.name}')
            print(f'admin: {admin}')
            print(f'register date: {user.register_date}')
            print('-'*40)


user = User()
articles = list()

show_message(user)

is_work = True
while is_work:
    text = input(show_input(user))

    if text == 'exit':
        is_work = False
        break

    if text == 'help':
        show_message(user)
        continue

    if text == '':
        continue

    if user.is_registered:
        if user.is_admin:
            if text == 'logout':
                print('logout')
                user.logout()
                show_message(user)
            elif text == 'list users':
                show_users()
            elif text == 'list articles':
                show_admin_articles(user, articles)
            # elif text == 'exit':
            #     break
            else:
                print('Wrong Command')

        else:
            if text == 'logout':
                print('logout')
                user.logout()
                show_message(user)
            elif text == 'list':
                show_user_articles(user, articles)
            elif text == 'create':
                create_user_articles(user, articles)
            # elif text == 'exit':
            #     break
            else:
                print('Wrong Command')
    else:
        if text == 'login':
            # print('login: user, password')
            login = input('enter login: ')
            password = input('enter password: ')
            # print(f'login: {login}, password:{password}')
            if user.login(login, password):
                # print('login succsess')
                # print(f'name: {user.name}')
                # print(f'is_reg: {user.is_registered}')
                # print(f'is_admin: {user.is_admin}')
                show_message(user)
            else:
                print('Incorrect login or password')
                continue
        elif text == 'register':
            login = input('enter login: ')
            password = input('enter password: ')

            if not user.is_unique_login(login):
                print('Login already exist: ')
                continue

            pass_ret = user.validation_password_check(password)
            if not pass_ret[0]:
                print(pass_ret[1])
                continue

            user.user_register(login, password)
        elif text == 'register admin':
            login = input('enter login: ')
            password = input('enter password: ')

            if not user.is_unique_login(login):
                print('Login already exist: ')
                continue

            pass_ret = user.validation_password_check(password)
            if not pass_ret[0]:
                print(pass_ret[1])
                continue

            user.user_register(login, password, is_admin=True)
        else:
            print('Wrong command')
            continue
