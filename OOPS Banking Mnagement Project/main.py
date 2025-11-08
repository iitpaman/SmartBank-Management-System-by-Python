import json
import random
import string
from pathlib import Path




class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exist")
    except Exception as err:
        print(f"an exception occured as {err}")
        


    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))


    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k = 3)
        num = random.choices(string.digits, k = 3)
        spchar = random.choices("!@#$%^&*", k = 1)
        id  = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)




    def Createaccount(self):
        info = {
            "name": input("Tell me your name :- "),
            "age": int(input("Tell me your age :- ")),
            "Email": input("Tell me your Email :- "),
            "pin": int(input("Tell me your four digit Pin :- ")),
            "accountNo": Bank.__accountgenerate(),
            "balance": 0,

        
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry you can not create your account")
        
        else:
            print("Account has been created Sucessfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please notedown your account number")
            Bank.data.append(info)
            
            Bank.__update()


    def depositmoney(self):
        accnumber = input("Please tell your account number :- ")
        pin = int(input("Please tell your pin as well :- "))

        # userdata =[i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        userdata =[i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("sorry no data found")
            return
        
        else:
            amount = int(input("How much you want to deposite :- "))
            if amount > 10000 and amount < 0:
                print("Sorry the amount is to much you can deposite below 10000")

            else:
                print(userdata)
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited Sucessfully")

    def withdrawmoney(self):
        accnumber = input("Please tell your account number :- ")
        pin = int(input("Pleaase tell your pin as well as :- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("Sorry no data Found")
            return
        else:
            amount = int(input("How much amount you want to withdraw :- "))
            if userdata[0]['balance'] < amount:
                print("Sorry you dont have much money")


            else:
                print(userdata)
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount Withdrew sucessfully")
                print(f"Remaining balance: {userdata[0]['balance']}")


    def  showdetails(self):

        accnumber = input("Please tell your Account Number :- ")
        pin = int(input("Please tell your pin :- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        print("_____Your Information are ______\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

        
    def updatedetails(self):

        accnumber = input("please tell your Account Number :- ")
        pin = int(input("Please tell your pin as well as :-"))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("No such user found ")
            return
        
        else:
            print("You can not change Age AccountNo and Balance")

            print("Fill the Details for change or leave the empty if no change")

            newdata = {
                "name": input("Please tell new Name or press Enter skip :- "),
                "Email": input("Please tell your new Email or press Enter to skip :- "),
                "pin" : input("Enter new Pin or press enter to skip :- ")

            }

            if newdata['name'] == "":
                newdata['name'] = userdata[0]['name']

            if newdata['Email'] == "":
                newdata['Email'] = userdata[0]['Email']

            if newdata['pin'] == "":
                newdata['pin'] = userdata[0]['pin']

            newdata['age'] = userdata[0]['age']

            newdata['accountNo'] = userdata[0]['accountNo']

            newdata['balance'] = userdata[0]['balance']

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print("Details updated sucessfully")

    def delete(self):
        accnumber = input("please tell your Account Number :- ")
        pin = int(input("Please tell your pin as well as :-"))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("No such user found ")
            return
        
        else:
            check = input("Press Y , if you actually want to delete the account or press N :- ")
            if check == "n" or check == "N":
                print("Bypassed")
            
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account Delete  successfully")

                Bank.__update()



user = Bank()
print("Press 1 for creating an account")
print("Press 2 for depositing the money in the Bank")
print("Press 3 for withdrawing the money")
print("Press 4 for details")
print("Press 5 for updating the details")
print("Press 6 for deleting the account")

check = int(input("Tell me your response :- "))

if check == 1:
    user.Createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.delete()