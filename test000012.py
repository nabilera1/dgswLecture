import random  # 랜덤 모듈

# arr = list() # arr을 리스트로 선언
arr = []  # arr을 리스트로 선언
print(arr)  # []가 출력, 리스트 의미

for i in range(10):  # 10회 반복
    arr.append(random.randint(1, 100))
    # arr리스트에 랜덤한 값을 넣는다. 실행할 때마다 다른 랜덤 값

print('*' * 40)
print(arr)
print('*' * 40)

# 로또 번호 생성기
# for i in range(6):  # 6회 반복
    # arr.append(random.randint(1, 46))


# [문제] arr에 있는 데이터 중 가장 큰 값을 출력하시오.
# print(max(arr))



# [문제] 리스트에서 두번째 큰 값을 출력하시오.
# [팁] 먼저 정렬 실행
# 리스트 정렬
arr.sort()  # arr.sort(reversed=True)  --> arr[1]
print(arr)
print(f'리스트 두번째 값 : {arr[1]}')