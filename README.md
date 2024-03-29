# GurufaBackend
## How to build and run on local
* If you wish to run your own build locally, first ensure you have python(3.11) or later globally installed in your computer. To check your version pf python, you can run this:
    ```bash
        $ python --version
    ```
*And create a '.env' file and add the follwing DEBUG=1 and SECRET_KEY

* After doing this, run this to create a virtual Environment in python:
    ```bash
        $ python -m venv ENV
    ```
* Activate virtual Environment:
    ```bash
        $ .\ENV\Scripts\activate
    ```
* Git clone this repo to your local
    ```bash
        $ git clone https://github.com/ArmaanChaand/GurufaBackend.git
    ```
* Install the necessary packages
    ```bash
        $ python -m pip install -r ./requirements.txt
    ```
* Run Migrations
    ```bash
        $ python manage.py makemigrations 
    ```
    ```bash
        $ python manage.py migrate
    ```

* Launch the Django server
    ```bash
        $ python manage.py runserver
    ```

### You can create superuser as well.
```bash
    $ python manage.py createsuperuser
```