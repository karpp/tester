import subprocess
import sys
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
        duration = time() - start_time

    except subprocess.TimeoutExpired:
        return Result(f'TL {time_limit:.2f}s', time_limit)

    if res.returncode != 0:
        return Result('RE\n' + res.stderr.decode('utf-8'), duration)
    
    output_text = res.stdout.decode('utf-8').strip()

    if output_text == test.output_text:
        return Result('', duration)

    return Result(f'WA\nGot:\n{output_text}', duration)
