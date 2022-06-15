from time import sleep

if __name__ == '__main__':
    item = 0
    while item not in range(1, 101):
        item = int(input('Введите номер предмета от 1 до 100 включительно: '))
    sleep(1)

    print('Вероятно, этот предмет синий.')