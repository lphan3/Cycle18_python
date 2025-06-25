x = "10"  # should be int
y = 5.0
flag = "False"  # should be boolean

# Fix the variables so this prints: "Room 2 unlocked!"
if isinstance(x, int) and isinstance(y, float) and isinstance(flag, bool):
    print("Room 2 unlocked!")
else:
    print("Still locked...")
