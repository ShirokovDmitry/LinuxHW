# Задание 2. (повышенной сложности)
#
# Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный
# режим работы, в котором вывод разбивается на слова с удалением всех знаков пунктуации
# (их можно взять из списка string.punctuation модуля string). В этом режиме должно проверяться наличие слова в выводе.
import subprocess
import string


def check_command_output(command, text, mode='default'):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    out = result.stdout

    if result.returncode == 0:
        if mode == 'default':
            return 'True' if text in out else 'False'
        elif mode == 'word':
            out_without_punctuation = ''.join(char for char in out if char not in string.punctuation)
            words = out_without_punctuation.split()
            return words
        else:
            return 'Invalid mode'
    else:
        return 'False'


if __name__ == "__main__":
    command = "cat /etc/os-release"
    text = "22.04.2"
    mode = 'word'
    output = check_command_output(command, text, mode)
    if isinstance(output, list):
        for word in output:
            print(word)
    else:
        print(output)