a=0
students = [
    {"name": "김민수", "grade": 1, "club": "밴드부", "attended": True},
    {"name": "이서연", "grade": 2, "club": "코딩부", "attended": True},
    {"name": "박지훈", "grade": 1, "club": "미술부", "attended": False},
    {"name": "최하은", "grade": 2, "club": "밴드부", "attended": True},
    {"name": "정준우", "grade": 1, "club": "코딩부", "attended": False}
]
print("[오늘의 출석 명단]")
for i in students:
    if i["attended"] == True:
        print(i["grade"],"학년",i["name"],i["club"],"- 출석 완료")

for i in students:
    if i["club"] == "코딩부":
        a = a+1
print("코딩부 총 인원",a,"명")