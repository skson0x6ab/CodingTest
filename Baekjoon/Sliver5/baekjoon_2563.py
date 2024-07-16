# 하얀 도화지 선언 -> 횐색: 0, 검정색: 1
canvas_array = []
for i in range(100):
   canvas_row = [None] * 100
   canvas_array.append(canvas_row)

# 색종이 수 입력
n = int(input().strip())

# 색종이 1로 칠하기
for i in range(n):
   input_value = input().split()
   for j in range(10):
      tmp_row = int(input_value[0]) + j
      for k in range(10):
         tmp_col = int(input_value[1]) + k
         if tmp_col > 100 or tmp_row > 100:
            break
         canvas_array[tmp_row][tmp_col] = 1

# 1갯수 구하기
total_sum = 0
for i in canvas_array:
   for j in i:
      if j is not None:
         total_sum = total_sum + 1

print(total_sum)




