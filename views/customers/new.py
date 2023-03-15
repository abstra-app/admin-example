from models.Customer import Customer
import json
from abstra.dashes import redirect

countries = [c["name"] for c in json.load(open("data/countries.json", "r"))]

customer = Customer()


def register_customer():
    print(customer)
    customer.save(force_insert=True)
    redirect("views/customers/list")
