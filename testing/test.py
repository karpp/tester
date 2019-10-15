import sys
import subprocess
from dataclasses import dataclass
from time import time
from testing.checker import check
from testing.download import iter_tests
from testing.local_tests import load_local_tests
from testing import cached_tests
from testing.tests import Test
from testing.run_tests import run_tests as run_tests_general


def print_result(text):
    w = len(text) + 6
    print(f'╔{"═" * w}╗\n║{" " * w}║\n║   {text}   ║\n║{" " * w}║\n╚{"═" * w}╝')


def test(target, time_limit, manual_tests_dir, google_sheets_url, contest, problem):
    if manual_tests_dir:
        manual_tests = load_local_tests(manual_tests_dir, contest, problem)

        if not run_tests(target, manual_tests, time_limit, 'Manual'):
            print_result('FAIL')
            return 
        
    if google_sheets_url:
        google_sheets_tests = list(iter_tests(google_sheets_url, contest, problem))

        if not run_tests(target, google_sheet_tests, time_limit, 'GoogleSheets'):
            print_result('FAIL')
            return

    print_result('OK')


def main():
    from run_tests import target, manual_tests_dir, time_limit, google_sheet_url, contest, problem

    test(target, time_limit, time_limit, google_sheet_url, contest, problem)


if __name__ == '__main__':
    main()
