menu = {
    "삼각김밥": 1200,
    "바나나우유": 1700,
    "컵라면": 1500,
    "샌드위치": 2500
}

for item in menu:
    item = input("메뉴를 선택해주세요 : ")
    if item not in menu:
        print("해당 메뉴는 존재하지 않습니다.")
        break
    print("가격 :",menu[item])
    break
