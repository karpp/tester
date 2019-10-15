import sys
import subprocess
from dataclasses import dataclass
from time import time

from lib.test import Test


@dataclass
class Result:
    error_str: str
    duration: float


def run_test(target: str, test: Test, time_limit: float) -> Result:
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

    elif result == test.output_text:
        return Result('', total_time)

    return Result(f'WA\nGot:\n{result}', total_time)
