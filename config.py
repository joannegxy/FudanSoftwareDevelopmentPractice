
SECRET_KEY = ".yycsieovltsrifym;"

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'software_architecture'
USERNAME = 'root'
PASSWORD = '******'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 25
MAIL_USE_SSL = True
MAIL_USERNAME = '18864776196@163.com'
MAIL_PASSWORD = 'RXawyQevHCjRiqg6'
MAIL_DEFAULT_SENDER = '18864776196@163.com'
