import os
import sys
import subprocess
from time import time
from checker import check
from test_config import target, tests, time_limit, print_failed_tests


TESTS_FILE = open(tests, 'r')
ALL_TESTS = TESTS_FILE.read().split('===')
ALL_TESTS = [test for test in ALL_TESTS if test != '']
TESTS_FILE.close()
cnt = 0

for test in ALL_TESTS:
    print('Case {}:'.format(cnt), end=' ')
    cnt = cnt + 1

    test = test.split('\n\n')
    test[0] = test[0].strip()
    test[1] = test[1].strip()

    start_time = time()

    try:
        start_time = time()
        res = subprocess.run(
            [sys.executable, target],
            input=test[0].strip().encode(),
            timeout=time_limit,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        end_time = time()
        total_time = end_time - start_time

    except subprocess.TimeoutExpired:
        print('TL ({:.2f}s)'.format(time() - start_time))

        if print_failed_tests:
            print('Test:')
            print(test[0])

        continue

    result = res.stdout.decode('utf-8').strip()

    if res.returncode != 0:
        print('RE')
        print(res.stderr.decode('utf-8'))
        if print_failed_tests:
            print('Test:')
            print(test[0])

    elif check(result, test[1]):
        print('OK ({:.2f}s)'.format(total_time))

    else:
        print('WA ({:.2f}s)'.format(total_time))
        if print_failed_tests:
            print('Test:')
            print(test[0])
            print('Expected:')
            print(test[1].strip())
            print('Found:')
            print(result)

