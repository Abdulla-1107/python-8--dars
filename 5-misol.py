import json

f = open("text.json", "r")

n = json.load(f)

login = input("Loginingizni kirting: ")
parol = input("parolingizni kriting: ")

# print(n)

for i in n:
    if i['login'] == login and i['parol'] == parol:
        print("OK")
        break
    if i['login'] == login and i['parol'] != parol:
        print("Xato parol kiritdingiz!")
        break
    if i['login'] != login and i['parol'] == parol:
        print("Bunday foydalanuvchi yo'q")
        break
    if i['login'] != login and i['parol'] != parol:
        print("Login va parol xato kiritilgan!")
        break



    


       
    
