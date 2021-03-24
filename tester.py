import validator

try:
    assert validator.validate_account_number_format("Aa1") == True
    assert validator.validate_account_number_format("") == False
    assert validator.validate_account_number_format("1") == False
    assert validator.validate_account_number_format("True") == False
    print("all tests passed")
except AssertionError:
    print("Failure")

