iin_ranges = [
        [340000,379999, "American Express"],
        [510000,559999, "Mastercard"],
        [560000,599999, "Maestro"],
        [400000,499999, "Visa"]
        ]

def check_issuer(card_number):
    iin = int(card_number[:6])
    for start, end, issuer in iin_ranges:
        if iin >= start and iin<=end:
            return issuer
    return "unknown"


def digits_of(n):
    return [int(d) for d in str(n)]


def LuhnChecksum(card_number ):
    digits=digits_of(card_number)
    odd_digits = digits[-1::-2] # every 2 backwards starting from -1
    even_digits = digits[-2::-2] # every 2 backwards starting from -2

    Checksum = 0
    Checksum += sum(odd_digits)
    for l in even_digits:
        Checksum += sum(digits_of(l*2))
    return (10- (Checksum % 10)) % 10


def isLuhnValid(card_number):
    if LuhnChecksum(card_number) == 0:
        print("The number that was given as input:{} is a valid CC number".format(card_number))
    else:
        print("The number that was given as input:{} is not a valid CC number".format(card_number))
    print("The issuer is: {}".format(check_issuer(card_number)))
