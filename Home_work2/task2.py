# *Задание 2. *
#
# • Установить пакет для расчёта crc32
# sudo apt install libarchive-zip-perl
# • Доработать проект, добавив тест команды расчёта хеша (h).
# Проверить, что хеш совпадает с рассчитанным командой crc32.

import subprocess
import zlib
out = "/home/linux/out"


def calculate_file_hash(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
        return zlib.crc32(content)


def test_step7():
    # Рассчитываем хеш файла arx2.7z
    expected_hash = calculate_file_hash("{}/arx2.7z".format(out))

    # Получаем хеш файла командой crc32
    output = subprocess.check_output("cd {}; crc32 arx2.7z".format(out), shell=True, encoding='utf-8')
    actual_hash = int(output.strip(), 16)
    # print(f"\nHash = {actual_hash}")
    # print(f"Hash_ex = {expected_hash}")
    assert expected_hash == actual_hash, "test6 FAIL with hash: {}".format(actual_hash)
