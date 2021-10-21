
# [문제] 리스트에 주어진 알파벳을 오름차순 정렬하라
# arr=['b','c','a','f','t','e'] # 배열, 리스트
# print(arr)
# #정렬
# arr.sort()
# # print(arr)
# 리스트 요소 중 아스키 코드값이 가장 작은 알파벳을 출력하시오.
# print(arr[0])
# print(len(arr)) #리스트의 길이 출력


# [문제]리스트 요소 중 아스키 코드값이 가장 큰 알파벳을 출력하시오.
arr = ['b', 'c', 'a', 'f', 't', 'e']
arr.sort()
print(arr[len(arr) - 1])


#또는 내림차순으로 처리
arr.sort(reverse=True) # 내림차순으로 정렬
print(arr[0])

print(arr[0]) #맨 앞 요소
print(arr[-1]) #맨 뒤 요소, 끝에서 첫번째


# [문제] :
# 아래 알파벳 리스트 중 가장 빨리 나오는 것과
# 마지막에 나오는 알파벳을 출력하시오.
# arr=['t','b','c','k','u','n']
# arr.sort(reverse=True) # arr.sort()
# print(arr)
# n=len(arr)-1
# print(arr[0],arr[n])
# print(arr[0],arr[len(arr)-1])

# [문제] 주어진 점수 리스트에서 최고점과 최저점을 출력하시오.
score=[55, 78, 99, 34, 87]
score.sort()
print(score[-1], score[0])  # 최고점, 최저점

# 1위 점수를 출력하시오.
# score.sort(reverse=True)
# print(score[0])
print(max(score)) # 최고점
print(min(score)) # 최저점


