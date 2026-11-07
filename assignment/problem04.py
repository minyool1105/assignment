#짝수만 화면에 출력하고 짝수의 총 개수를 세는 프로그램
numbers = [12, 7, 19, 20, 33, 42, 8, 15, 26, 31]
count = 0

for i in range(len(numbers)):
    num = numbers[i]
    if num % 2 == 0:
        count += 1
        print(numbers[i])
print("짝수의 개수 :",count)