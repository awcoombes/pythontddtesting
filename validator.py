import re

def validate_account_number_format(account_string):
    b = re.findall("[A-Z]", account_string)
    c = re.findall("[a-z]", account_string)
    d = re.findall("[0-9]", account_string)
    if len(b) > 0 and len(c) > 0 and len(d) > 0:
        # print("Acceptable")
        return True
    else:
        # print("String must contain uppercase, lower case and numbers")
        return False

# while True:
#     a = input("Enter a string to check: ")
#     running = validate_account_number_format(a)
#     if running == False:
#         break