from lib.google_sheet_tests import COMMON_192_2_URL
from lib.run_all import run_all


if __name__ == '__main__':
    run_all(
        target='./main.py',
        manual_tests_dir='./manual_tests',
        time_limit=2.0,
        google_sheet_url=COMMON_192_2_URL,
        contest='10',
        problem='J'
    )
