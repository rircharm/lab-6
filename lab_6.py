students = {
    "Віктор" : {
        
        "last_name" : "Афанасенко",
        "course" :  2,
        "grades": {" Python" : 4 , "Numerical Methods" : 4 , "elective course" : 5}
        } ,
    "Роман" : {
        "last_name" : "Федорченко",
        "course" :  2,
        "grades": {" Python" : 5 , "Numerical Methods" : 5, "elective course" : 3}
        },
    "Мар'яна" : {
        "last_name" : "Бобро",
        "course" :  2,
        "grades": {" Python" : 4 , "Numerical Methods" : 5 , "elective course" : 5}
        }
    }
print(" students:")
for key, value in  students.items():
    print(f"{key}: {value}")

n = int(input("Скільки студентів ви хочете додати? "))

for _ in range(n):
    name = input("\nВведіть ім'я студента: ")
    students[name] = {}  
    
    m = int(input(f"Скільки предметів у {name}? "))
    for _ in range(m):
        subject = input("Введіть назву предмета: ")
        grade = int(input("Введіть оцінку: "))
        students[name][subject] = grade

print("\nСловник студентів та їх оцінок:")
print(students)