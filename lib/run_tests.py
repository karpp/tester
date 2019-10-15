from typing import List

from lib.test import Test
from lib.run_test import run_test, Result


def run_tests(target: str, tests: List[Test], time_limit: float, label: True) -> bool:
    for i, test in enumerate(tests):
        result = run_test(target, test, time_limit)

        print(f'{label} {i + 1}) {"FAIL" if result.error_str else "OK"}, {result.duration:.3f}s')

        if result.error_str:
            print(f'{result.error_str}\nInput:\n{test.input_text}\nExpected:\n{test.output_text}')
            return False

    return True
