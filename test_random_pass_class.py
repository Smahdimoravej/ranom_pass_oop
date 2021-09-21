import string
import random


class password_generation:

    def __init__(self, digit_number, lower_case_number,
                 upper_case_number, special_character_number):
        self.digit_number = digit_number
        self.lower_case_number = lower_case_number
        self.upper_case_number = upper_case_number
        self.special_character_number = special_character_number

    def digits():
        dig = int(input('''if you want your pass has digit_number ,
                write number of it else write no: '''))
        return dig

    def lower():
        lower = int(input('''if you want your pass has lower_case_number ,
                write number of it else write no: '''))
        return lower

    def upper():
        upper = int(input('''if you want your pass has upper_case_number ,
                write number of it else write no: '''))
        return upper

    def special():
        special = int(input('''if you want your pass has special_character_number ,
                write number of it else write no: '''))
        return special

    def password_generation(dig, lower, upper, special):
        a = "".join(random.choice(string.digits) for i in range(dig))
        b = "".join(random.choice(string.ascii_lowercase) for i in range(lower))
        c = "".join(random.choice(string.ascii_uppercase) for i in range(upper))
        d = "".join(random.choice(string.punctuation) for i in range(special))
        x = "".join(list(a) + list(b) + list(c) + list(d))
        x = list(x)
        if len(x) < 8:
            print("excuse me sir,the length of password cannot lower than 8")
            a = "".join(random.choice(string.digits) for i in range(2))
            b = "".join(random.choice(string.ascii_lowercase) for i in range(2))
            c = "".join(random.choice(string.ascii_uppercase) for i in range(2))
            d = "".join(random.choice(string.punctuation) for i in range(2))
            x = "".join(list(a) + list(b) + list(c) + list(d))
            x = list(x)
            random.shuffle(x)
            print("".join(x))
        else:
            # print(x)
            random.shuffle(x)
            # print(x)
            print("".join(x))


sample = password_generation.password_generation(3,2,1,2)
