# Making a basic Bokeh Graph

# importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas


# prepare some data
x =[1,2,3,4,5]
y =[6,7,8,9,10]

# prepare the output file
output_file("Circle_html")

# create figure file
f = figure()

# create line plot
f.circle(x,y)

#write the plot in figure object
show(f)