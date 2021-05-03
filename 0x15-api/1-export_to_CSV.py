#!/usr/bin/python3
""" Export data from task 0 in the CSV format """
import csv
import requests
import sys
if __name__ == '__main__':
    employee_id = sys.argv[1]
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todo = requests.get(todo_url, params={'userId': employee_id})
    users = requests.get(users_url, params={'id': employee_id})
    todo_dict = todo.json()
    users_dict = users.json()
    employee = users_dict[0].get('username')
    with open('{}.csv'.format(employee_id), 'w', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo_dict:
            task_status = task['completed']
            task_title = task['title']
            csv_writer.writerow(["{}".format(employee_id),
                                 "{}".format(employee),
                                 "{}".format(task_status),
                                 "{}".format(task_title)])
