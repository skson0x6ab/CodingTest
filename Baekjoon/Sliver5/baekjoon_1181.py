# 점의 갯수 입력
n = int(input().strip())

#arraylist [], 딕셔너리 {}, 튜플 ()
array_List = []

#값 입력
for i in range(n):
   input_value = input()
   array_List.append(input_value)

#중복 제거
set_array_List = list(set(array_List))
# 오름차순 내열
set_array_List.sort(key=lambda x: (len(x), x))

#출력
for i in set_array_List:
   print(i)




