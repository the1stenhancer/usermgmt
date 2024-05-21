# **Note**
1. In the **Local** part of this Readme.md, I explain how to deploy with localhost (127.0.0.1). You could setup a VM like Ubuntu Server or CentOS, git clone the project in it, configure uWSGI, NGINX etc and use it as your deployment server (this is actually more fun, give it a try!).

2. Internalization is enable in this project, with the two supported languages being *English* and 
*French* (Feel free to add yours).

3. Default super user credentials for the Django administration site:
   ```
   username: admin
   password: Super.20.24@
   ```

4. The project contains dummy data, so you would run the app and have data to use ASAP.

# **Local (on your computer)**
To deploy this web application locally, follow these steps (make sure you have Python installed on your computer or your virtual machine):

1. Clone this repository using `git clone git@github.com:the1stenhancer/usermgmt.git`

2. On your local computer, navigate to the folder named after the repository you just cloned.

3. Open your favorite code editor (e.g. Vscode) and open the terminal there (Ctrl + Shift + `)

4. In the terminal that opens, do the following:
    ```
	1. pip install -r requirements.txt
	2. python manage.py runserver 127.0.0.1:49152 \--settings=usermgmt.settings.local
    ```

5. Open your browser and type `127.0.0.1:49152` for the web application (and `127.0.0.1:49152/admin/` for the administrative site).

6. You should see the web application:

![Screenshot of the usermgmt web application home page](https://github.com/the1stenhancer/usermgmt/blob/main/crud/static/img/home_screen.png)



# **Internet**
For this one, you will need to find a method based on your taste. Either setup yourself or use a web hosting company.