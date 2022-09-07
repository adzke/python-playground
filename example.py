# Example of Class inheritance 
# Adrian Stockwell
#
class User():

    def __init__(self, username, email):

        self.username = username
        self.email = email

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.email
        

class Developer(User):

    def __init__(self, username, email, userid):
        User.__init__(self, username, email)
        self.userid = userid

    def __str__(self):
        return str(self.userid)

    def __repr__(self):
        return self.email

    def developer_info(self):
        return "Dev info {} {}".format(self.userid, self.username)


user1 = User('jamesy', 'jamesy@gmail.com')
user2 = User('bobj', 'yahoo@gmail.com')
user3 = Developer('adrians', 'adrians@gmail.com', 3321)
user4 = Developer('jayjay', 'jayjay@gmail.com', 3322)

print(user4.developer_info())
