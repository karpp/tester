import csv
import io
import os
import requests

from lib.test import Test


COMMON_192_2_URL = 'https://docs.google.com/spreadsheets/d/1ExOQ7X76lQ13e4fmqxPo0i_vS0qDOhMKgpjeJzV6amc/export?format=csv&id=1ExOQ7X76lQ13e4fmqxPo0i_vS0qDOhMKgpjeJzV6amc&gid=1092659262'


def load_tests(url, contest, problem):
    return [Test(input_text, output_text) for 
            row_contest, row_problem, input_text, output_text, *_ in
            csv.reader(io.StringIO(requests.get(url).text))
            if row_contest == contest and row_problem == problem]
