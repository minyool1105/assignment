password = ""

while True:
    password = input("비밀번호를 입력하세요 : ")
    if password == "python123":
        print("로그인 성공! 환영합니다.")
        break

    else:
        print("비밀번호가 틀렸습니다. 다시 입력하세요.")