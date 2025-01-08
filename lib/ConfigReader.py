import configparser
from pyspark import SparkConf

## Loading the application conf into python dictionary

def get_app_config(env):
    config = configparser.ConfigParser()
    config.read("configs/application.conf")
    app_conf = {}
    for (key,value) in config.items(env):
        app_conf[key]=value
    return app_conf

def get_pyspark_config(env):
    config = configparser.ConfigParser()
    config.read("configs/pyspark.conf")
    pyspark_config = SparkConf()
    for (key,value) in config.items(env):
        pyspark_config.set(key,value)
    return pyspark_config