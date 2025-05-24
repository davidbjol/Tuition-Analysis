import pandas as pd
import plotly.express as px

df = pd.read_csv("data/studentcost.csv")

filtered_df = df[df["Tuition_USD"] > 16705.02]

from preswald import table, text
text("# Tuition Analysis App")
text("Displaying universities with tuition above the midpoint of $16,705.02")
table(filtered_df, title="Filtered Data")

from preswald import plotly

fig = px.scatter(
    filtered_df,
    x="Tuition_USD",
    y="Rent_USD",
    color="Country",
    title="Tuition vs. Rent (Above Midpoint)",
    labels={"Tuition_USD": "Tuition (USD)", "Rent_USD": "Rent (USD)"},
    hover_data=["University", "City", "Program"]
)

fig.update_traces(marker=dict(size=12, color="lightblue"))
fig.update_layout(template="plotly_white")

plotly(fig)
