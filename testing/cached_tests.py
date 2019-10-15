from typing import Callable, List

from tests import Test
from local_tests import load_local_tests, save_local_tests


def get_cached_tests(tests_dir: str, contest: str, problem: str, reload_: bool,
                     get_tests: Callable[[str, str] -> List[Test]]) -> List[Test]:
    if not reload_:
        tests = load_local_tests(tests_dir, contest, problem)
        if tests:
            return tests

    tests = get_tests(contest, problem)

    save_local_tests(tests_dir, contest, problem, tests)

    return tests
