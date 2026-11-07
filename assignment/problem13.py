import random

lotto = [0, 0, 0, 0, 0, 0]  # 6칸을 미리 0으로 채워둔 리스트
count = 0  # 지금까지 채운 개수

while count < 6:
    num = random.randint(1, 45)
    # 여기에 중복 검사 및 번호 저장 코드를 작성하세요
    if num not in lotto:
        lotto[count] = num
        count += 1


print(lotto)
