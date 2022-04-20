print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")                                  
name = name1.lower() + name2.lower()
num = name.count("t") + name.count("r") + name.count("u") + name.count("e")
num2 = name.count("l") + name.count("o") + name.count("v") + name.count("e")
value = int(str(num) + str(num2))

if value < 10 or value > 90:
 print(f"Your score is {value}, you go together like coke and mentos.")
elif value >= 40 and value <= 50:
  print(f"Your score is {value}, you are alright together.")
else:
  print(f"Your score is {value}.")

