import sys
import subprocess
from dataclasses import dataclass
from time import time
from lib.checker import check
from lib.download import iter_tests
from lib.local_tests import load_local_tests
from lib import cached_tests
from lib.tests import Test
from lib.run_tests import run_tests as run_tests_general


def print_result(text):
    w = len(text) + 6
    print(f'╔{"═" * w}╗\n║{" " * w}║\n║   {text}   ║\n║{" " * w}║\n╚{"═" * w}╝')


def run_all(target, time_limit, manual_tests_dir, google_sheets_url, contest, problem):
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
