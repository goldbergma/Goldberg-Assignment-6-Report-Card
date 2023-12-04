################ Function Definitions ################


# Shows the user what options they have
def displayMenu():

  # This option will involve you adding a student and a collection for their
  # grades to a dictionary!
  print("1. Add Student")

  # This option will involve you removing a pair from a dictionary!
  print("2. Remove Student")

  # This option will require you to grab a student from a dictionary and add
  # a quiz grade to it's corresponding collection of grades!
  # You'll also need to use a pre-written function that ensures the user is
  # entering a valid grade (a decimal number)
  print("3. Add Student Quiz Grade")

  # This option will require you to use a loop to list all of the grades for
  # an INDIVIDUAL student!
  print("4. List Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade
  # as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  print("6. Quit Gradebook")


# Prompts the user to enter a numeric grade
# This function works, and ensures the user entered a valid float for the
# grade
# It's not important HOW this function works, but how to USE this function
def getNumberGradeFromUser():

  val = None

  while val is None:
    try:
      test = float(input("Enter a Number Grade: "))
      val = test
    except:
      val = None

  return val


def letter_grade_from_number(grade):
  if 90 <= grade:
    return 'A'
  elif 80 <= grade < 90:
    return 'B'
  elif 70 <= grade < 80:
    return 'C'
  elif 60 <= grade < 70:
    return 'D'
  else:
    return 'F'


################ Main Program ################

print ("Smith High School")
print ("Mr. Jones English Class")
print()
students = {}

displayMenu()
choice = input('Select an Option: ')

# Application Loop
while choice != '6':
  if choice == '1':
    name = input('Enter student name: ')
    students[name] = []
  elif choice == '2':
    name = input('Enter student name: ')
    if name in students:
      del students[name]
      print(f'{name} removed!')
    else:
      print(f'{name} is not in the gradebook!')
  elif choice == '3':
    name = input('Enter student name: ')
    if name in students:
      grade = getNumberGradeFromUser()
      students[name].append(grade)
    else:
      print(f'{name} is not in the gradebook!')
  elif choice == '4':
    name = input('Enter student name: ')
    if name in students:
      for grade in students[name]:
        print(grade)
    else:
      print(f'{name} is not in the gradebook!')

  elif choice == '5':
    name = input('Enter student name: ')
    if name in students:
      gpa = sum(students[name]) / len(students[name])
      letter = letter_grade_from_number(gpa)
      print(f'{name} has a grade of {letter}')
    else:
      print(f'{name} is not in the gradebook!')

  print()
  displayMenu()
  choice = input('Select an Option: ')

print('Gradebook is now closed')