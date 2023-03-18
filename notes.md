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
