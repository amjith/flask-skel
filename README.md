This is a skeleton project for Flask with the following features.

* User login using open id (Google, Yahoo, OpenID, AOL, Flickr).
* SQLAlchemy ORM
* Alembic for DB migrations
* Whoosh for search
* Email support
* Bootstrap 3 for eye candy

Getting Started:
----------------

Clone this repo into your desired location. 

    git clone https://github.com/amjith/flask-skel.git project_name
    cd project_name
    mkvirtualenv project_name   # Create a new virtualenv, I use virtualenvwrapper(http://virtualenvwrapper.readthedocs.org/en/latest/).
    pip install -r requirements.txt  # Install the requirements.
    PYTHONPATH=. alembic revision --autogenerate -m 'Initial setup.'   # Create an initial migration.
    PYTHONPATH=. alembic upgrade head  # Upgrade the database to the newly created migration.
    python run.py  # Start the flask dev server that serves on port 5000.

Visit http://localhost:5000 to bask in the glory.
