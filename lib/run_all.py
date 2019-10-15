import subprocess
import sys

from lib import local, google_sheet
from lib.run_tests import run_tests


def print_result(text):
    w = len(text) + 6
    print(f'╔{"═" * w}╗\n║{" " * w}║\n║   {text}   ║\n║{" " * w}║\n╚{"═" * w}╝')


def run_all(target, time_limit, manual_tests_dir, google_sheet_url, contest, problem):
    label_tests_pairs = []

    if manual_tests_dir:
        label_tests_pairs.append((
            'Manual', 
            local.load_tests(manual_tests_dir, contest, problem)
        ))

    if google_sheet_url:
        label_tests_pairs.append((
            'GoogleSheet', 
            google_sheet.load_tests(google_sheet_url, contest, problem)
        ))

    for label, tests in label_tests_pairs:
        if not run_tests(target, tests, time_limit, label):
            print_result('FAIL')
            return

    print_result('OK')
