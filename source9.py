#READING FROM SQL DATABASE

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///college.db")
df = pd.read_sql("SELECT *FROM STUDENTS",engine)

print(df) 