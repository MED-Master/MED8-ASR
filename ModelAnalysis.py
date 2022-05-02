import plotly.express as px
import numpy as np
import pandas as pd
import os
data=pd.read_csv("logs/Logs.csv")
df = pd.DataFrame(data=data)


if not os.path.exists("images"):
    os.mkdir("images")
print(df)

fig = px.box(df, x="model", y="string", points="all", color="model")

fig.write_image("images/fig1.png")

fig.show()