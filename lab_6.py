students = {
    "student1" : {
        "first_name" : "Viktor",
        "last_name" : "Afanasenko",
        "course" :  2,
        "grades": {" Python" : 4 , "Numerical Methods" : 4 , "elective course" : 5}
        }  ,
    "student2" : {
        "first_name" : "Romar",
        "last_name" : "Fedorchenko",
        "course" :  2,
        "grades": {" Python" : 5 , "Numerical Methods" : 5, "elective course" : 3}
        },
    "student3" : {
        "first_name" : "Mariyana",
        "last_name" : "Bobro",
        "course" :  2,
        "grades": {" Python" : 4 , "Numerical Methods" : 5 , "elective course" : 5}
        }
    }
print(" students:")
for key, value in  students.items():
    print(f"{key}: {value}")
     
n = int(input("Скільки студентів ви хочете додати? "))

for i in range(1, n+1):
    key = f"student {i+3}"  
    students[key] = {}     
    
    name = input(f"\nВведіть ім'я для {key}: ")
    students[key]["first_name"] = name
    last_name = input(f"\nВведіть прізвище для {key}: ")
    students[key]["last_name"] = last_name
    course= input("\nВведіть курс студента : ")
    students[key][" course"] =  course
    students[key]["grades"] = {} 
    
    m = int(input(f"Скільки предметів у {name}? "))
    for _ in range(m):
        subject = input("Введіть назву предмета: ")
        grade = int(input("Введіть оцінку: "))
        students[key]["grades"][subject] = grade
print("\nСловник студентів та їх оцінок:")
print(students)