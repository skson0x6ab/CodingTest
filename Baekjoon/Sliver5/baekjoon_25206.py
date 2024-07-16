
#n = int(input().strip())
def grade_to_gpa(grade):
   gpa_map = {
      'A+': 4.5,
      'A0': 4.0,
      'B+': 3.5,
      'B0': 3.0,
      'C+': 2.5,
      'C0': 2.0,
      'D+': 1.5,
      'D0': 1.0,
      'F': 0.0
   }
   return gpa_map.get(grade, 0.0)

n = 20
ArrayValue = 0.0
sum_of_grades = 0.0
for i in range(n):
   TmpArray = input().split()
   if TmpArray[2] == 'P':
      pass
   else:
      ArrayValue = ArrayValue + float(TmpArray[1]) * float(grade_to_gpa(TmpArray[2]))
      sum_of_grades = sum_of_grades + float(TmpArray[1])
print(ArrayValue / sum_of_grades)



