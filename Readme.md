# **Note**:
1. Internalization is enable in this project, with the two supported languages being *English* and 
*French* (Feel free to add yours).
2. For the tech-savvy, you will notice that the production settings file (pro.py) has `DEBUG = True`.
This is intentional and should be changed to **False** in a production environment.

# **Local (on your computer)**
To deploy this web application locally, follow these steps (make sure you have Python installed on your computer or your virtual machine):

1. Clone this repository using `git clone git@github.com:the1stenhancer/usermgmt.git`

2. On your local computer, navigate to the folder named after the repository you just cloned.

3. Open your favorite code editor (e.g. Vscode) and open the terminal there (Ctrl + Shift + `)

4. In the terminal that opens, do the following:
    ```
	pip install -r requirements.txt
	python manage.py runserver 127.0.0.1:49152 \--settings=usermgmt.settings.local
    ```

5. Open your browser and type: 127.0.0.1:49152/crud/ and you will see the web application.

# **Internet**
For this one, you will need to find a method based on your taste. Either setup yourself or use a web hosting company.