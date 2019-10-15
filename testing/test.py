import sys
import subprocess
from time import time
from testing.checker import check
from testing.download import iter_tests
from testing.local_tests import load_local_tests
from testing.tests import Test


def test(target, manual_tests_dir, time_limit, print_failed_tests, use_online_tests,
         contest_num, task_name):
    cnt = 0
    if manual_tests_dir:
        all_tests = load_local_tests(manual_tests_dir, str(contest_num), task_name)

        for cur_test in all_tests:
            print('Case {}:'.format(cnt), end=' ')
            cnt = cnt + 1

            cur_test = cur_test.split('\n\n')
            cur_test[0] = cur_test[0].strip()
            cur_test[1] = cur_test[1].strip()

            start_time = time()

            try:
                start_time = time()
                res = subprocess.run(
                    [sys.executable, target],
                    input=cur_test[0].strip().encode(),
                    timeout=time_limit,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)
                end_time = time()
                total_time = end_time - start_time

            except subprocess.TimeoutExpired:
                print('TL ({:.2f}s)'.format(time() - start_time))

                if print_failed_tests:
                    print('Test:')
                    print(cur_test[0])
                    print()

                continue

            result = res.stdout.decode('utf-8').strip()

            if res.returncode != 0:
                print('RE')
                print(res.stderr.decode('utf-8'))
                if print_failed_tests:
                    print('Test:')
                    print(cur_test[0])

            elif check(result, cur_test[1]):
                print('OK ({:.2f}s)'.format(total_time))

            else:
                print('WA ({:.2f}s)'.format(total_time))
                if print_failed_tests:
                    print('Test:')
                    print(cur_test[0])
                    print('Expected:')
                    print(cur_test[1].strip())
                    print('Found:')
                    print(result)
            print()

    if use_online_tests:
        for cur_test in iter_tests(contest_num, task_name):
            print('Case {} (shared):'.format(cnt), end=' ')
            cnt = cnt + 1

            start_time = time()

            try:
                start_time = time()
                res = subprocess.run(
                    [sys.executable, target],
                    input=cur_test.input_text.strip().encode(),
                    timeout=time_limit,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)
                end_time = time()
                total_time = end_time - start_time

            except subprocess.TimeoutExpired:
                print('TL ({:.2f}s)'.format(time() - start_time))

                if print_failed_tests:
                    print('Test:')
                    print(cur_test.input_text)
                    print()

                continue

            result = res.stdout.decode('utf-8').strip()

            if res.returncode != 0:
                print('RE')
                print(res.stderr.decode('utf-8'))
                if print_failed_tests:
                    print('Test:')
                    print(cur_test.input_text)

            elif check(result, cur_test.output_text):
                print('OK ({:.2f}s)'.format(total_time))

            else:
                print('WA ({:.2f}s)'.format(total_time))
                if print_failed_tests:
                    print('Test:')
                    print(cur_test.input_text)
                    print('Expected:')
                    print(cur_test.output_text.strip())
                    print('Found:')
                    print(result)
            print()


def main():
    from run_tests import target, manual_tests_dir, time_limit, print_failed_tests, \
        use_online_tests, contest_num, task_name

    test(target, manual_tests_dir, time_limit, print_failed_tests,
         use_online_tests, contest_num, task_name)


if __name__ == '__main__':
    main()
