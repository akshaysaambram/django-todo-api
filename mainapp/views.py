import requests
from django.shortcuts import render, redirect

from .forms import TodoForm

# Create your views here.
def index(request):
    api = 'http://127.0.0.1:8000/api/todos/'
    response = requests.get(api)

    # todo = None
    # Check the response status code to see if the request was successful (HTTP 200 OK)
    if response.status_code == 200:
        todos = response.json()  # Convert the response JSON data to a Python dictionary
    else:
        print(f"Failed to retrieve todos. Status code: {response.status_code}")

    context = {
        'todos': todos,
    }
    return render(request, 'mainapp/index.html', context)


def create(request):
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
                    # Convert form data to JSON
        if form.is_valid():
            todo_data = {
                'title': form.cleaned_data['title'],
                'description': form.cleaned_data['description'],
                'completed': form.cleaned_data['completed'],
            }

            # API endpoint for creating todos
            api = 'http://127.0.0.1:8000/api/todos/create/'

            # Headers with content-type set to application/json
            headers = {
                'Content-Type': 'application/json',
            }

            # Send the POST request with JSON data
            response = requests.post(api, json=todo_data, headers=headers)

            if response.status_code == 201:
                # Todo item created successfully
                # You can add code here to handle the successful response, if needed.
                return redirect('index')
            else:
                # Failed to create todo item
                # You can add code here to handle the failed response, if needed.
                return render(request, '404.html')

    context = {
        'form': form,
    }
    return render(request, 'mainapp/create.html', context)


def detail(request, pk):
    api = f'http://127.0.0.1:8000/api/todos/{pk}/'
    response = requests.get(api)

    # todo = None
    # Check the response status code to see if the request was successful (HTTP 200 OK)
    if response.status_code == 200:
        todo = response.json()  # Convert the response JSON data to a Python dictionary
    else:
        print(f"Failed to retrieve todos. Status code: {response.status_code}")

    context = {
        'todo': todo,
    }
    return render(request, 'mainapp/detail.html', context)


def update_view(request, pk):
    # API endpoint for retrieving a specific todo
    api = f'http://127.0.0.1:8000/api/todos/{pk}/'

    # Send a GET request to the API to retrieve the todo's data
    response = requests.get(api)

    if response.status_code == 200:
        # Convert the response JSON data to a Python dictionary
        todo_data = response.json()

        # Create a TodoForm instance with the retrieved Todo data
        form = TodoForm(data=todo_data)

        if request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():
                # Convert the form data to JSON
                updated_todo_data = {
                    'title': form.cleaned_data['title'],
                    'description': form.cleaned_data['description'],
                    'completed': form.cleaned_data['completed'],
                }

                # API endpoint for updating todos
                update_api = f'http://127.0.0.1:8000/api/todos/{pk}/'

                # Headers with content-type set to application/json
                headers = {
                    'Content-Type': 'application/json',
                }

                # Send the PUT request with JSON data
                update_response = requests.put(update_api, json=updated_todo_data, headers=headers)

                if update_response.status_code == 200:
                    # Todo item updated successfully
                    # You can add code here to handle the successful response, if needed.
                    return redirect('index')
                else:
                    # Failed to update todo item
                    # You can add code here to handle the failed response, if needed.
                    return render(request, '404.html')

        return render(request, 'mainapp/create.html', {'form': form})
    else:
        # Handle the case when the API request to retrieve the todo item fails
        return render(request, '404.html')

def delete_view(request, pk):
    # API endpoint for deleting a specific todo
    api = f'http://127.0.0.1:8000/api/todos/{pk}/'

    # Send the DELETE request
    response = requests.delete(api)
    if response.status_code == 204:
        # Todo item deleted successfully
        # You can add code here to handle the successful response, if needed.
        return redirect('index')
    else:
        # Failed to delete todo item
        # You can add code here to handle the failed response, if needed.
        return render(request, '404.html')