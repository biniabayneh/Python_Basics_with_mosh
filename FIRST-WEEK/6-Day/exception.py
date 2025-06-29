try :
    age = int(input("Age :"))
    income= 2000
    total = income/age
    print(total)
except ZeroDivisionError:
    print("number divisible by zero is not")
except ValueError:
    print("invalid values please try it within correct numerical value")
