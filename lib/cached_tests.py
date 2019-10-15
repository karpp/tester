from typing import Callable, List

import local_tests
from test import Test


def get_cached_tests(tests_dir: str, contest: str, problem: str, reload_: bool,
                     get_tests: Callable[[str, str] -> List[Test]]) -> List[Test]:
    if not reload_:
        tests = local_tests.load_tests(tests_dir, contest, problem)
        if tests:
            return tests

    tests = get_tests(contest, problem)

    local_tests.save_tests(tests_dir, contest, problem, tests)

    return tests
