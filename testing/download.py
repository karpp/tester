import requests
import csv
import os

from tests import Test


DEFAULT_URL = 'https://docs.google.com/spreadsheets/d/1ExOQ7X76lQ13e4fmqxPo0i_vS0qDOhMKgpjeJzV6amc/export?format=csv&id=1ExOQ7X76lQ13e4fmqxPo0i_vS0qDOhMKgpjeJzV6amc&gid=1092659262'


def iter_tests(target_contest, target_problem):
    file = requests.get(DEFAULT_URL).text
    temp_csv = open('.temp.csv', 'w')
    temp_csv.write(file)
    temp_csv.close()
    temp_csv = open('.temp.csv', 'r')
    reader = csv.reader(temp_csv)
    for line in reader:
        if len(line) == 5:
            contest, problem, input_, output, timestamp = line
        else:
            contest, problem, input_, output = line

        if contest == target_contest and problem == target_problem:
            yield Test(input_text=input_, output_text=output)
    temp_csv.close()
    os.remove('.temp.csv')
