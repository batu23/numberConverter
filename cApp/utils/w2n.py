
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


def get_words_as_number(number_sentence):

    split_words = number_sentence.strip().split()  # strip extra spaces and split sentence into words

    clean_numbers = []

    # removing and, & etc.
    for word in split_words:
        if word in numbers_dict:
            clean_numbers.append(word)

    # Error message if the user enters invalid input!
    if len(clean_numbers) == 0:
        raise ValueError("No valid number words found! Please enter a valid number word (eg. two million twenty three thousand and forty nine)") 

    # Error if user enters million,billion, thousand or decimal point twice
    if clean_numbers.count('thousand') > 1 or clean_numbers.count('million') > 1 or clean_numbers.count('billion') > 1:
        raise ValueError("Redundant number word! Please enter a valid number word (eg. two million twenty three thousand and forty nine)")

    billion_index = clean_numbers.index('billion') if 'billion' in clean_numbers else -1
    million_index = clean_numbers.index('million') if 'million' in clean_numbers else -1
    thousand_index = clean_numbers.index('thousand') if 'thousand' in clean_numbers else -1
    hundred_index = clean_numbers.index('hundred') if 'hundred' in clean_numbers else -1

    if (thousand_index > -1 and (thousand_index < million_index or thousand_index < billion_index)) or (million_index>-1 and million_index < billion_index):
        raise ValueError("Malformed number! Please enter a valid number word (eg. two million twenty three thousand and forty nine)")

    total_sum = 0  # storing the number to be returned

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
                total_sum += million_multiplier * 1000000

            if thousand_index > -1:
                if million_index > -1:
                    thousand_multiplier = number_formation(clean_numbers[million_index+1:thousand_index])
                elif billion_index > -1 and million_index == -1:
                    thousand_multiplier = number_formation(clean_numbers[billion_index+1:thousand_index])
                else:
                    thousand_multiplier = number_formation(clean_numbers[0:thousand_index])
                total_sum += thousand_multiplier * 1000

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


def main():
    n = str(raw_input("Please enter an number:\n>> "))

    # if len(str(n)) > 16:
    #     print("Please enter less than quadrillion")
    #     exit(0)
    # expected='ninety-five quadrillion, five hundred and five trillion, eight hundred and ninety-six billion, six hundred and thirty-nine million, six hundred and thirty-one thousand, eight hundred and ninety-three'
    print(get_words_as_number(n))
    # print(expected)
    # assert(get_number_as_words(n)==expected)


if __name__ == "__main__":
    main()
