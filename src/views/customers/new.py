from models.Customer import Customer
import json

countries = [c["name"] for c in json.load(open("data/countries.json", "r"))]

customer = Customer()


def register_customer():
    print(customer)
    customer.save(force_insert=True)
    __redirect__("views/customers/list")
