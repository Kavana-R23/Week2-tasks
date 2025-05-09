users=[
    {"id":1,"name":"Alice","email":"alice@example.com"},
    {"id":2,"name":"Bob","email":"bob@example.com"}
     ]

def addUser(user):
    users.append(user)

def getUserById(userId):
    for user in users:
        if user["id"]==userId:
            return user
    return None     
    
def update(userId,name=None,email=None):
    for user in users:
        if user["id"]==userId:
            if name:
                user["name"]=name
            if email:
                user["email"]=email
            return user
    return None

def delete(userId):
    for user in users:
        if user["id"]==userId:
            users.remove(user)
            return True
    return False

addUser(
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
    )
print("Read from list")
print(getUserById(2))  # print Bob's info
print("update list")
update(1, name="Alicia")
print("delete a list")
delete(2)
print(users) 