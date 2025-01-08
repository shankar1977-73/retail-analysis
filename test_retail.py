import pytest
from lib.DataReader import read_customers

#, read_orders
#from lib.DataManipulation import filter_closed_orders, count_orders_state, filter_orders_generic
#from lib.ConfigReader import get_app_config

def test_customerdf_count(spark):
    customer_count = read_customers(spark, "LOCAL").count()
    assert customer_count == 12435