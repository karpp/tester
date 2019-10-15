import sys
import subprocess
from dataclasses import dataclass
from time import time
from testing.checker import check
from testing.tests import Test


@dataclass
class Result:
    error_str: str,
    duration: float


def run_tests(target: str, tests: List[Test], time_limit: float, label: True) -> bool:
    for i, test in enumerate(tests):
        result = get_result(target, test, time_limit)

        print(f'{label} {i + 1}) {"FAIL" if result.error_str else "OK"}, {result.duration:.3f}s')

        if result.error_str:
            print(f'Input:\n{test.input_text}\nExpected:\n{test.output_text}\n\n{result.error_str}')
            return False

    return True


def get_result(target: str, test: Test, time_limit: float) -> Result:
    try:
        start_time = time()
        res = subprocess.run(
            [sys.executable, target],
            input=test.input_text.strip().encode(),
            timeout=time_limit,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        total_time = time() - start_time

    except subprocess.TimeoutExpired:
        return Result(f'TL {time_limit:.2f}s', time_limit)

    result = res.stdout.decode('utf-8').strip()

    if res.returncode != 0:
        return Result('RE\n' + res.stderr.decode('utf-8'), total_time)

    elif check(result, test.output_text):
        return Result('', total_time)

    return Result(f'WA\n{result}', total_time)
