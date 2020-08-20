import random
import string

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    print("Here is your randomly generated strong password:", result_str)
    print("With this password you're accounts are secured as fuck!")
    print("Of course if some site, where are you using this password, had a huge breach including your password, you have a problem.")
    print("But remember you can generate other strong password, and change old for this new, and you are again secured as fuck!")

get_random_alphanumeric_string(14)
