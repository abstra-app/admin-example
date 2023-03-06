from models.Customer import Customer
from models.Project import Project
import json
from playhouse.shortcuts import model_to_dict
import pandas as pd
from abstra.dashes import redirect, query_params


customer_id = query_params["id"]
customer = Customer.get_by_id(customer_id)
projects = pd.DataFrame(
    [model_to_dict(c) for c in Project.select().where(Project.customer == customer_id)]
)


countries = [c["name"] for c in json.load(open("data/countries.json", "r"))]


def update_customer():
    print(customer)
    customer.save()
    redirect("views/customers/list")
