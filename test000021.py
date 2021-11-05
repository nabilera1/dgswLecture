#숫자를 입력받아 총합을 구하는 프로그램을 만드시오.
#1 2 3 4
#10

n=list(map(int, input().split()))
print(sum(n))


# 만약 아래로 입력을 받는다면
# 단, 5개를 입력받는다.
# [입력]
# 11021
# 2
# 3
# 4
# 5
# [출력]
# 15

sum = 0
for i in range(5):
    num = int(input())
    sum = sum + num

print(sum)
###########################
n=[]
for _ in range(5):
    n.append(int(input()))
print(sum(n))
