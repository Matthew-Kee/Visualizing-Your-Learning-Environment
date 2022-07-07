# Hi Professor! Ignore the setup steps below. 
# You can view the prototype hosted online at [ADD LINK HERE]. Thanks!

# Setup (for devs):
# pip install dash
# pip install dash-bootstrap-components
# pip install pandas

# TODO:
# Functionality we NEED before any visual changes:
# - Add callbacks so that the Monday-Thursday buttons/dropdown 
# - Add data for different locations and different days
# - Figure out how to do the line segments for different locations - done!

# Visual nice-to-haves:
# Add images to each dropdown option
# Increase the size of the graphs

# import pandas for Data Frame manipulation
import pandas as pd

# import Dash class, the dcc (Dash Core Components) module, Dash html, callback context, 
# Output and Input (for callbacks), and the dbc (Dash Bootstrap Components) module
from dash import Dash, dcc, html, callback_context, Output, Input  
import dash_bootstrap_components as dbc

# import Plotly express module, Plotly graph objects, and the make_subplots function
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# STYLES:
white_button_style = {'background-color': 'white',
                      'color': 'black',
                      'height': '50px',
                      'width': '400px'}

# PARSE CSV FILE:
# read the csv of mock data from the file hosted on GitHub and import it into a df (data frame) which is a table of rows and columns
csvFile = 'https://raw.githubusercontent.com/malakali542/361Design1/main/mock_data1.csv'
df = px.pd.read_csv(csvFile)
# TODO: STOP HARDCODING THE DATE, I am hardcoding to June 30th 2022 right now because that's when the mock data was taken
# append the date of data collection to the times in the "Time" column so that Pandas can interpret the string as a DateTime object
df["Time"] = pd.to_datetime("2022-06-30" + ' ' + df["Time"])

# DECLARE COMPONENTS:
app = Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])
title = dcc.Markdown(children='Epic Title')
subtitle = dcc.Markdown(children='Visualizing daily student experience in place and time.')
week = dcc.Markdown(children='July 4th to July 7th')
mondayButton = html.Button('Monday', id='monday-button', n_clicks=0, style=white_button_style)
tuesdayButton = html.Button('Tuesday', id='tuesday-button', n_clicks=0, style=white_button_style)
wednesdayButton = html.Button('Wednesday', id='wednesday-button', n_clicks=0, style=white_button_style)
thursdayButton = html.Button('Thursday', id='thursday-button', n_clicks=0, style=white_button_style)
summaryTitle = dcc.Markdown(children='Check out other weeks:')
graph = dcc.Graph(id='graph', figure={})

# # CALLBACKS FOR BUTTONS:
@app.callback(
    # `component_id`, `component_property`
    Output(component_id='graph', component_property='figure'),
    Input(component_id='monday-button', component_property='n_clicks'),
    Input(component_id='tuesday-button', component_property='n_clicks'),
    Input(component_id='wednesday-button', component_property='n_clicks'),
    Input(component_id='thursday-button', component_property='n_clicks'))
def update_figure(monday, tuesday, wednesday, thursday):
    button_id = [p['prop_id'] for p in callback_context.triggered][0]
    if 'monday-button' in button_id:
        figure = fig.update
        figure = make_subplots(rows=3, cols=1, subplot_titles=("Monday", "Monday", "Monday"))
        return figure
    elif 'tuesday-button' in button_id:
        figure = make_subplots(rows=3, cols=1, subplot_titles=("Tuesday", "Tuesday", "Tuesday"))
        return figure
    elif 'wednesday-button' in button_id:
        figure = make_subplots(rows=3, cols=1, subplot_titles=("Wednesday", "Wednesday", "Wednesday"))
        return figure
    elif 'thursday-button' in button_id:
        figure = make_subplots(rows=3, cols=1, subplot_titles=("Thursday", "Thursday", "Thursday"))
        return figure
    else:
        figure = make_subplots(rows=3, cols=1, subplot_titles=("Default", "Default", "Default"))
        return figure

# MAKE FIGURES:
# make 3 rows of subplots, for Temperature, Humidity, and Light
fig = make_subplots(rows=3, cols=1, subplot_titles=("Temperature", "Humidity", "Light"))
fig.update_layout(height = 1000)

# add section 1 of the Temperature vs. Time plot in row 1
startTime1 = pd.to_datetime("2022-06-30 13:00:00")
endTime1 = pd.to_datetime("2022-06-30 13:54:00")
fig.add_trace((go.Scatter(
    x=df.loc[(df["Time"] > startTime1) & (df["Time"] < endTime1), "Time"],
    y=df.loc[(df["Time"] > startTime1) & (df["Time"] < endTime1), " Temperature"],
    mode="lines",
    name="E7 temperature",
)), row=1, col=1)

# add section 2 of the Temperature vs. Time plot in row 1
startTime2 = endTime1
endTime2 = pd.to_datetime("2022-06-30 14:20:00")
fig.add_trace((go.Scatter(
    x=df.loc[(df["Time"] > startTime2) & (df["Time"] < endTime2), "Time"],
    y=df.loc[(df["Time"] > startTime2) & (df["Time"] < endTime2), " Temperature"],
    mode="lines",
    name="SYDE lounge temperature",
)), row=1, col=1)

# add section 3 of the Temperature vs. Time plot in row 1
startTime3 = endTime2
endTime3 = pd.to_datetime("2022-06-30 15:00:00")
fig.add_trace((go.Scatter(
    x=df.loc[(df["Time"] > startTime3) & (df["Time"] < endTime3), "Time"],
    y=df.loc[(df["Time"] > startTime3) & (df["Time"] < endTime3), " Temperature"],
    mode="lines",
    name="DC library temperature",
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
        # add a column on the left with the title, subtitle, week, buttons, and summary
        dbc.Col([title, subtitle, week, mondayButton, tuesdayButton, wednesdayButton, thursdayButton, summaryTitle], width=4),
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
