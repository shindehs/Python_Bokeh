#Plotting flower species

#Importing libraries
from bokeh.plotting import figure
from bokeh.io import output_notebook, output_file, show
from bokeh.sampledata.iris import flowers

#Define the output file path
output_file("iris.html")

#Create the figure object
f = figure()

#adding glyphs
f.circle(x=flowers["petal_length"], y=flowers["petal_width"])

#Save and show the figure
show(f)
#Plotting flower species

#Importing libraries
from bokeh.plotting import figure
from bokeh.io import output_notebook, output_file, show
from bokeh.sampledata.iris import flowers

#Define the output file path
output_file("iris.html")

#Create the figure object
f = figure()

# Styling the plot
f.plot_height = 1100
f.plot_width = 900
f.background_fill_color = "deeppink"

#adding glyphs
f.circle(x=flowers["petal_length"], y=flowers["petal_width"])

#Save and show the figure
show(f)
