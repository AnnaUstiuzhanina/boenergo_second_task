### Второе задание

Есть группа из 100 предметов. Предметы могут быть синего, зелёного и красного цвета. Известно, что предметов синего цвета сильно больше, чем предметов зелёного цвета, а предметов зелёного цвета немного больше, чем предметов красного цвета. Напишите сервис, который будет принимать номер предмета и пытаться угадать его цвет. Логику работы сервиса определите самостоятельно.

#### Начать работу:
Для запуска приложения введите в консоли `python3 main.py` из соотвествующей директории.
Далее следуйте инструкциям.

**ИЛИ**

Для запуска сервиса введите в консоли `uvicorn service:app --reload` из соотвествующей директории.
Далее следуйте инструкциям.


#### Пояснение:
Так как условия задачи "сильно больше" и "немного больше" не конкретны, наверняка известно лишь следующее:
**синие > зеленые > красные**

Порядковое расположение предметов не определено, соотвественно, независимо от номера предмета, сервис будет отдавать в ответ статистически наиболее вероятный цвет предмета (синий).
