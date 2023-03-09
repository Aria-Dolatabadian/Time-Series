import plotly.express as px
import pandas as pd
df = pd.read_csv("met.csv")
fig = px.line(df, x="date", y=df.columns,
              title='Value changes in six locations')
fig.show()
