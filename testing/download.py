import requests
import csv
import os


def iter_test_inputs_and_outputs(target_contest, target_problem):
    file = requests.get('https://docs.google.com/spreadsheets/d/1ExOQ7X76lQ13e4fmqxPo0i_vS0qDOhMKgpjeJzV6amc/export?format=csv&id=1ExOQ7X76lQ13e4fmqxPo0i_vS0qDOhMKgpjeJzV6amc&gid=1092659262').text
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
                yield input_, output
    temp_csv.close()
    os.remove('.temp.csv')


if __name__ == '__main__':
    contest_num = '10'
    task_name = 'J'
    test_file = open(contest_num + task_name + '.txt', 'w')
    for test in iter_test_inputs_and_outputs(contest_num, task_name):
        test_file.write(test[0] + '\n\n' + test[1] + '\n===\n')
