# **Note**:
Readme.md file is in both **English* and **French*

# **Local (sur votre ordinateur)**
Pour déployer cette application Web localement, procédez comme suit (assurez-vous que Python est installé sur votre ordinateur):

1. Clonez ce référentiel en utilisant `git clone git@github.com:the1stenhancer/usermgmt.git`

2. Sur votre ordinateur local, accédez au dossier nommé d'après le référentiel que vous venez de cloner.

3. Ouvrez votre éditeur de code préféré (par exemple, Vscode) et ouvrez-y le terminal (Ctrl + Shift + `)

4. Dans le terminal qui s'ouvre, procédez comme suit:
    ```
	pip install -r requirements.txt
	python manage.py runserver 127.0.0.1:49152 \--settings=usermgmt.settings.local
    ```

5. Ouvrez votre navigateur et tapez: 127.0.0.1:49152/crud/ et vous verrez l'application Web.

# **Internet**
For this one, you will need to find a method based on your taste. Either setup yourself or use a web hosting company.