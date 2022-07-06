# Hi Professor! Ignore the setup steps below. You can view the prototype hosted online at [ADD LINK HERE]. Thanks!

# Setup (for devs):
# pip install dash
# pip install dash-bootstrap-components
# pip install pandas

# TODO:
# Functionality we NEED before any visual changes:
# - Add callbacks so that the Monday-Thursday buttons/dropdown 
# - Add data for different locations and different days (can fake this, for proof-of-concept can use straight lines)
# - Figure out how to do the line segments for different locations (honestly if this is too time consuming we can rethink it)

# Visual nice-to-haves:
# Add images to each dropdown option
# Increase the size of the graphs

# import Dash class, the dcc (Dash Core Components) module, Output and Input (for callbacks), and the dbc (Dash Bootstrap Components) module
from dash import Dash, dcc, Output, Input  
import dash_bootstrap_components as dbc

# import Plotly express module, Plotly graph objects, and the make_subplots function
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# PARSE CSV FILE:
# read the csv of mock data from the file hosted on GitHub and import it into a df (data frame) which is a table of rows and columns
csvFile = 'https://raw.githubusercontent.com/malakali542/361Design1/main/mock_data1.csv'
df = px.pd.read_csv(csvFile)

# DECLARE COMPONENTS:
app = Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])
title = dcc.Markdown(children='Epic Title')
subtitle = dcc.Markdown(children='Visualizing daily student experience in place and time.')
week = dcc.Markdown(children='July 4th to July 7th')
summaryTitle = dcc.Markdown(children='Check out other weeks:')
dropdown = dcc.Dropdown(options=['Monday', 'Tuesday', 'Wednesday', 'Thursday'], # dropdown options (days of the week)
                        value='Monday',  # initial value displayed when page first loads
                        clearable=False, # hide the "x" button that allows users to clear the dropdown
                        searchable=False) # remove the ability for users to type and search through the options
graph = dcc.Graph(figure={}) 

# MAKE FIGURES:
# make 3 rows of subplots, for Temperature, Humidity, and Light
fig = make_subplots(rows=3, cols=1, subplot_titles=("Temperature", "Humidity", "Light"), vertical_spacing=0.30)

# add the Temperature vs. Time plot in row 1
fig.add_trace((go.Scatter(
    x=df["Time"],
    y=df[" Temperature"],
    mode="lines",
    name="temperature",
)), row=1, col=1)
# add the Humidity vs. Time plot in row 2
fig.add_trace((go.Scatter(
    x=df["Time"],
    y=df[" humidity"],
    mode="lines",
    name="humidity"
)), row=2, col=1)
# add the Light vs. Time plot in row 3
fig.add_trace((go.Scatter(
    x=df["Time"],
    y=df[" Light"],
    mode="lines",
    name="light"
)), row=3, col=1)

# LAYOUT COMPONENTS USING GRIDS:
# declare a top-level container
app.layout = dbc.Container([
    # we currently have a single row
    dbc.Row([ 
        # add a column on the left with the title, dropdown, and summary
        dbc.Col([title, subtitle, week, dropdown, summaryTitle], width=4),
        # add a column on the right for the graph, and set it to display fig which has our 3 subplots
        dbc.Col([dcc.Graph(
            id='graph',
            figure=fig
        ), ], width=8)
    ]),
], fluid=True) # set the container to expand fluidly to fill space on the page

# RUN THE APP:
if __name__ == '__main__':
    app.run_server(port=8053)
