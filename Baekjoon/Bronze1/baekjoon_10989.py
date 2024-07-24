# 입력
import sys
n = int(sys.stdin.readline())

my_dict = {}

for i in range(n):
   tmp = int(sys.stdin.readline())
   if tmp in my_dict:
      my_dict[tmp] += 1
   else:
      my_dict[tmp] = 1
sorted_items = sorted(my_dict.items())
for i in sorted_items:
    for j in range(i[1]):
        print(i[0])




