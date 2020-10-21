class BaseConfig():
	API_PREFIX='/api'
	TESTING = False
	DEBUG= False

class DevConfig(BaseConfig):
	FLASK_ENV='development'
	DEBUG=True
	SQLALCHEMY_DATABASE_URI='postgresql://db_user:db_password@db-postgres:5432/flask-deploy'
	CELERY_BLOCKER='pyamqp://rabbit_user:rabbit_password@broker-rabbitmq//'
	CELERY_RESULT_BACKEND='rpc://rabbit_user:rabbit_password@broker-rabbitmq//'

class ProductionConfig(BaseConfig):
	FLASK_ENV='production'
	SQLALCHEMY_DATABASE_URI='postgresql://db_user:db_password@db-postgres:5432/flask-deploy'
	CELERY_BLOCKER='pyamqp://rabbit_user:rabbit_password@broker-rabbitmq//'
	CELERY_RESULT_BACKEND='rpc://rabbit_user:rabbit_password@broker-rabbitmq//'

class TestConfig(BaseConfig):
	FLASK_ENV='development'
	TESTING=True
	DEBUG=True
	CELERY_ALWAYS_EAGER=True