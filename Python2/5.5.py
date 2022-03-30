#Student lists
students_present = ["tommy", "dahlia", "manaia", "isaac", "jamila", "britt", "patrick", "jessika", "chantal", "rocio"]
students_absent = ["iliana", "olympia", "juan", "kelsey"]

#Sort the students present list and print
print("Students present: ")

students_present.sort()

for student in students_present:
  print(student.title())
  
#Sort the students absent list and print
print("Students absent: ")

students_absent.sort()
for student in students_absent:
  print(student.title())