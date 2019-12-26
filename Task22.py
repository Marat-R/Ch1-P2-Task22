def convert_c_f():
    return (temp * 9/5) + 32
def convert_f_c():
    return (temp - 32) * 5/9

temp = float(input("Enter temperature: "))
temp_type = input("\nCelsius or Fahrenheit: \nenter 'C / F':\n")

if temp_type == "C" or temp_type == "c":
    print(f"\n{temp} Celsius = {convert_c_f()} Fahrenheit")
elif temp_type == "F" or temp_type == "f":
    print(f"\n{temp} Fahrenheit = {convert_f_c()} Celsius")
else:
    print("Wrong input data!")
