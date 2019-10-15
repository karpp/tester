from run_tests import tests
# tests = 'test.txt'
f = open(tests, 'a')

while True:
    print('Введите тест. Когда тест закончится, введите пустую строку.')
    test = ''
    s = input()
    while s:
        test += s + '\n'
        s = input()

    f.write(test)
    f.write('\n')

    ans = ''
    print('Введите ответ. Когда ответ закончится, введите пустую строку.')
    s = input()
    while s:
        ans += s + '\n'
        s = input()

    f.write(ans + '===\n')

    cont = input('Вы хотите добавить еще? (y/n): ')
    if cont.lower() == 'n':
        break

print('Спасибо, что пользуетесь тестилкой!')
