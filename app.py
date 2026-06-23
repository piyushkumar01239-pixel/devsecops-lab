import os

name = input("Enter your name: ")
print(f"Hello, {name}")

app_password = os.getenv("APP_PASSWORD")

if app_password:
    print("Environment variable loaded successfully")