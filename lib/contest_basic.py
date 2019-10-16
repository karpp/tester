import requests
import re
from typing import List

from lib.test import Test


test_re = re.compile('<pre>([\s\S]*?)<\/pre>[\s\S]*?<pre>([\s\S]*?)<\/pre>')


def load_tests(contest: str, problem: str, cookies: dict) -> List[Test]:
    session = requests.Session()
    for name, val in cookies.items():
        session.cookies.set(name, val)

    page = session.get(f'https://official.contest.yandex.ru/contest/{contest}/problems/{problem}').text

    return [Test(input_text, output_text) for input_text, output_text
            in re.findall(test_re, page)]
