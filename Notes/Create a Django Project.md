# Create a Django Project

* A django web application is made up of a project and its *constituent apps*
* Once you're in your directory and you've activated `virtual environment`, run this command:



/warning 

```
$ django-admin startproject personal_portfolio
```

"`personal_portfolio`" can be renamed to whatever you want

* This creates a new directory, in `rp-portfolio` called `personal_portfolio`
* `cd` into this directory:

/success

```
$ cd personal_portfolio
```

(This of course assumes that you're in the directory that we were in previously)

* After doing this, there is another folder called `personal_portfolio` (an app) and a file called `manage.py`
* The directory should look like this:

```
rp-portfolio/
│
├── personal_portfolio/
│   ├── personal_portfolio/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   └── manage.py
│
└── venv/
```

> Most of the work you do will be in that first `personal_portfolio` directory. To save having to `cd` through several directories each time you come to work on your project, it can be helpful to reorder this slightly by moving all the files up a directory. While you’re in the `rp-portfolio` directory, run the following commands:

```
$ mv personal_portfolio/manage.py ./
$ mv personal_portfolio/personal_portfolio/* personal_portfolio
$ rm -r personal_portfolio/personal_portfolio/
```

(Or just move them manually in the windows/file explorer until the view is like this:)

```
rp-portfolio/
│
├── personal_portfolio/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── venv/
│
└── manage.py
```

> Once your file structure is set up, you can now start the server and check that your set up was successful. In the console, run the following command:

```
python manage.py runserver
```

(`cd ../`) back into `rp_portfolio` dir. first



Go to http://localhost:8000/ to see the site live