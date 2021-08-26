import os

DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'postgres')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'mukul123')
DATABASE_HOST = os.getenv('DATABASE_HOST', '192.168.0.101')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'mukuldb')
TEST_DATABASE_NAME = os.getenv('DATABASE_NAME', 'test_mukuldb')
REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.getenv('REDIS_PORT', '6379')
REDIS_DB = os.getenv('REDIS_DB', '0')