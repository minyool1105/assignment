import random

win = 0
draw = 0
lose = 0

# 가위 = 1, 바위 = 2, 보 = 3

while True:
    user = input("가위, 바위, 보 중 하나 입력 (종료: 그만): ")
    com = random.randint(1,3)
    # 여기에 코드를 작성하세요
    if user =="그만":
        print("승 :",win,"무 :",draw,"패 :",lose)
        break

    if user =="가위":
        if com == 1:
            draw += 1
            print('비겻습니다.')
        elif com == 2:
            win += 1
            print('사용자가 이겼습니다.')

        elif com == 3:
            lose += 1
            print("사용자가 패배했습니다.")

    elif user =="바위":
        if com == 1:
            win += 1
            print('사용자가 이겼습니다.')
        elif com == 2:
            draw += 1
            print('비겼습니다')

        elif com == 3:
            lose += 1
            print("사용자가 패배했습니다.")


    elif user =="보":
        if com == 1:
            lose += 1
            print('사용자가 패배했습니다.')
        elif com == 2:
            win += 1
            print('사용자가 이겼습니다.')

        elif com == 3:
            draw += 1
            print("비겼습니다.")
