"""
Created by: Batuhan Demir on 27/09/2018
contact: dmrbatu23@gmail.com
"""

numbers_dict = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 10**3,
    'million': 10**6,
    'billion': 10**9
}


def get_words_as_number(sentence):
    """
    given sentence of words of number returns corresponding integer value
    only works up to billion
    algorithm mainly works checking the indexes like billion, million, thousand and hundred
    returns error if word not in dict or words are not organized correctly like 'one thousand two thousand'
    takes words up to some index and formats, calculates mathematical result, going over the list from beginning to end
    :param sentence: string
    :return: result: integer
    """

    split_words = sentence.strip().split()  # strip extra spaces and split sentence into words list

    clean_numbers = []

    # append only if word is in dictionary
    for word in split_words:
        if word in numbers_dict:
            clean_numbers.append(word)

    # Error message if the user enters invalid input!
    if len(clean_numbers) == 0:
        raise ValueError("Please enter a valid number word (eg. six million and five hundred thousand and eight hundred sixty)")

    # Error if user enters million,billion, thousand or decimal point twice
    if clean_numbers.count('thousand') > 1 or clean_numbers.count('million') > 1 or clean_numbers.count('billion') > 1:
        raise ValueError("Please enter a valid number word (eg. six million and five hundred thousand and eight hundred sixty)")

    billion_index = clean_numbers.index('billion') if 'billion' in clean_numbers else -1
    million_index = clean_numbers.index('million') if 'million' in clean_numbers else -1
    thousand_index = clean_numbers.index('thousand') if 'thousand' in clean_numbers else -1
    hundred_index = clean_numbers.index('hundred') if 'hundred' in clean_numbers else -1

    # Error if  wrong order of words
    if (thousand_index > -1 and (thousand_index < million_index or thousand_index < billion_index)) or (million_index>-1 and million_index < billion_index):
        raise ValueError("Please enter a valid number word (eg. six million and five hundred thousand and eight hundred sixtye)")

    total_sum = 0

    # goes from billions down to hundred getting the words before the index or between the indexes in the list of words
    if len(clean_numbers) > 0:
        if len(clean_numbers) == 1:
                return numbers_dict[clean_numbers[0]]
        else:
            if billion_index > -1:
                billion_multiplier = number_formation(clean_numbers[0:billion_index])
                total_sum += billion_multiplier * numbers_dict['billion']

            if million_index > -1:
                if billion_index > -1:
                    million_multiplier = number_formation(clean_numbers[billion_index+1:million_index])
                else:
                    million_multiplier = number_formation(clean_numbers[0:million_index])
                total_sum += million_multiplier * numbers_dict['million']

            if thousand_index > -1:
                if million_index > -1:
                    thousand_multiplier = number_formation(clean_numbers[million_index+1:thousand_index])
                elif billion_index > -1 and million_index == -1:
                    thousand_multiplier = number_formation(clean_numbers[billion_index+1:thousand_index])
                else:
                    thousand_multiplier = number_formation(clean_numbers[0:thousand_index])
                total_sum += thousand_multiplier * numbers_dict['thousand']

            if hundred_index > -1:
                if thousand_index > -1 and thousand_index != len(clean_numbers)-1:
                    hundreds = number_formation(clean_numbers[thousand_index+1:])
                elif million_index > -1 and million_index != len(clean_numbers)-1:
                    hundreds = number_formation(clean_numbers[million_index+1:])
                elif billion_index > -1 and billion_index != len(clean_numbers)-1:
                    hundreds = number_formation(clean_numbers[billion_index+1:])
                elif thousand_index == -1 and million_index == -1 and billion_index == -1:
                    hundreds = number_formation(clean_numbers)
                else:
                    hundreds = 0
                total_sum += hundreds

    return total_sum


def number_formation(number_words):
    """
    Formats given word list to required number
    Gets corresponding word from dict and calculates mathematical result
    should be given at most 4 length of list eq. thousand at most
    :param number_words: list
    :return: result: integer
    """
    numbers = []
    for number_word in number_words:
        numbers.append(numbers_dict[number_word])
    if len(numbers) == 4:
        return (numbers[0] * numbers[1]) + numbers[2] + numbers[3]
    elif len(numbers) == 3:
        return numbers[0] * numbers[1] + numbers[2]
    elif len(numbers) == 2:
        if 100 in numbers:
            return numbers[0] * numbers[1]
        else:
            return numbers[0] + numbers[1]
    else:
        return numbers[0]
