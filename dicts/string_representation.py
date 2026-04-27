# https://stepik.org/lesson/488830/step/12?unit=480066

numbers = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

n = input()
res = []

for i in n:
    res.append(numbers[i])

print(' '.join(res))