class User:

    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        self.followers=0
        self.following=0
    def follow(self):
        self.followers+=1
    def following(self):
        self.following+=1

user_1=User(881,'Dev')
print(user_1.id)