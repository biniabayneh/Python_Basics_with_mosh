from os import lseek

tempreture = int(input("tempreture : "))
if tempreture > 30:
    print("it's hot day")
elif tempreture < 10 :
    print("it's cold day")
else:
    print("it's neither hot nor hold weather")