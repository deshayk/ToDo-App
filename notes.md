# Project Notes
## Description
I want to create an application that creates a To-Do list. The application has the following characteristics:
- When the application opens, the application verbally welcomes the user.
- (F-string) “Hello {name}, what do you need to do today?
- Asks user input what they want to name the todo list
- This initializes the creation of a new table within the To-Do App database
- The user verbally tells the application what it wants to do
- The application stores the to-do items in the list.
- The user can update the list by telling the application they just completed a list item.
- When the user updates the list, the application updates the to-do list by “crossing off” the completed list items
- When the user completes all of the items on the to-do list, the application verbally congratulates the user.

Additional Notes
- Users will be able to manually add and remove list items
- Data will be stored in a MySQL database
- Application will utilize cloud AI & Database Services

Concepts to Research
- Azure App Service (PaaS - deploying Web Apps)
- Azure Web Apps
- Azure Active Directory (authentication & authorization)
- Azure Functions
- REST API
- (React)/Angular (web application user interface)
- Flask/(Django)
- Azure Cognitive Suite (AI)
- Azure Speech Services (AI)
- Azure Translator Speech API (AI)
- Azure Storage (Data)
- Database for MySQL (Data)
- MySQL connector (Data)
- Tkinter (user interface) - cross platform
- PyQt (user interface) - requires Qt framework installation
- wxPython (user interface) - cross platform

Needs
- MySQL database that stores the created todo lists
- Python Library that allows the user and application to communication with each other using sounds
- Azure Tools
- Azure Cognitive Suite
- Azure Speech Services
- (STT) Python Library: azure-cognitiveservices-speech
- (TTS) Python Library: azure-ai-texttospeech
- Azure Translator Speech API
- Python Library: azure-ai-texttospeech
- Database Storage
- Database for MySQL
- MySQL connector for Python: mysql-connector-python or pymysql
- import mysql.connector
- User interface for the application
- Tkinter
- PyQt
- wxPython
- A list that resembles the following
◦ List item 1 (completed - green)
◦ List item 2 (incomplete - red)
◦ List item 3 (incomplete - red)
General Instruction Tips
1. Set up your development environment by installing Django, React, and any necessary libraries and dependencies.
2. Create a new Django project and application. You can do this by running the following commands in your terminal:
django-admin startproject myproject
cd myproject
python manage.py startapp myapp

1. Configure your MySQL database by installing the necessary drivers and creating a database in your Azure account.
2. Create a Django model that corresponds to your MySQL database schema. You can use Django's Object-Relational Mapping (ORM) system to map your database tables to Python classes.
3. Use Django's views and templates to create the backend logic and HTML rendering for your application.
4. Create a REST API using Django's built-in REST framework. This API will serve as the backend for your React frontend.
5. Create a new React app inside your Django project directory. You can do this by running the following command
npx create-react-app myapp

1. Create React components that correspond to the different views and features of your application.
2. Use Axios or another HTTP library to make API requests to your Django backend and update your React components accordingly.
3. Integrate Azure Cognitive Services into your application by using the relevant Python libraries or REST APIs.
4. Test your application locally and deploy it to a cloud platform like Azure App Service or Azure Kubernetes Service.

Set-Up notes
- To integrate React with Django, you will need to configure your Django project to serve the React frontend. You can do this by adding a static file route to your Django views, then configuring your React app to build and output its static files to a directory within your Django project.
- To integrate Azure Cognitive Services and MySQL with your application, you will need to use the relevant Python libraries or REST APIs to connect to and interact with these services. For example, you can use the Azure Cognitive Services Speech SDK to add speech-to-text and text-to-speech capabilities to your application, and use the MySQL connector for Python to interact with your MySQL database.