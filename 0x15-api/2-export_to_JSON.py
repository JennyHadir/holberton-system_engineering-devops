#!/usr/bin/python3
""" Export data from task 0 in the Json format  """
import json
import requests
import sys
if __name__ == '__main__':
    employee_id = sys.argv[1]
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todo = requests.get(todo_url, params={'userId': employee_id})
    users = requests.get(users_url, params={'id': employee_id})
    todo_dict_list = todo.json()
    users_dict_list = users.json()
    task_list = []
    user_tasks = {}
    employee_username = users_dict_list[0].get('username')
    with open('{}.json'.format(employee_id), 'w', encoding='utf-8') as jsonfile:
        for task in todo_dict_list:
            status = task.get('completed')
            title = task.get('title')
            task_dict = {}
            task_dict['task'] = title
            task_dict['completed'] = status
            task_dict['username'] = employee_username
            task_list.append(task_dict)
        user_tasks[employee_id] = task_list
        json.dumps(user_tasks, jsonfile)
