import random

secret = random.randint(1, 100)
count = 0  # 시도 횟수

while True:
    user = int(input("숫자를 맞춰보세요."))
    if user > secret:
        print("DOWN!")
        count += 1
    elif user < secret:
        print("UP!")
        count += 1
    elif user == secret:
        print("정답!")
        count += 1
        print("당신의 시도 횟수는",count,"회 입니다.")
