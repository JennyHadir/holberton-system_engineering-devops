#!/usr/bin/python3
""" Returns information about the todo list of a given employee
 id from a givent API """
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
    total_tasks = len(todo_dict)
    completed_tasks = []
    for task in todo_dict:
        if task['completed']:
            completed_tasks.append(task)
    print('Employee {} is done with tasks({}/{}):'.format(
            users_dict[0].get('name'), len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print('\t {}'.format(task.get('title')))
