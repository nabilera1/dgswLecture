mydict = {}  # 빈 딕셔너리를 생성
for _ in range(2):  # 2회 반복만 시키기 위해 _ 사용
    key = input('가수명 입력 : ')
    value = input('가수에 대한 설명 입력 : ')
    mydict[key] = value
print(mydict)

name=input('좋아하는 K Pop 가수 이름을 적으시오 : ')
print(mydict[name])

# KPop={'BTS':'세계적인 한국의 보이밴드이다. 총 7명으로 구성되어 있다.',
#       '블랙핑크' : '세계적인 한국의 여성 아이돌 밴드이다. 총  4명으로 구성되어 있다.'}