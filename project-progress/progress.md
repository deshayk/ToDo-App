# Developer Comments
## Description
This page is dedicated to comments, notes, and important observations made by the developer during the project creation process.

## 3/19/2023
- The goal for today was to successfully install Django for the project. I am having some trouble with the installation. I have successfully created the virtual environment but for some reason, I am unable to connect Django. This virtual environment attempt was made after trying to install Django globally on the machine but had the same issue. Python, pip, and Django are all installed on the machine.

- Update: I successfully installed Django in the myenv virtual environment using the following steps using the bash terminal: 
1. Activate the virtual environment
```source myenv/Scripts/activate```
2. Install Django
```pip install django```
3. Update pip 22.22.2 to 23.0.1
```python.exe -m pip install --upgrade pip```
4. Verify Django installation
```python -m django --version```

- Now, I am attempting to install react using a new virtual environment inside of the JS-lib folder. I reinstalled node.js. I am now having issues connecting the node.js path.

- I attempted to move on to something else and play with the TTS library pyttsx3, however, I am expiriencing module installation issues. I installed the module using ```pip install --user pyttsx3``` because I did not have the correct user permissions but there are still connection issues. I use the following code ```pip install --user --upgrade wheel``` to upgrade the wheel due to experiencing different installation errors.