# 입력
input_value = input()
list_value = list(map(int, list(input_value)))
list_value.sort(reverse=True)

answer = ""
for i in list_value:
   answer += str(i)

print(answer)


