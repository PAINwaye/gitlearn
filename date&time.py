from datetime import datetime

try:
    user_input = input("Enter your name: ")

except Exception as e:
    print("Error occurred:", e)

else:
    now = datetime.now()
    print(f"Hello {user_input}!")
    print("Current Date and Time:", now)

finally:
    print("Program executed successfully.")