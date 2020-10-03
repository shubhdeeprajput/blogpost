# Blogpost

A web app made using `django` framework. The frontend is made using `html` and `bootstrap` and `sqlite3` is used as the database. You can add articles which can be viewed by anyone. Just make an account and you are good to go. To see a live demo [click here](http://vlogpost.herokuapp.com).

## Requirements

Python 3.7  
Django 2.2.8  
And additional requirements are in **Pipfile**.

## Setting up the Project

  * Download and install Python 3.7
  * Download and install Git.
  * Fork the Repository.
  * Clone the repository to your local machine `$ git clone https://github.com/<your-github-username>/blogpost.git`
  * Change directory to blogpost `$ cd blogpost`
  * Install pipenv `$ pip3 install pipenv`  
  * Create a virtual environment and install all requirements from Pipfile `$ pipenv install`  
  * Activate the env: `$ pipenv shell`
  * Make migrations `$ python manage.py makemigrations`
  * Migrate the changes to the database `$ python manage.py migrate`
  * Create superuser `$ python manage.py createsuperuser`
  * Run the server `$ python manage.py runserver`

## Contributing

Feel free to raise a issue or make a pull request to fix a bug or add a new feature. If you are new to open source you can first read about git by [clicking here](https://www.codecademy.com/learn/learn-git).

## Code of Conduct

Check the Code of Conduct [here](https://github.com/Rohan-cod/blogpost/blob/master/CODE_OF_CONDUCT.md)
