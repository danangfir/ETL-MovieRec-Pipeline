import os

class Config:
    DEBUG = True
    TESTING = False
    PORT = 5000
    HOST = '0.0.0.0'
    DATABASE_URI = 'sqlite:///movies.db'
    
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    
    