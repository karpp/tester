import os
from typing import List

from texts import Test


def load_tests(tests_dir: str, contest: str, problem: str) -> List[Test]:
    filename = _get_filename(tests_dir, contest, problem)
    
    try:
        with open(filename, 'r') as in_:
            return [_text_to_test(chunk) for chunk in in_.read.split('===') if chunk.strip()]
    except FileNotFoundError:
        return []
        
    
def save_tests(tests_dir: str, contest: str, problem: str, tests: List[Test]) -> None:
    filename = _get_filename(tests_dir, contest, problem)

    os.makedirs(os.path.basename(filename), exist_ok=True)

    with open(filename, 'w') as out:
        for test in tests:
            out.write(_test_to_text(test))
            out.write('\n===')


def _get_filename(tests_dir: str, contest: str, problem: str):
    return os.path.join(tests_dir, f'tests.{contest}.{problem}.txt')


def _text_to_test(text: str) -> Test:
    input_text, output_text = text.split('\n\n')

    return Test(intput_text=intput_text, output_text=output_text)


def _test_to_text(test: Test) -> str:
    return f'{test.input_text}\n\n{test.output_text}'
