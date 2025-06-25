# Keep asking for input until correct password "python"

attempt = ""
tries = 0

while attempt != "Leoisno1":
    attempt = input("Enter password: ")
    tries += 1

print(f"Access granted after {tries} tries!")
