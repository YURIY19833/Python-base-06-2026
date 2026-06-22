numbers = [1, 2, 3, 4, 5]
print(len(numbers))
for num in numbers:
    print(num)
    print('-------------')

arrNumbers = [27, 56, 12, 2, 88, 67, 10, 8, 11, 55]
counter = 0
for num in arrNumbers:
    if num % 2 == 0:
        counter = counter + 1
print(counter)
print('-------------')

list = [45, 8, 7, 48, 13]
total = 0
for num in list:
    total = total + num
print(total)

students = {
    'Олег': 5,
    'Катерина': 3,
    'Іванка': 6,
    'Ілона': 0,
    'Максим': 5
}
for student in students:
    print(f"Ім'я: {student}, Пропусків: {students[student]}")
