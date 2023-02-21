from models.Customer import Customer
import json


customer_id = __query_params__["id"]
customer = Customer.get_by_id(customer_id)


countries = [
    c["name"]
    for c in json.load(open("data/countries.json", "r"))
    ]


def update_customer():
    print(customer)
    customer.save()