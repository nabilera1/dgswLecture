# 숫자를 입력받아 정렬하여 출력한다.
# 이 때 중복된 숫자는 하나만 나오도록 하시오.
# [입력] : 4 5 1 2 3 4 3
# [출력] : 1 2 3 4 5
# n = map(int, input().split()) # <map object at 0x000001F0B91D2190>

n = list(map(int, input().split()))  # 리스트로 입력 받는 문장은 반드시 암기
print(n)
n = list(set(n))  # set()은 알아서 중복 사항 제거
print(n)
n.sort()
print(n)

