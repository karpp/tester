import sys
import subprocess
from dataclasses import dataclass
from time import time

from lib import local_tests, google_sheet_tests
from lib.run_tests import run_tests


def print_result(text):
    w = len(text) + 6
    print(f'╔{"═" * w}╗\n║{" " * w}║\n║   {text}   ║\n║{" " * w}║\n╚{"═" * w}╝')


def run_all(target, time_limit, manual_tests_dir, google_sheet_url, contest, problem):
    if manual_tests_dir:
        tests = local_tests.load_tests(manual_tests_dir, contest, problem)

        if not run_tests(target, tests, time_limit, 'Manual'):
            print_result('FAIL')
            return 
        
    if google_sheet_url:
        tests = google_sheet_tests.load_tests(google_sheet_url, contest, problem)

        if not run_tests(target, tests, time_limit, 'GoogleSheets'):
            print_result('FAIL')
            return

    print_result('OK')
