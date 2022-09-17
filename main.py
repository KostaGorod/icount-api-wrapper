from dotenv import dotenv_values
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
