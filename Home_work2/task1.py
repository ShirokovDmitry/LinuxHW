# Задание 1.
#
# Условие:
# Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).

import subprocess

out = "/home/linux/out"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step6():
    # Выводим список файлов в архиве
    assert checkout("cd {}; 7z l arx2.7z".format(out), "test1"), "test6 FAIL"


def test_step7():
    # Разархивируем архив с указанием путей и проверяем наличие файла test1 в папке folder2
    assert checkout("cd {}; 7z x {}/arx2.7z -o{}".format(out, out, out), "Everything is Ok"), "test7 FAIL"
