# 숫자를 입력받아 정렬하여 출력한다.
# 이 때 중복된 숫자는 하나만 나오도록 하시오.
# [입력] : 4 5 1 2 3 4 3
# [출력] : 1 2 3 4 5

# 파이썬으로 입력받는 연습
# a, b = map(int, input().split())
arr = list(map(int, input().split()))
print(arr)
# 중복 제거 하기
arr = list(set(arr))
# arr = set(arr) # {1, 2, 3, 4, 5}
print(arr)
arr.sort()
print(arr)

# 5명이 출입구에 모이면 번호가 큰순으로
# 들여보내야 한다.
# 이 때 중복된 번호의 학생은 한 명만 안으로 보내도록 하자.
# [입력] : 4 5 1 2 3
# [출력] : 5 4 3 2 1

# [입력] : 3 5 1 2 3
# [출력] : 5 3 2 1

# [입력] : 14 5 7 2 3
# [출력] : 14 7 5 3 2
students = list(set(map(int, input().split())))
students.sort(reverse=True)
for i in students:
    print(i, end=' ')
