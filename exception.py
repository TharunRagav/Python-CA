try:
    a = 5/1
except ZeroDivisionError as e:
    print("Error occured")
else:
    print("Code Executed")
#except block used


try:
    b = 5/0
except ZeroDivisionError as e:
    print("Error occured")
else:
    print("Code Executed")
#else block used


try:
    num = int(input("Enter number: "))
    result = 100 / num

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Execution completed")
#finally block used


age = 15

try:
    if age < 18:
        raise ValueError("Age must be 18 or above")
except ValueError as e:
    print("Error:", e)

else:
    print("Eligible")
#raising error