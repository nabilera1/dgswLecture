li = []
li.append('BTS')
li.append('Black Pink')
print(li)  # ['BTS', 'Black Pink']
print(li[1])  # 값 출력, Black Pink


# 가수 세 명을 입력 받기
for _ in range(0, 3, 1): # for _ in range(3)
    li.append(input('가수 이름을 쓰세요 : '))

print('-' * 20)
print(li)
print(f'리스트 개수 {len(li)}개 입니다.')