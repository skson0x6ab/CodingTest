# 점의 갯수 입력
n = int(input().strip())

#arraylist [], 딕셔너리 {}, 튜플 ()
array_List = []
num = 0
#값 입력
for i in range(n):
   num += 1
   input_value = input().split()
   array_List.append([int(input_value[0]), input_value[1], num])

# 오름차순 내열
array_List.sort(key=lambda x: (x[0], x[2]))

#출력
for i in array_List:
   print(f"{i[0]} {i[1]}")




