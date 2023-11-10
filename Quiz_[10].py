import random

def generate_lotto_numbers():
    lotto_numbers = []

    for i in range(6):
        while True:
            number = random.randint(1, 45)
            if number not in lotto_numbers:
                lotto_numbers.append(number)
                break

    lotto_numbers.sort()

    result_string = "생성된 로또 번호는 {} 입니다.".format(', '.join(map(str, lotto_numbers)))
    print(result_string)

    return lotto_numbers

generate_lotto_numbers()
