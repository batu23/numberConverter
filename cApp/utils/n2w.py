"""
Created by: Batuhan Demir on 27/09/2018
contact: dmrbatu23@gmail.com
"""

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
    """
    gets number splits it into smaller integers
    gets corresponding number from one of the lists above
    it starts from lower numbers up to 1000 and loops until billions
    therefore it appends words in reversed order
    finally returns reverses list to correct the order
    :param n: integer
    :return: res: string
    """
    res = []
    for i, num in enumerate(split_by_thousand(n)):
        if num:
            res.append(sub_thousand(num) + " " + thousands[i])

    return " and ".join(reversed(res))


def split_by_thousand(n):
    """
    parses integers up to billion down to sub thousand and returns remaining numbers list
    :param n: integer
    :return: res: list
    """
    res = []
    while n:
        n, r = divmod(n, 1000)
        res.append(r)
    return res


def sub_thousand(n):
    """
    gets integer up to thousand and parses given integer, calculates mathematical representation using modulation
    works in a recursive manner
    parsing from 1-19, 20-90 and 100-999 iteratively
    :param n: integer
    :return: res: string
    """
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
    """
    Gets the integer number returns corresponding string words
    :param n: integer
    :return:
    """
    if n == 0:
        return zero
    return normalize(abs(n))
