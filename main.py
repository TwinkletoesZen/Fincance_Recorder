import json


print("Welcome to TwinkleMoneyTree")

Currnet_Saving_Money_Amount = 0
Currnet_Queqing_Money_Amount = 0

print(Currnet_Queqing_Money_Amount and Currnet_Saving_Money_Amount)

if (Currnet_Saving_Money_Amount + Currnet_Queqing_Money_Amount == 0):
  print("Please Enter your savings account amount: ")
  Currnet_Saving_Money_Amount = int(input(": "))

  print("Please Enter your queqing account amount: ")
  Currnet_Queqing_Money_Amount = int(input(": ")) 

Currnet_Saving_Money_Amount_str = {"Saving": {"Amount":"$" + str(Currnet_Saving_Money_Amount)}}
with open("AmountofMoney.json", "a") as write:
  json.dump(Currnet_Saving_Money_Amount_str, write, indent=4)


Currnet_Queqing_Money_Amount_str = {"Queqing": {"Amount":"$" + str(Currnet_Queqing_Money_Amount)}}
with open("AmountofMoney.json", "a") as write:
  json.dump(Currnet_Queqing_Money_Amount_str, write, indent=4)





# data = {"president": {"name": "Zaphod Beeblebrox","species": "Betelgeusian"}}

# with open("data_file.json", "w") as write_file:
#     json.dump(data, write_file, indent=4 )


# class Finance_Recorder:

#   def Input_Expense():
    