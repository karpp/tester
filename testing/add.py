from tests import Test


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
