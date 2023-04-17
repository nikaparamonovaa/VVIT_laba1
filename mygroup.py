groupmates = [
    {
        "name": "Артемий",
        "surname": "Бобков",
        "exams": ["ВВиТ", "Вышмат", "Философия"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Владислав",
        "surname": "Хорунжий",
        "exams": ["ВВиТ", "Вышмат", "Философия"],
        "marks": [4, 5, 3]
    },
    {
        "name": "Дмитрий",
        "surname": "Ясинский",
        "exams": ["ВВиТ", "Вышмат", "Философия"],
        "marks": [4, 5, 3]
    },
    {
        "name": "Артём",
        "surname": "Лаврюк",
        "exams": ["ВВиТ", "Вышмат", "Философия"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Али",
        "surname": "Калбаев",
        "exams": ["ВВиТ", "Вышмат", "Философия"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Дмитрий",
        "surname": "Изюмин",
        "exams": ["ВВиТ", "Вышмат", "Философия"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Андрей",
        "surname": "Лудин",
        "exams": ["ВВиТ", "Вышмат", "Философия"],
        "marks": [3, 4, 3]
    }
]
def students(stud):
    print("Введите среднюю оценку")
    needScore = float(input())
    needStudents = []
    for i in range(len(stud)):
        studScore = stud[i]['marks']
        summary = sum(studScore)
        middleScoreStud = summary / len(stud[i]['marks'])
        if middleScoreStud > needScore:
            needStudents.append(stud[i])
    print(needStudents, end = '\n')

students(groupmates)
