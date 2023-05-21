from django.shortcuts import render
from django.http import Http404
import json
import os

def dataFromJson(request):


    directory = os.getcwd()

    print(directory)
    with open("bar_tasks/assets/bar_task.json") as file:
        data = json.load(file)
        bar_tasks = []

    # Extract tasks from different sections of the JSON object
        for section_data in data:
            section_name = section_data['section']
            tasks = section_data['tasks']
            bar_tasks.append({'section': section_name, 'tasks': tasks})
    
    return render(request, "bar_tasks.html", context={'bar_tasks': bar_tasks})




