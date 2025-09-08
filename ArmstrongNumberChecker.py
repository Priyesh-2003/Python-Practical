num = int(input("Enter a number: "))
power = len(str(num))
total = 0

for digit in str(num):
    total += int(digit) ** power

if total == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

print("This program is written and executed by PRIYESH (0231BCA024).")
