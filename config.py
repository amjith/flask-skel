import os

def get_env_setting(setting):
    """ Get the environment setting or raise exception """
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise LookupError(error_msg)

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'ThisIsAReallyLongKey-ThatYoullNeverGuess'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

# Email settings

# debug settings
#MAIL_SERVER = 'localhost'
#MAIL_PORT = 25
#MAIL_USERNAME = None
#MAIL_PASSWORD = None

# Prod Settings
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'youremail@gmail.com'
MAIL_PASSWORD = get_env_setting('GMAIL_PASSWD')

ADMINS = ['youremail@provider.com']

OPENID_PROVIDERS = [
    {'icon': 'fa fa-google-plus', 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'icon': 'icon-yahoo', 'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'icon': 'icon-aim', 'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'icon': 'icon-flickr-1', 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'icon': 'icon-openid', 'name': 'OpenID', 'url': 'https://www.myopenid.com'}
]
