# print("*" * 10)
# print("*,*,*,*")
#
# print("----------")
# print("|        |")
# print("|        |")
# print("----------\n")
#
# print("          *     ")
# print("         ***    ")
# print("        *****    ")
# print("       *******    ")
# print("      *********    ")
# print("     ***********    ")
#
#
#
#
#
#
#
#
#
# print("          *     ")
# print("         ***    ")
# print("        *****    ")
# print("       *******    ")
# print("      *********    ")
# print("     ***********    ")
# print("      *       *    ")
# print("      *       *    ")
# print("      *  |****|    ")
# print("      *  |****|    ")
#
#
#
# # Ask person weight and calculate in kg
#
# p_weight = input("what is your weight : ")
# personal_weight_in_pound = 0.43 * int( p_weight)
# print(personal_weight_in_pound, "KG")
#
#
# # Ask person name and his favourite color then display on console "name likes color"
#
# name = input("what is your name :")
# f_color = input("what is your favourite color :")
# print(name, "likes" , f_color)

# what is the output of the following question

# s_name = 'jennefir'
# bini = s_name[1 : -1]
# print(bini)


# quiz (if statement)

#price of a house is 1M$ if buyer has good credit they need to put down 10% otherwise they need to put down 20% print down payment

# price = 100000
# is_good_credit = True # or False
#
# if is_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"down_payment is: ${down_payment}")


# name = input("enter :")
# if len(name) <= 3:
#     print("name my be atleast 3 characters.")
# elif len(name) < 50:
#     print("name can be maximum of 50 character.")
# else:
#     print("name looks good")


#quiz

weight = int(input("weight :"))
Unit = input("(L)lbs or K(kg) :")
if Unit.lower() == "L":
    converted= int(weight) * 0.45
    print(f"You are {converted} kilos")
else :
    converted =int(weight) / 0.45
    print(f"You are {converted} pounds")


