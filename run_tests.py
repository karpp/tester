target = 'main.py'            # файл с решением
tests = 'tests.txt'           # файл с тестами
time_limit = 1.0              # ограничение по времени в секундах
print_failed_tests = True     # выводить ли непройденные тесты вместе с вердиктами
use_online_tests = True       # использовать ли общие тесты
use_offline_tests = True      # использовать ли тесты из файла tests
contest_num = '9'
task_name = 'K'

if __name__ == '__main__':
    from testing.test import test
    test(target, tests, time_limit, print_failed_tests,
         use_online_tests, use_offline_tests, contest_num, task_name)
