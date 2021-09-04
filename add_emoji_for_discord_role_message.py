count = 0
emoji = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "keycap_ten", "hash", "asterisk"]
# Replace the placeholder text with roles to add emoji's to followed by a new line
classes = "placeholder"

for line in classes.splitlines():
    print(":" + emoji[count] + ": " + line)
    count += 1
    if (count == 13):
        break