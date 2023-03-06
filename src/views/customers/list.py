import pandas as pd
from models.Customer import Customer
from playhouse.shortcuts import model_to_dict
from abstra.dashes import redirect

customers = pd.DataFrame([model_to_dict(c) for c in Customer.select()])
