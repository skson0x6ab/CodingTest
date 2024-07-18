import sys

# 입력
n = input()
bag_5kg = int(int(n) / 5)
bag_3kg = int((int(n) - bag_5kg * 5 ) / 3)
if (int(n) - bag_5kg * 5) % 3 == 0:
   print(bag_5kg + bag_3kg)
   sys.exit()

for i in range(1, bag_5kg + 1):
   j = 0
   while (bag_5kg - i) * 5 + (bag_3kg + j) * 3 <= int(n):
      if (bag_5kg - i) * 5 + (bag_3kg + j) * 3 == int(n):
         print(bag_5kg - i + bag_3kg + j)
         sys.exit()
      j += 1

print(-1)





