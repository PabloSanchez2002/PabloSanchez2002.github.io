---
layout: default
---

# Web Development using Django and Python for backend framework in Computer Systems Proyect class.

Django is a popular web framework for building web applications in Python. It is known for its flexibility, scalability, and security. With Django, you can create web services that handle requests and serve responses, making it an ideal platform for building APIs.

Here are the steps to deploy a web service on Django:

1. Set up a virtual environment for your project.This is a good practice to keep your project dependencies separate from your system dependencies. We used python3.9 for some compatibility reasons with the other lybraries we used.

2. Install Django using pip. You can do this by running the following command in your terminal:

    ```console
    $ pip install Django
    ```

3. Create a new Django project using the following command:

    ```console
    $ django-admin startproject myproject
    ```

3. Replace myproject with the name of your project.

    💡 Create a new Django app within your project. An app is a module that does something specific. You can create an app using the following command:

    ```python 
    manage.py startapp myapp
    ```

4. Replace myapp with the name of your app.

5. Define your app's views. A view is a Python function that takes a web request and returns a web response. You can define your views in the views.py file within your app.

6. Define your app's URLs. A URL is a Python string that maps to a view. You can define your app's URLs in the urls.py file within your app.

7.  Run the Django development server to test your web service. You can do this by running the following command:

    ```console
    python manage.py runserver
    ```

    This will start the server on http://127.0.0.1:8000/.
    You can specify the port in which the server runs by passing the port number as an argument to the runserver command. For example, to run the server on port 8080, you can run the following command:

     ```console
      python manage.py runserver 8080
      ```


8. Deploy your web service to a production server. There are many ways to do this, but a popular method is to use a web server like Apache or Nginx as a reverse proxy to forward requests to your Django application.

That's it! With these steps, you can create and deploy a web service on Django. Of course, there is much more to learn about Django, but this should be enough to get you started.

[/back](./)
