# Chat Application 📱
This is a simple chat application built with Django Framework and Ajax. Its a real-time communication application where users can chat with each other in real-time. 

## Installation
### 1. Clone the repository using:

```bash
git clone https://github.com/Jeff-mwangi/django_group_chat_application.git
```

### 2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the requirements:

```bash
pip install -r requirements.txt
```

<!-- adding postgres database -->
### 4. Create a postgres database and add the credentials to env file
In these project, I used postgres database. (You can use any database of your choice. Remember to change the database settings in settings.py file). If you are using postgres, you need to install it first. You can follow this [link](https://www.postgresql.org/download/) to install postgres. After installing postgres, create a database and add the credentials to the env file.

### 5. Add the credentials to the env file
Add the credentials to the env file. You can use the env.example file as a guide:
    
    
    SECRET_KEY=your_secret_key
    DATABASE_NAME=your_database_name
    DATABASE_USER=your_database_user
    DATABASE_PASSWORD=your_database_password
    DATABASE_HOST=your_database_host
    DATABASE_PORT=your_database_port
    




### 6. Run the migrations:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```


### 5. Run the server:

```bash
python manage.py runserver
```

> Incase the application ask for a secret key, uncomment the secret key in settings.py. The secret key was commented out for production purposes. The secret key available in the settings.py file is not for production purposes. Feel free to use it for development purposes or generate your own secret key [here](https://djecrety.ir/).



## Usage
1. Create a superuser to access the admin panel:

```bash
python manage.py createsuperuser
```

2. Run the server:

```bash
python manage.py runserver
```

Use the credentials to access the admin panel. You can create users and rooms from the admin panel.

