import sys
sys.path.append("..")  # Adjust the path as necessary

import requests
import constants


class Client:
    """Client for BizFly CRM Base Table operations. 
    This class provides methods to interact with the BizFly CRM API for base table operations.
    """
    
    def __init__(self):
        ...

    def getListFieldData(self, endpoint, params=None):
        ...

    def createFieldData(self, endpoint, data=None):
        ...

    def getDetailRecord(self, endpoint, data=None):
        ...

    def createListCustomer(self, endpoint): 
        ...
    
    def getListCustomer(self, endpoint):
        ...
    