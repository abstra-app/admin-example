import pandas as pd
from models.Customer import Customer

customers = pd.DataFrame(list(Customer.select().dicts()))