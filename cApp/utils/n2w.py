zero = 'zero'

up_to_19 = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen"
]

tens = [
    "",
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
]

thousands = [
    "",
    "thousand",
    "million",
    "billion",
]


def normalize(n):

    res = []
    for i, num in enumerate(split_by_thousand(n)):
        if num:
            res.append(sub_thousand(num) + " " + thousands[i])

    return " and ".join(reversed(res))


def split_by_thousand(n):
    res = []
    while n:
        n, r = divmod(n, 1000)
        res.append(r)
    return res


def sub_thousand(n):
    assert(0 <= n <= 999)
    if n <= 19:
        return up_to_19[n]
    elif n <= 99:
        quotient, remainder = divmod(n, 10)
        return tens[quotient] + (" " + sub_thousand(remainder) if remainder else "")
    else:
        quotient, remainder = divmod(n, 100)
        return up_to_19[quotient] + " hundred" + (" " + sub_thousand(remainder) if remainder else "")


def get_number_as_words(n):
    if n == 0:
        return zero
    return normalize(abs(n))
