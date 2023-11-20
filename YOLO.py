# Файл txt где числа
file = 'nums.txt'
# Открываем файл на чтение
with open(file, 'r') as f:
    #f.readlines() считывает все строки из файла и возвращает их в виде списка
    lines = f.readlines()
    numbers = []

    # цикла for line in lines перебирает каждую строку в списке lines
    for line in lines:
        # line.split() разбивает строку на список слов, используя пробелы в качестве разделителей
        words = line.split()

        # Вложенный цикл for word in words перебирает каждое слово в списке words
        for word in words:
            # Число представленное каждым словом преобразуется в целое число с помощью функции int() и добавляется в список numbers.
            # Проверка есть ли в файле букыв
            try:
                numbers.append(int(word))

            except:
                print(f"Error в {file} есть буквы")


#sum(numbers) суммирует все числа в списке numbers
_sum = sum(numbers)
#выводит общую сумму чисел
print(f'Сумма чисел: {_sum}')