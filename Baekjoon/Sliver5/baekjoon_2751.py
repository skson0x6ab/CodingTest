# 입력
import sys
n = int(sys.stdin.readline())

array_list = []

for i in range(n):
   tmp = int(sys.stdin.readline())
   array_list.append(tmp)

array_list.sort()

for i in array_list:
   print(i)


