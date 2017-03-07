__author__= "Anto.s"
import json

def get_resp_notfound():
    resp_dict = {"status": "404",
                 "message": "Data Not Found",
                }
    return json.dumps(resp_dict)

def get_resp_invalid():
    resp_dict = {"status": "403",
                 "message": "Invalid request",
                }
    return json.dumps(resp_dict)

def get_resp_error(msg):
    resp_dict = {"status": "403",
                 "message": msg,
                }
    return json.dumps(resp_dict)


def get_resp_exception(msg):
    resp_dict = {"status": "500",
                 "message": msg,
                }
    return json.dumps(resp_dict)
