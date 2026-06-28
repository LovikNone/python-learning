
import random
secret = random.randint(1, 100)
messages = [
    "Ошибка",
    "Попытки закончились. Число было:",
    "Слишком мало",
    "Слишком много",
    "Ты угадал!!"
]
try:
    for i in range(3):
        guess = int(input("Угадай число: "))

        if guess == secret:
            print(messages[4])
            break
        elif guess > secret:
            print(messages[3])
        else:
            print(messages[2])
    else:
        print(messages[1], secret)
except:
    print(messages[0])

