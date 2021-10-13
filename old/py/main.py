import json
import os.path

print("Welcome to TwinkleMoneyTree")

class Tracker():


  def Inital_Setup():

    global Currnet_Saving_Money_Amount
    global UserName
    global Currnet_Queqing_Money_Amount
    global AccountStatus


    print("Please Enter your savings account amount: ")
    Currnet_Saving_Money_Amount = int(input(": "))

    print("Please Enter your queqing account amount: ")
    Currnet_Queqing_Money_Amount = int(input(": ")) 

    print("Please Enter who holds these accounts: ")
    UserName = input(": ")

    print("Please Enter the Accounts Status: ")
    AccountStatus = input(": ")


  def Writing_Data():
    Currnet_Saving_Money_Amount_str = {'Saving': {'Amount': Currnet_Saving_Money_Amount, 'Owner': UserName, 'Status': AccountStatus}}
    with open("log/Saving.json", "w") as write_saving:
      json.dump(Currnet_Saving_Money_Amount_str, write_saving, indent=4)

    Currnet_Queqing_Money_Amount_str = {'Queqing': {'Amount': Currnet_Queqing_Money_Amount, 'Owner': UserName, 'Status': AccountStatus}}
    with open("log/Queqing.json", "w") as write_queqing:
      json.dump(Currnet_Queqing_Money_Amount_str, write_queqing, indent=4)




Check_For_Saving = (os.path.exists("log/Saving.json"))
Check_For_Queqing = (os.path.exists("log/Queqing.json"))

if Check_For_Queqing & Check_For_Saving == True:
  pass
else:
  Tracker.Inital_Setup()


Command = input("How can I help you? \n : ").upper()

while True:
  if Command == "WRITEDATA":
    Tracker.Writing_Data()

  elif Command == "HELP" or "MAN":
    with open("help/help.txt", "rb") as Read_Help:
      print(Read_Help)


  elif Command == "BREAK" or "QUIT" or "STOP" or "EXIT":
    break
    quit()
  else:
    print("Wrong Command")