# Write your code here :-)
# counts all the 7's in a string unless they are followed by a 5
def count_sevens(text):
    seven_count = 0
    previous_digit = None
    for digit in text:
        if digit != "5" and previous_digit == "7":
            seven_count += 1
        previous_digit = digit
    return seven_count

print(count_sevens("1728498023475282948271483"))