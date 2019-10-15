import os
from typing import List

from texts import Test


def load_local_tests(tests_dir: str, contest: str, problem: str) -> List[Test]:
    filename = get_filename(tests_dir, contest, problem)
    
    try:
        with open(filename, 'r') as in_:
            return [text_to_test(chunk) for chunk in in_.read.split('===') if chunk.strip()]
    except FileNotFoundError:
        return []
        
    
def save_local_tests(tests_dir: str, contest: str, problem: str, tests: List[Test]) -> None:
    filename = get_filename(tests_dir, contest, problem)

    os.makedirs(os.path.basename(filename), exist_ok=True)

    with open(filename, 'w') as out:
        for test in tests:
            out.write(test_to_text(test))
            out.write('\n===')


def get_filename(tests_dir: str, contest: str, problem: str):
    return os.path.join(tests_dir, f'tests.{contest}.{problem}.txt')


def text_to_test(text: str) -> Test:
    input_text, output_text = text.split('\n\n')

    return Test(intput_text=intput_text, output_text=output_text)


def test_to_text(test: Test) -> str:
    return f'{test.input_text}\n\n{test.output_text}'
