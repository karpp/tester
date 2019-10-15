import argparse

from lib.local_tests import save_tests, load_tests
from lib.test import Test


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manual-tests-dir', '-m', './manual_tests')
    parser.add_argument('--contest', '-c', required=True)
    parser.add_argument('--problem', '-p', required=True)

    return parser.parse_args()


def add_manual_test(manual_tests_dir, contest, problem):
    pass


def main():
    args = parse_args()

    add_manual_test(args.manual_tests_dir, args.contest, args.problem)


def input_test() -> Test:
    print('Введите тест. Когда тест закончится, введите пустую строку.')
    input_text = ''
    s = input()
    while s:
        input_text += s + '\n'
        s = input()

    output_text = ''
    print('Введите ответ. Когда ответ закончится, введите пустую строку.')
    s = input()
    while s:
        output_text += s + '\n'
        s = input()

    return Test(input_text=input_text, output_text=output_text)


def input_tests() -> List[Test]:
    tests = []
    while True:
        tests.append(input_test())
            
        cont = input('Вы хотите добавить еще? (y/n): ')
        if cont.lower() == 'n':
            break

    print('Спасибо, что пользуетесь тестилкой!')
    
    return tests


if __name__ == '__main__':
    main()
