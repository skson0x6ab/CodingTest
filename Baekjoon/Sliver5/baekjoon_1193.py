## 등차수열 응용 문제 같음
## 짝수는 분모가 큰거부터, 홀수는 분자가 큰거부터 시작
# 입력
n = int(input().strip())

# 등차수열합, 공차, 초항, 마지막항, 이전 등차수열합 = 변수선언
arithmetic_sequence = 0
common_difference = 1
first_term = 1
last_term = 1
arithmetic_sequence_previous = 0
# 대략적인 위치 예측
while True:
   arithmetic_sequence = arithmetic_sequence + common_difference + last_term - 1
   if n <= arithmetic_sequence:
      break
   last_term = last_term + 1
   arithmetic_sequence_previous = arithmetic_sequence

# 정확한 위치 검색
if last_term % 2 == 0:
   numerator = 1
   denominator = last_term
   print(f'{numerator + n - arithmetic_sequence_previous - 1}/{denominator - (n - arithmetic_sequence_previous - 1)}')
else:
   numerator = last_term
   denominator = 1
   print(f'{numerator - (n - arithmetic_sequence_previous - 1)}/{denominator + (n - arithmetic_sequence_previous - 1)}')


