import random
import os
import art
from random_data import data

points = 0


while True:
    print(art.logo)

    first_random = random.choice(data)
    second_random = random.choice(data)

    if first_random != second_random:
        if points > 0:
            print(f"You're right! current score is: {points}")

        print(f"Compare A: {first_random['name']} {first_random['description']} from {first_random['country']}")
        print(art.vs)
        print(f"Against B: {second_random['name']} {second_random['description']} from {second_random['country']}")

        answer = input("Who has more followers? Type 'A' or 'B': ")

        if answer.capitalize() == "A":
            if first_random['follower_count'] > second_random['follower_count']:
                points += 1
            else:
                print(f"You are wrong. Your score is {points}")
                break
        else:
            if second_random['follower_count'] > first_random['follower_count']:
                points += 1
            else:
                print(f"You are wrong. Your score is {points}")
                break
    os.system("clear")