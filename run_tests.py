import argparse

from lib.google_sheet import COMMON_192_2_URL
from lib.run_all import run_all


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manual-tests-dir', '-m', default='./manual_tests')
    parser.add_argument('--google-sheet-url', '-g', default=COMMON_192_2_URL)
    parser.add_argument('--contest', '-c', required=True)
    parser.add_argument('--problem', '-p', required=True)
    parser.add_argument('--target', '-t', default='./main.py')
    parser.add_argument('--time-limit', '-l', type=float, default=2.0)

    return parser.parse_args()


def main():
    args = parse_args()

    run_all(
        target=args.target,
        manual_tests_dir=args.manual_tests_dir,
        google_sheet_url=args.google_sheet_url,
        contest=args.contest,
        problem=args.problem,
        time_limit=args.time_limit
    )


if __name__ == '__main__':
    main()
