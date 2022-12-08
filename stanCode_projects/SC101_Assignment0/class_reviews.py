"""
File: class_reviews.py
Name: Ting-Wen (Wenny)
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""
# EXIT = -1


def main():
    """
    This program is to separate the sc101 and sc001 scores and figure out their avg, min, max individually
    after the users fill in the classes and the scores.
    """
    total_101 = 0
    total_001 = 0
    number_101 = 0
    number_001 = 0
    clas = input('Which class? ')
    if clas == '-1':
        print("No class scores is entered")
    else:
        score = int(input('Score: '))
        if clas == 'sc001' or clas == 'Sc001' or clas == 'sC001' or clas == 'SC001':
            max_001 = score
            min_001 = score
            # avg_001 = score
            total_001 = score
            number_001 += 1  # edited
        elif clas == 'sc101' or clas == 'Sc101' or clas == 'sC101' or clas == 'SC101':
            max_101 = score
            min_101 = score
            # avg_101 = score
            total_101 = score
            number_101 += 1  # edited
        while True:
            clas = input('Which class? ')
            if clas == 'sc001' or clas == 'Sc001' or clas == 'sC001' or clas == 'SC001':
                score = int(input('Score: '))
                if number_001 == 0:
                    max_001 = score
                    min_001 = score
                else:
                    if score > max_001:
                        max_001 = score
                    elif score < min_001:
                        min_001 = score
                total_001 += score
                number_001 += 1  # edited
                # avg_001 = total_001/number
            elif clas == 'sc101' or clas == 'Sc101' or clas == 'sC101' or clas == 'SC101':
                score = int(input('Score: '))
                if number_101 == 0:
                    max_101 = score
                    min_101 = score
                else:
                    if score > max_101:
                        max_101 = score
                    if score < min_101:
                        min_101 = score
                total_101 += score
                number_101 += 1  # edited
                # avg_101 = total_101 / number
            elif clas == '-1':  # edited, clas is a string, but EXIT is a int
                break

        # edited, outside the while loop
        equals()
        print('SC001', end='')
        equals()
        print('')

        if total_001 != 0:
            print('Max (001): ' + str(max_001))
            print('Min (001): ' + str(min_001))
            print('Avg (001): ' + str(total_001 / number_001))
        else:
            print('No score for SC001')

        equals()
        print('SC101', end='')
        equals()
        print('')

        if total_101 != 0:
            print('Max (101): ' + str(max_101))
            print('Min (101): ' + str(min_101))
            print('Avg (101): ' + str(total_101 / number_101))
        else:
            print('No score for SC101')


def equals():
    for i in range(13):
        print('=', end='')  #
    # return

# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #


if __name__ == '__main__':
    main()
