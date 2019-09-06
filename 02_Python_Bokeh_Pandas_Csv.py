# Importing data from pandas and Csv and plotting using bokeh

# Importing Bokeh and Pandas

from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

# prepare some data , import from csv
df = pandas.read_csv("data.csv")
x = df["x"]
y = df["y"]

# prepare the output file
output_file("Line_from_CSVData.html")

# create figure object
f = figure()

# Create ling plot
f.line(x,y)

# write the plot in figure object
show(f)

