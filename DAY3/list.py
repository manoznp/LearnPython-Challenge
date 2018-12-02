#list

names = ['raju', 'manoj']
length_names = len(names)
print("Length of the array name is {}".format(length_names))

names.append("saroj")
length_names = len(names)
print("Length of the array name is {}".format(length_names))

print(names)

names.insert(1, "sudeep")
print("After inserting sudeep at position second: {}".format(names))

for name in names:
    print(name)

# extending the list
other_names = ['dipesh', 'pankaj', 'prmaod']
names.extend(other_names)
print(names)

# Dictionary
student = {'name':'manoz',
			        'time':'1.5 hrs',
			        'course': 'Data Science',
			        'fee': 25000,
			        'hasVeichle': False
			}

# print the value of the dictionary with key
print(student['course'])

student_all_key = student.keys()
print(student_all_key)

student_all_value = student.values()
print(student_all_value)


# iterate in the dictionary
for key in student.keys():
	print("{} : {}".format(key, student[key]))

# change the value of the dictionary
student['course'] = 'Advanced Java'
print(student)

# lets add the key that doesnot exist in the dictionary student
student['gender'] = "male"

print("after adding gender")
print(student)

# delete the key course
del(student['course'])
# after deleting the key course
print(student)

# convert the student to list
student = list(student)
# after converting to the list
print(student)

# check the key is exist in the dictionary or not
isCourseExists = "courses" in student
print("course exists in student  : {} ". format(isCourseExists))

