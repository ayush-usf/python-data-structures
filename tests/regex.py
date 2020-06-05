import re

email_pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"

print("Enter email :")
user_input_1 = input()

if(re.search(email_pattern, user_input_1)):
	print("valid email")
else:
	print("invalid input")

# ========================================

# remove hyphen from phone number

pattern = "(\d\d\d)-(\d\d\d)-(\d\d\d\d)"

# r => raw input string
new_pattern = r"\1\2\3"

print("Enter number (xxx-xxx-xxxx) :")
user_input = input()

new_user_input = re.sub(pattern, new_pattern, user_input)
print(new_user_input)
