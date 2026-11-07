#for는 배열과 같이 자주 쓰임
"""
arr = ["apple", "banana", "cherry"]

print("메뉴 리스트")
for item in arr:
    print(item)

print("------------------")
print("메뉴 리스트")
sale_list = {'apple':1, 'banana':0, 'cherry':3}
for key in sale_list:
    if sale_list[key] == 0:
        print(key, "sold out")
    else:
        print(key, sale_list[key])

print("------------------")
for i in range(10):
    print(i)

# while 문으로 동일하게 수행하려면
a = 0
while a < 10:
    print(a)
    a += 1 
"""




class_scores = [ { "name": "김철수", "scores": {"국어": 85, "영어": 90, "수학": 78, "과학": 92} }, { "name": "이영희", "scores": {"국어": 92, "영어": 88, "수학": 95, "과학": 96} }, { "name": "박민수", "scores": {"국어": 76, "영어": 65, "수학": 82, "과학": 70} }, { "name": "정수진", "scores": {"국어": 88, "영어": 94, "수학": 90, "과학": 89} }, { "name": "한동석", "scores": {"국어": 60, "영어": 72, "수학": 65, "과학": 58} } ]
#개인별 평균 점수
#과목별 최고 득점자
#이름으로 검색해서 성적을 알아보는 메ㅠ






##평균 점수
for i in range(5):
   print(class_scores[i]["name"],"평균" , class_scores[i]["scores"]["국어"]/4 + class_scores[i]["scores"]["영어"]/4 + class_scores[i]["scores"]["수학"]/4 + class_scores[i]["scores"]["과학"]/4)

#과목별 최고 득점자
korean = []
english = []
math = []
science = []
for j in range(5):
    korean.append(class_scores[j]["scores"]["국어"])
    english.append(class_scores[j]["scores"]["영어"])
    math.append(class_scores[j]["scores"]["수학"])
    science.append(class_scores[j]["scores"]["과학"])


