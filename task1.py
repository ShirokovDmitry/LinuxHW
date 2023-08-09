# Задание 1.
#
# Условие:
# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе
# и False в противном случае. Передаваться должна только одна строка, разбиение вывода
# использовать не нужно.
import subprocess


def check_command_output(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    out = result.stdout
    if result.returncode == 0:
        if text in out:
            return 'True'
        else:
            return 'False'
    else:
        return 'False'


if __name__ == "__main__":
    command = "cat /etc/os-release"
    text = "22.04.2"
    print(check_command_output(command, text))