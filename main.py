from dotenv import dotenv_values
import json
from icount import iCountSession

# flake8: noqa
if __name__ == "__main__":
    icountConfig: dict = dotenv_values(".env")
    with iCountSession(
        company=icountConfig.get("COMPANY"),
        username=icountConfig.get("USERNAME"),
        password=icountConfig.get("PASSWORD"),
    ) as session:
        res = session.supplier_list()
        print(res)

        icountDoc = {
            "doctype": "invrec",
            "client_id": "",
            "email": "clientemail@example.com",
            "client_name": "clientnameexample",
            "items": [
                {"description": "descr", "unitprice_incvat": "100", "quantity": "1"},
                {},
            ],
            "cc": {
                "sum": 100,
                "card_type": "VISA",
                "card_number": "0000",
                "holder_id": "123456789",
                "holder_name": "Israel Israeli",
                "confirmation_code": "875646",
            },
        }
        res = session.create_doc(icountDoc)
        print(res)
