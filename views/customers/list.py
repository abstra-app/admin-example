import pandas as pd
from models.Customer import Customer
from playhouse.shortcuts import model_to_dict
from abstra.dashes import redirect, get_user

user = get_user()
if '@abstra.app' not in user.email:
    exit()

customers = pd.DataFrame([model_to_dict(c) for c in Customer.select()])