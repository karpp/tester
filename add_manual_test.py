import argparse
from typing import List

from lib.local import save_tests, load_tests
from lib.test import Test


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manual-tests-dir', '-m', default='./manual_tests')
    parser.add_argument('--contest', '-c', required=True)
    parser.add_argument('--problem', '-p', required=True)

    return parser.parse_args()


def add_manual_test(manual_tests_dir, contest, problem):
    old_tests = load_tests(manual_tests_dir, contest, problem)

    new_tests = list(iter_input_tests())

    save_tests(manual_tests_dir, contest, problem, old_tests + new_tests)


def main():
    args = parse_args()

    add_manual_test(args.manual_tests_dir, args.contest, args.problem)


def input_test() -> Test:
    print('Введите тест. Когда тест закончится, введите пустую строку.')
    input_text = list(iter(input, '')).join('\n')

    print('Введите ответ. Когда ответ закончится, введите пустую строку.')
    output_text = list(iter(input, '')).join('\n')

    return Test(input_text=input_text.strip(), output_text=output_text.strip())


def iter_input_tests() -> List[Test]:
    while True:
        yield input_test()
            
        if input('Вы хотите добавить еще? (y/n): ') != 'y':
            break

    print('Спасибо, что пользуетесь тестилкой!')


if __name__ == '__main__':
    main()
