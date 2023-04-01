import pandas as pd
from models.Customer import Customer
from playhouse.shortcuts import model_to_dict
from abstra.dashes import redirect, get_user

user = get_user()
if '@abstra.app' not in user.email:
    exit()

def reload():
    global customers
    customers = pd.DataFrame([model_to_dict(c) for c in Customer.select()])

reload()

def row_action(evt):
    if evt['payload']['action'] == "Edit":
        redirect("/views/customers/edit", {"id": evt['payload']['data']['id']})
    elif evt['payload']['action'] == "Delete":
        Customer.delete_by_id(evt['payload']['data']['id'])
        reload()
    else:
        print(evt)
        print(evt['payload']['action'])