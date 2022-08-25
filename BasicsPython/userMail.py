class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, new_mail):
        if isinstance(new_mail, str):
            if new_mail.count('@') == 1:
                index_of_affe = new_mail.index('@')
                if new_mail[index_of_affe: len(new_mail)].count('.') == 1:
                    self.__email = new_mail
                    return
        print(f'ErrorMail:{new_mail}')

    email = property(fget=get_email, fset=set_email)


if __name__ == '__main__':
    k = UserMail('belosnezhka', 'prince@wait.you')
    print(k.email)  # prince@wait.you
    k.email = [1, 2, 3]  # ErrorMail:[1, 2, 3]
    k.email = 'prince@still@.wait'  # ErrorMail:prince@still@.wait
    k.email = 'prince@still.wait'
    print(k.email)  # prince@still.wait
