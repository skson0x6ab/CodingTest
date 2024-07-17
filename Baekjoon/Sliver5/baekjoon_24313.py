#입력
num_a = input().split()
num_c = int(input())
num_n0 = int(input())

#결과 출력
if int(num_a[0]) * num_n0 + int(num_a[1]) > num_c * num_n0 or int(num_a[0]) * 100 + int(num_a[1]) > num_c * 100 :
   print(0)
else:
   print(1)