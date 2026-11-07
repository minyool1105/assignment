
a = int(input("나이를 입력하세요 : "))
if a<8:
    print("무료입니다.")
elif a>=8 and a <= 19:
    print("입장료는 10,000원입니다.")
elif a >= 20 and a <= 64:
    print("입장료는 20,000원입니다.")
elif a>= 65:
    print("입장료는 5,000원입니다.")