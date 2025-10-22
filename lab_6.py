# Створення та управління словником студентів
from sort import sort_by_name

students = {
    "student1": {
        "first_name": "Viktor",
        "last_name": "Afanasenko",
        "course": 2,
        "grades": {"Python": 4, "Numerical Methods": 4, "elective course": 5}
    },
    "student2": {
        "first_name": "Roman",  # коригування назви
        "last_name": "Fedorchenko",
        "course": 2,
        "grades": {"Python": 5, "Numerical Methods": 5, "elective course": 3}
    },
    "student3": {
        "first_name": "Mariyana",
        "last_name": "Bobro",
        "course": 2,
        "grades": {"Python": 4, "Numerical Methods": 5, "elective course": 5}
    }
}
# Виведення початкового словника студентів
def show() : 
 print("\nСловник студентів та їх оцінок:")
 for key, value in students.items():
    print(f"{key}: {value}")
# Функція Афанасенка В.Ю.
# Функція додавання нових студентів
def add ():
 n = int(input("Скільки студентів ви хочете додати? "))
 for i in range(1, n + 1):
    key = f"student{i + 3}"  # виправлено проблему з пробілом у ключі
    students[key] = {}

    name = input(f"\nВведіть ім'я для {key}: ")
    students[key]["first_name"] = name
    last_name = input(f"\nВведіть прізвище для {key}: ")
    students[key]["last_name"] = last_name
    course = input("\nВведіть курс студента: ")
    students[key]["course"] = course
    students[key]["grades"] = {}

    m = int(input(f"Скільки предметів у {name}? "))
    for _ in range(m):
        subject = input("Введіть назву предмета: ")
        grade = int(input("Введіть оцінку: "))
        students[key]["grades"][subject] = grade
        print("\nСловник студентів та їх оцінок:")
 for key, value in students.items():
    print(f"{key}: {value}")



def sortt():
# Виведення відсортованого словника
 print("\nВідсортований словник:")
 sorted_students = sort_by_name(students)
 for key, value in sorted_students.items():
    print(f"{key}: {value}")
def delete ():
 # Функція Бобро М.Г.
 # Функція для видалення студента зі словника
 def remove_student(students_dict):
    print("\nСписок студентів:")
    for key in students_dict.keys():
        print(f" - {key}") # Виводимо всі ключі студентів
    student_key = input("\nВведіть ключ студента, якого потрібно видалити (наприклад, student2): ")

    if student_key in students_dict: # Перевірка чи існує такий студент
        del students_dict[student_key] # Видаляємо студента зі словника
        print(f"Студента '{student_key}' успішно видалено.")
    else:
        print(f"Студента з ключем '{student_key}' не знайдено.")

 remove_student(students)

 #Виводимо оновлений словник студентів
 print("\nОновлений список студентів:")
 for key, value in students.items():
    print(f"{key}: {value}")
while True :
 x=int(input("1  Вивести словник  \n2 Додати елемент у словник  \n3  Видалити елемент зі словника  \n 4   Відсортувати словник  \n 5  Закрити програму  \n Виберіть дію (1-5):"))
 if x == 1 :
  show()
 elif x==2:
   add()
 elif x==3:
  delete ()
 elif x==4:
   sortt()
 elif x==5:
  break

