x = "10"
y = 5.0
flag = "False"

# isinstance checks if a variable is a certain type
# isinstance(object, classinfo)
if isinstance(x, int) and isinstance(y, float) and isinstance(flag, bool):
    print("Room 2 unlocked!")
else:
    print("Still locked...")
