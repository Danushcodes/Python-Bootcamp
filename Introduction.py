# Prompts to get user input
name= input("What is your name?: ")
age = input("How old are you?: ")
place = input("Where are you from?: ")
hobby = input("What is your No.1 favourite hobby?: ")
# I’ve used \n to insert blank lines between the input prompts and the output for better readability.
print(f"\n \n \nYour simple introduction:\n"
      f" Hi I'm {name}, {age}yrs old "
      f"\n I'm from {place}, "
      f"\n and my favourite hobby is {hobby} ")
