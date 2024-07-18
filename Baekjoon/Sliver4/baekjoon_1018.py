## 브루투포스 알고리즘?? 이거 경우의 수 다 해보는거 아닌가...
def compare_8x8_tables(def_chess_array_parameter, def_chess_array_white, def_chess_array_black):
   def_count_white = 0
   def_count_black = 0
   for i in range(8):
      for def_char_main, def_char_w, def_char_b in zip(def_chess_array_parameter[i],def_chess_array_white[i],def_chess_array_black[i]):
         if def_char_main != def_char_w:
            def_count_white += 1
         if def_char_main != def_char_b:
            def_count_black += 1

   if def_count_white <= def_count_black:
      return def_count_white
   else:
      return def_count_black

# 입력
n = input().split()
chess_array = []
chess_array_white = []
chess_array_black = []
answer_candidate = 64
for i in range(int(n[0])):
   input_value = input()
   chess_array.append(input_value)

for i in range(4):
   chess_array_white.append('WBWBWBWB')
   chess_array_white.append('BWBWBWBW')
   chess_array_black.append('BWBWBWBW')
   chess_array_black.append('WBWBWBWB')

for i in range(int(n[0])-7):
   for j in range(int(n[1])-7):
      tmp_array = []
      for k in range(8):
         tmp_array.append(chess_array[k+i][j:j+8])
      answer_candidate_tmp = compare_8x8_tables(tmp_array, chess_array_white, chess_array_black)
      if answer_candidate > answer_candidate_tmp:
         answer_candidate = answer_candidate_tmp

print(answer_candidate)


