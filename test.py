import time

user_text = input("enter text: ")
print(f"your text: {user_text}")

# Force the script to stay open
print("keeping background thread alive..")

while True:
    time.sleep(1)