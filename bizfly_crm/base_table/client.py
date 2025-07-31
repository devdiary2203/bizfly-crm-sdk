from datetime import datetime
from typing import List, Dict, Union

from bizfly_crm.common import constants, http, utils

__TABLES__ = ["data_customer", "data_deal", "data_account", "data_activity"]


def _validate(table: str, **kwargs):
    if not table:
        raise RuntimeError(f"table is required")
    if table not in __TABLES__:
        raise RuntimeError(f"table is invalid")


class Client:
    """Client for BizFly CRM Base Table operations. 
    This class provides methods to interact with the BizFly CRM API for base table operations.
    """
    
    def __init__(self, project_token: str = None, access_key: str = None, access_sign: str = None):
        if not project_token:
            raise RuntimeError(f"project_token is required")
        self.project_token = project_token

        if not access_key:
            raise RuntimeError(f"access_key is required")
        self.access_key = access_key

        if not access_sign:
            raise RuntimeError(f"access_sign is required")
        self.access_sign = access_sign

        # Get the current datetime object
        self.current_datetime = datetime.now()

        headers = {
            'cb-access-key': access_key,
            'cb-project-token': project_token,
            'Content-Type': 'application/json'
        }
        self.http_client = http.HttpClient(constants.BASE_URL, headers)

    def _headers(self):
        # Convert the datetime object to a Unix timestamp (float representing seconds since epoch)
        time_now = str(self.current_datetime.timestamp())
        return {
            'cb-access-sign': utils.generate_bizfly_signature(time_now, self.project_token, self.access_sign),
            'cb-access-timestamp': time_now,
        }

    def get_list_field_data(self, table: str = None, **kwargs):
        _validate(table)
        payload = {
            "table": table
        }
        return self.http_client.post(endpoint=constants.BASE_TABLE_STRUCT, json=payload, headers=self._headers())

    def create_field_data(self, table: str, data: Dict[List], **kwargs):
        _validate(table)
        payload = {
            "table": table,
            "data": data
        }
        return self.http_client.post(endpoint=constants.BASE_TABLE_ADD_FIELDS, json=payload, headers=self._headers())

    def get_detail_record(self,
                          table: str = None,
                          limit: int = 0,
                          skip: int = 0,
                          select: List = None,
                          query: Dict = None,
                          output: str = None,
                          **kwargs) -> Union[Dict, str]:
        _validate(table)
        payload = {
            "table": table,
            "limit": limit,
            "skip": skip,
            "select": select,
            "query": query,
            "output": output
        }
        return self.http_client.post(endpoint=constants.BASE_TABLE_FIND_DETAIL, json=payload, headers=self._headers())

    def update_record(self, table: str = None, **kwargs):
        _validate(table)
        payload = {
            "table": table,
            "mappingBy": None,
            "mode": None,
            "mergingFieldBy": None,
            "updateEmptyField": None,
            "data": None,
            "no_result": None
        }
        return self.http_client.post(endpoint=constants.BASE_TABLE_UPDATE, json=payload, headers=self._headers())
    
    def create_list_customer(self, data: List, **kwargs):
        payload = {
            "data": data
        }
        return self.http_client.post(endpoint=constants.BASE_TABLE_ADD_LISTS, json=payload, headers=self._headers())

    def get_list_customers(self, table: str = None, limit: int = 0, skip: int = 0, sort: List = None, output: str = None, **kwargs):
        payload = {
            "table": table,
            "limit": limit,
            "skip": skip,
            "sort": sort,
            "output": output,
        }
        return self.http_client.post(endpoint=constants.BASE_TABLE_GET_LISTS, json=payload, headers=self._headers())
    