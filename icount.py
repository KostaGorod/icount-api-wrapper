"""
A python wrapper for the icount.co.il api
https://www.icount.co.il/api-v3/
"""
import requests
from dotenv import dotenv_values

def post(url, data):
    req = requests.post(url=url, params=data)
    resp_json = req.json()
    if not resp_json.get("status", "False"):
        raise Exception(
            resp_json.get(
                "error_description", "General Error, no error_description found"
            )
        )
    return resp_json


class iCountSession(object):
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
        self.sid = post(endpoint, {"user": username, "cid": company, "pass": password})[
            "sid"
        ]

    def logout(self):
        if not self.sid:
            return
        endpoint = "https://api.icount.co.il/api/v3.php/auth/logout"
        post(endpoint, {"sid": self.sid})
        self.sid = None

    def supplier_list(self):
        endpoint = "https://api.icount.co.il/api/v3.php/supplier/get_list"
        res = post(
            endpoint, {"sid": self.sid, "detail_level": 10}
        )
        return res.get("suppliers")
    
    def create_doc(self):
        return


# flake8: noqa
if __name__ == "__main__":
    icountConfig = dotenv_values(".env")
    with iCountSession(
        company=icountConfig.get("COMPANY"), username=icountConfig.get("USERNAME"), password=icountConfig.get("PASSWORD")
    ) as session:
        res = session.supplier_list()
        print(res)