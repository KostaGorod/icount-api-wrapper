"""
A python wrapper for the icount.co.il api
https://www.icount.co.il/api-v3/
"""
import requests


def post(url, data=None, json=None, params=None):
    req = requests.post(url=url, data=data, json=json, params=params)
    resp_json = req.json()
    if not resp_json.get("status", "False"):
        raise Exception(
            resp_json.get(
                "error_description", "General Error, no error_description found"
            )
        )
    return resp_json


class iCountAPI(object):
    def __init__(self, company, username, password):
        self.sid = None
        self.login(company, username, password)

    def __del__(self):
        self.logout()

    def __enter__(self):
        assert self.sid is not None
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.logout()

    def login(self, company, username, password):
        self.logout()
        endpoint = "https://api.icount.co.il/api/v3.php/auth/login"
        self.sid = post(
            endpoint, params={"user": username, "cid": company, "pass": password}
        )["sid"]

    def logout(self):
        if not self.sid:
            return
        endpoint = "https://api.icount.co.il/api/v3.php/auth/logout"
        post(endpoint, params={"sid": self.sid})
        self.sid = None

    def supplier_list(self):
        endpoint = "https://api.icount.co.il/api/v3.php/supplier/get_list"
        res = post(endpoint, params={"sid": self.sid, "detail_level": 10})
        return res.get("suppliers")

    def create_doc(self, doc: dict):
        endpoint = "https://api.icount.co.il/api/v3.php/doc/create"
        res = post(endpoint, json={"sid": self.sid} | doc)
        return res

    def get_doc(self, doctype, docnum: int):
        endpoint = "https://api.icount.co.il/api/v3.php/doc/info"
        res = post(
            endpoint, params={"sid": self.sid, "doctype": doctype, "docnum": docnum}
        )
        return res

    def cancel_doc(self, doctype, docnum: int):
        endpoint = "https://api.icount.co.il/api/v3.php/doc/cancel"
        res = post(
            endpoint, params={"sid": self.sid, "doctype": doctype, "docnum": docnum}
        )
        return res
