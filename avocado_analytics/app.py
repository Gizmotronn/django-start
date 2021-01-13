# Import required libraries
import dash # initialization of application
import dash_core_components as dcc # interactive components like graphs /#/ assign shortcuts to library/module
import dash_html_components as html # access html tags
import pandas as pd # read and organise data

# Read the data and preprocess it for use in the dashboard
data = pd.read_csv("avocado.csv") # Use pandas to read the contents of the csv and assign it to the data variable    /#/ //#/ 
data = data.query("type == 'conventional' and region == 'Albany'") # create a query and use data to only show values from that query
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True) # sort by date

# Create instance of the Dash Class
app = dash.Dash(__name__)