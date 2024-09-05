from datetime import *
#UserProfile
#username, password,email,age,is_login
#login,logout,update_email,change_paeeword,display
class UserProfile:
    # class attribute
    user_count = 0
    logged_in_users = 0
    logged_out_users = 0
    def __init__(self,username, password,email,age):
        self.username = username
        self.password = password
        self.is_valid_email(email)
        self.email = email
        self.age = age
        self.is_login = False
        self.logs = []
        self.count_login = 0
        UserProfile.user_count += 1
    def login(self, username, password):
        if self.is_login:
            print("you are logged in!")
        elif username == self.username and password == self.password:
            self.is_login = True
            self.logs.append(f"Logged in at {datetime.now()}")
            print(f"Welcome {self.username}")
            self.count_login += 1
            UserProfile.logged_in_users += 1
        else:
            print("your info in not correct!")
    def logout(self):
        if self.is_login:
            self.is_login = False
            self.logs.append(f"Logged out at {datetime.now()}")
            UserProfile.logged_in_users -= 1
            UserProfile.logged_out_users += 1
        else:
            print("User is not logges in!")
    def update_email(self, new_eamil):
        if self.is_login:
            try:
                self.is_valid_email(new_eamil)
                self.email = new_eamil
                self.logs.append("Email Updated!")
            except ValueError as e:
                print(e)
                self.logs.append(e)
        else:
            print("User is not logges in!")
    def change_pass(self, new_pass):
        if self.is_login:
            self.password = new_pass
            self.logs.append("Password Updated!")
        else:
            print("User is not logges in!")
    def show_logs(self):
        if self.is_login:
            result = "\n".join(self.logs)
            print(result)
        else:
            print("User is not logges in!")
    def display(self):
        print(self.username)
        print(self.password)
        print(self.email)
        print(self.age)
        print(self.is_login)
        print("*"*10,"logs")
        self.show_logs()
    @classmethod
    def number_of_users(cls):
        print(f"number of user: {cls.user_count}")
        print(f"logged in users: {cls.logged_in_users}")
        print(f"logged out users: {cls.logged_out_users}")
    @staticmethod
    def is_valid_email(email):
        if "." not in email or "@" not in email or len(email) < 5:
            raise ValueError("Invalid Email!")
        return True


if __name__ == "__main__":
    user1 = UserProfile("abc", "123", "a.b@gmail.com",17)
    print(user1.email)
    user1.login("abc", "123")
    user1.update_email("a.c")
    print(user1.email)
    print(user1.is_valid_email("a.b@gmail.com"))
    """user1.login("abc", "123")
    print(f"user1: {user1.count_login}")
    user2 = UserProfile("abc", "123", "a.b@gmail.com",17)
    print(f"user2: {user2.count_login}")
    print(user2.user_count)
    print(user1.user_count)
    print(UserProfile.user_count)
    UserProfile.number_of_users()
    user1.number_of_users()
    print(type(user1))
    user1.login("abc", "123")
    user2.login("abc", "123")
    user2.logout()
    print(UserProfile.logged_in_users)
    print(UserProfile.logged_out_users)
    UserProfile.number_of_users()"""
    """print(user1.age)
    user1.login("abc", "123")
    print(user1.is_login)
    #user1.logout()
    print(user1.is_login)
    print(user1.email)
    user1.update_email("m.d@gmail.com")
    print(user1.email)
    print(user1.password)
    user1.change_pass("a123")
    print(user1.password)
    user1.show_logs()
    user1.display()"""