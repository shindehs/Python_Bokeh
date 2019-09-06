# Import Bokeh and pandas

from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

# Prepare some data
df = pandas.read_csv("bachelors.csv")
x = df["Year"]
y = df["Engineering"]

# prepare output file

output_file("LineChartFromBatchlersCSV.html")


# prepare figure object

f = figure()

# create line chart

f.line(x,y)

# Print the line chart

show(f)