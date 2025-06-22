s = 'jagan'
count = 0
for i in s:
    count+=1
print(count)
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    "City": ["Delhi", "Mumbai", "Chennai", "Kolkata"],
    "Population": [20, 19, 11, 14]
})

# Create a bar chart
fig = px.bar(df, x="City", y="Population", title="Population by City")

# Show the interactive chart
fig.show()
'''