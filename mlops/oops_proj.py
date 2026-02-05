class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()


    def menu(self):
        user_input=input(""""welcome to chat book 
        1. signup
        2. signin
        3.write a post
        4.message to a friend
        5.exit """)
        if(user_input=="1"):
            self.signup()
        elif(user_input=="2"):
            self.signin()
        elif(user_input=="3"):
            self.write_post()
        elif(user_input=="4"):
            self.message_friend()
        else:
            exit()
    def signup(self):
        self.username=input("enter username")
        self.password=input("enter password")
        print("signup successful")
        self.menu()
    def signin(self):
        if self.username=='' and self.password=='':
            print("no user found please signup first")
        else:
            username=input("enter username")
            password=input("enter password")
            if(username==self.username and password==self.password):
                self.loggedin=True
                print("signin successful")
            else:
                print("invalid credentials")
            self.menu()
    def write_post(self):
        if self.loggedin:
            post=input("write your post:")
            print("post published:",post)
        else:
            print("please signin first to write a post")
        self.menu()

    def message_friend(self):
        if self.loggedin:
            friend=input("enter friend's name:")
            message=input("enter your message:")
            print(f"message sent to {friend}: {message}")
        else:
            print("please signin first to message a friend")
        self.menu()

obj=chatbook()