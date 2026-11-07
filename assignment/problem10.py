words = {
    "사과": "apple",
    "바나나": "banana",
    "학교": "school"
}

for i in words:
    a = input(i+"를 영어로 하면?")
    if a == words[i]:
        print("정답!")
    elif a != words[i]:
        print("아쉽습니다. 정답은",words[i],"입니다.")