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

# Create the layout property of the Dash app
app.layout """define parent component - an html div element"""= html.Div( # Using dash_html_components library 
    children=[ # add a child element to the html div
        html.H1(children="Avocado Analytics",), # first child element is a heading - h1
        html.P( # secondchild element is a paragraph - p
            children="Analyze the behavior of avocado prices"
            " and the number of avocados sold in the US"
            " between 2015 and 2018",
        ),
        dcc.Graph( # dash core components/graph. /#/ This one is plotting the average price during period of study
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["AveragePrice"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Average Price of Avocados"},
            },
        ),
        dcc.Graph( # graph plotting number of aUnits sold
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Total Volume"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Avocados Sold"},
            },
        ),
    ]
)

# Run the app
if __name__ == "__main__": # run app locally using flask's built-in server
    app.run_server(debug=True"""Enables hot reload""")