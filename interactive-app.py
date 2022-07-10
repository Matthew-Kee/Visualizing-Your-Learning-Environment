# Hi Professor! Ignore the setup steps below. 
# You can view the prototype hosted online at https://interactive-app1237.herokuapp.com/. Thanks!

# Setup (for devs):
# pip install dash
# pip install dash-bootstrap-components
# pip install pandas

# import pandas for Data Frame manipulation
from calendar import MONDAY, TUESDAY, WEDNESDAY, weekday
from re import match

import pandas as pd

# import NumPy for number manipulation
from numpy import NaN

# import enums for better match statements
from enum import Enum

# import Dash class, the dcc (Dash Core Components) module, Dash html, callback context,
# Output and Input (for callbacks), and the dbc (Dash Bootstrap Components) module
from dash import Dash, dcc, html, callback_context, Output, Input
import dash_bootstrap_components as dbc

# import Plotly express module, Plotly graph objects, and the make_subplots function
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# STYLES:
whiteButtonStyle = {'background-color': 'white',
                    'color': 'black',
                    'height': '50px',
                    'width': '380px',
                    'border-radius': '20px',
                    'margin': '10px'
                    }

titleStyle = {'font-family': 'Helvetica',
                'font-size': '30px',
                'font-weight': '400',
                'line-height': '34px',
                'color': '#000000'
                }

datesStyle = {'font-family': 'Helvetica',
                'font-size': '24px',
                'font-weight': '400',
                'line-height': '28px',
                'color': '#000000'
                }

subtitleStyle = {'font-family': 'Helvetica',
                'font-size': '20px',
                'font-weight': '700',
                'line-height': '23px',
                'color': '#000000'
                }

boldStyle = {'font-family': 'Helvetica',
            'font-size': '16px',
            'font-weight': '700',
            'line-height': '24px',
            'color': '#000000'
            }

# CONSTANTS:
MONDAY_CLASS_START_TIME_1 = pd.to_datetime('2022-07-04 08:00:00')
MONDAY_CLASS_END_TIME_1 = pd.to_datetime('2022-07-04 11:50:00')
MONDAY_LOUNGE_START_TIME = pd.to_datetime('2022-07-04 11:50:00')
MONDAY_LOUNGE_END_TIME = pd.to_datetime('2022-07-04 13:00:00')
MONDAY_CLASS_START_TIME_2 = pd.to_datetime('2022-07-04 13:00:00')
MONDAY_CLASS_END_TIME_2 = pd.to_datetime('2022-07-04 15:20:00')
MONDAY_DC_START_TIME = pd.to_datetime('2022-07-04 15:20:00')
MONDAY_DC_END_TIME = pd.to_datetime('2022-07-04 23:59:00')

TUESDAY_CLASS_START_TIME_1 = pd.to_datetime('2022-07-05 08:00:00')
TUESDAY_CLASS_END_TIME_1 = pd.to_datetime('2022-07-05 12:35:00')
TUESDAY_LOUNGE_START_TIME = pd.to_datetime('2022-07-05 12:35:00')
TUESDAY_LOUNGE_END_TIME = pd.to_datetime('2022-07-05 13:30:00')
TUESDAY_CLASS_START_TIME_2 = pd.to_datetime('2022-07-05 13:30:00')
TUESDAY_CLASS_END_TIME_2 = pd.to_datetime('2022-07-05 15:50:00')
TUESDAY_DC_START_TIME = pd.to_datetime('2022-07-05 15:50:00')
TUESDAY_DC_END_TIME = pd.to_datetime('2022-07-05 23:59:00')

WEDNESDAY_CLASS_START_TIME_1 = pd.to_datetime('2022-07-06 08:00:00')
WEDNESDAY_CLASS_END_TIME_1 = pd.to_datetime('2022-07-06 11:20:00')
WEDNESDAY_LOUNGE_START_TIME = pd.to_datetime('2022-07-06 11:20:00')
WEDNESDAY_LOUNGE_END_TIME = pd.to_datetime('2022-07-06 12:20:00')
WEDNESDAY_CLASS_START_TIME_2 = pd.to_datetime('2022-07-06 12:30:00')
WEDNESDAY_CLASS_END_TIME_2 = pd.to_datetime('2022-07-06 17:00:00')
WEDNESDAY_DC_START_TIME = pd.to_datetime('2022-07-06 17:00:00')
WEDNESDAY_DC_END_TIME = pd.to_datetime('2022-07-06 23:59:00')

THURSDAY_CLASS_START_TIME_1 = pd.to_datetime('2022-07-07 08:00:00')
THURSDAY_CLASS_END_TIME_1 = pd.to_datetime('2022-07-07 12:20:00')
THURSDAY_LOUNGE_START_TIME = pd.to_datetime('2022-07-07 12:20:00')
THURSDAY_LOUNGE_END_TIME = pd.to_datetime('2022-07-07 13:30:00')
THURSDAY_CLASS_START_TIME_2 = pd.to_datetime('2022-07-07 13:30:00')
THURSDAY_CLASS_END_TIME_2 = pd.to_datetime('2022-07-07 14:50:00')
THURSDAY_DC_START_TIME = pd.to_datetime('2022-07-07 14:50:00')
THURSDAY_DC_END_TIME = pd.to_datetime('2022-07-07 23:59:00')

FIGURE_HEIGHT = 1000

SUMMARY_LIST = ['Hottest (August 15 to 18)','Highest humidex (June 6 to 9)'
    , 'Sunniest (August 15 to 18)', 'Coldest (January 12 to 15)', 'Darkest (December 16 to 19)']
AVERAGED_WEEKS_LIST = ['Winter', 'Spring', 'Summer', 'Fall']

# ENUMS:
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4

# PARSE CSV FILE:
# read the csv of mock data from the file hosted on GitHub and import it into a df (data frame) which is a table of rows and columns
csvFile = 'Data_July4ToJuly7.csv'
df = px.pd.read_csv(csvFile)
# use the Date and Time columns to create a DateTime column of DateTime objects
df.insert(loc=0, column='DateTime', value=pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d-%m-%Y %H:%M:%S'),
          allow_duplicates=True)

# DECLARE COMPONENTS:
app = Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])
title = dcc.Markdown(children='SYDE Environment Dashboard', style=titleStyle)
subtitle = dcc.Markdown(children='Visualizing daily student experience in place and time. Collected data is compared against acceptable ranges defined by ASHRAE (American Society of Heating, Refrigerating and Air-Conditioning Engineers) and CEN (Comité Européen de Normalisation/European Committee for Standardization).')
week = dcc.Markdown(children='July 4th to July 7th', style=datesStyle)
mondayButton = html.Button('Monday', id='monday-button', n_clicks=0, style=whiteButtonStyle)
tuesdayButton = html.Button('Tuesday | MOST HUMID', id='tuesday-button', n_clicks=0, style=whiteButtonStyle)
wednesdayButton = html.Button('Wednesday | HOTTEST', id='wednesday-button', n_clicks=0, style=whiteButtonStyle)
thursdayButton = html.Button('Thursday | BRIGHTEST', id='thursday-button', n_clicks=0, style=whiteButtonStyle)
summaryTitle = dcc.Markdown(children='Check out other weeks:', style=subtitleStyle)
summarySubtitle = dcc.Markdown(children='Extreme Weeks', style=boldStyle)
summary = html.Ul(id='summary-list', children=[html.Li(i, style={'text-decoration': 'underline'}) for i in SUMMARY_LIST])
averagedWeeksTitle = dcc.Markdown(children='Averaged weeks for', style=boldStyle)
averagedWeeks = html.Ul(id='averaged-weeks-list', children=[html.Li(i, style={'text-decoration': 'underline'}) for i in AVERAGED_WEEKS_LIST])
graph = dcc.Graph(id='graph', figure={})

# array of the 3 columns of data in the csv that we will plot against time
plots = ['Temperature', 'Humidity', 'Light', 'Sunlight']
fig = make_subplots(rows=4, cols=1, subplot_titles=plots)

# set up layout of the figure
fig.update_layout(
height=FIGURE_HEIGHT,
showlegend=True,
legend_tracegroupgap=(FIGURE_HEIGHT - 150) / 4)
fig.update_xaxes(tickformat="%I:%M %p")

# set the axes for all the subplots
fig['layout']['xaxis']['title']='Time'
fig['layout']['xaxis2']['title']='Time'
fig['layout']['xaxis3']['title']='Time'
fig['layout']['xaxis4']['title']='Time'
fig['layout']['yaxis']['title']='Temperature (°C)'
fig['layout']['yaxis2']['title']='Humidity (%)'
fig['layout']['yaxis3']['title']='Lux'
fig['layout']['yaxis4']['title']='Lumen'

# set the range on the y axes for all the subplots
fig.update_layout(yaxis = dict(range=[18,30]))
fig.update_layout(yaxis2 = dict(range=[0,100]))
fig.update_layout(yaxis3 = dict(range=[0,1000]))
fig.update_layout(yaxis4 = dict(range=[0,1000]))

# CALLBACKS FOR BUTTONS:
@app.callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id='monday-button', component_property='n_clicks'),
    Input(component_id='tuesday-button', component_property='n_clicks'),
    Input(component_id='wednesday-button', component_property='n_clicks'),
    Input(component_id='thursday-button', component_property='n_clicks'))
def update_figure(monday, tuesday, wednesday, thursday):
    button_id = [p['prop_id'] for p in callback_context.triggered][0]
    if 'monday-button' in button_id:
        return updatePlotForDate(Weekday.MONDAY)
    elif 'tuesday-button' in button_id:
        return updatePlotForDate(Weekday.TUESDAY)
    elif 'wednesday-button' in button_id:
        return updatePlotForDate(Weekday.WEDNESDAY)
    elif 'thursday-button' in button_id:
        return updatePlotForDate(Weekday.THURSDAY)
    else:
        return createDefaultPlot()

def createDefaultPlot():
    figure = fig
    figure.data = []

    # enumerate through all of the subplots
    for index, plot in enumerate(plots, start=1):
        # Add E7 6008 section
        figure.add_trace((go.Scatter(
            x=df.loc[(df['DateTime'] > MONDAY_CLASS_START_TIME_1) & (df['DateTime'] < MONDAY_CLASS_END_TIME_1) |
                     (df['DateTime'] > MONDAY_CLASS_START_TIME_2) & (
                             df['DateTime'] < MONDAY_CLASS_END_TIME_2), 'DateTime'],
            y=df.loc[(df['DateTime'] > MONDAY_CLASS_START_TIME_1) & (df['DateTime'] < MONDAY_CLASS_END_TIME_1) |
                     (df['DateTime'] > MONDAY_CLASS_START_TIME_2) & (df['DateTime'] < MONDAY_CLASS_END_TIME_2), plot],
            mode='lines',
            name='E7 6008',
            # name = 'Classroom', # The name of the location is changed to be more general to generate graphs for our prototype that targets a more general third-person audience (incoming students/parents)
            connectgaps=False,
            line=dict(color='#FF2D2D'),
            legendgroup=index,
        )), row=index, col=1)

        # Add SYDE lounge section
        figure.add_trace((go.Scatter(
            x=df.loc[
                (df['DateTime'] > MONDAY_LOUNGE_START_TIME) & (df['DateTime'] < MONDAY_LOUNGE_END_TIME), 'DateTime'],
            y=df.loc[(df['DateTime'] > MONDAY_LOUNGE_START_TIME) & (df['DateTime'] < MONDAY_LOUNGE_END_TIME), plot],
            mode='lines',
            name='SYDE lounge',
            # name = 'Lounge/lunch room', # The name of the location is changed to be more general to generate graphs for our prototype that targets a more general third-person audience (incoming students/parents)
            connectgaps=False,
            line=dict(color='#5048E5'),
            legendgroup=index,
        )), row=index, col=1)

        # Add DC section
        figure.add_trace((go.Scatter(
            x=df.loc[(df['DateTime'] > MONDAY_DC_START_TIME) & (df['DateTime'] < MONDAY_DC_END_TIME), 'DateTime'],
            y=df.loc[(df['DateTime'] > MONDAY_DC_START_TIME) & (df['DateTime'] < MONDAY_DC_END_TIME), plot],
            mode='lines',
            name='DC library',
            # name = 'Library study space', # The name of the location is changed to be more general to generate graphs for our prototype that targets a more general third-person audience (incoming students/parents)
            connectgaps=False,
            line=dict(color='#62B013'),
            legendgroup=index,
        )), row=index, col=1)

    # Add acceptable ranges as an overlay onto each plot
    figure.add_hrect(y0=20.8, y1=27.2, row=1, col=1,
                        annotation_text="ASHRAE acceptable range: 20.8°C - 27.2°C", annotation_position="top right",
                        annotation=dict(font_size=20, font_family="Arial"),
                        fillcolor="#5048E5", opacity=0.10, line_width=2
                        )
    figure.add_hrect(y0=0, y1=60, row=2, col=1,
                        annotation_text="ASHRAE acceptable range: 0%-60%", annotation_position="top right",
                        annotation=dict(font_size=20, font_family="Arial"),
                        fillcolor="#5048E5", opacity=0.10, line_width=2
                        )
    figure.add_hrect(y0=500, y1=1000, row=3, col=1,
                        annotation_text="CEN acceptable range for lecture halls: 500+ lux", annotation_position="top right",
                        annotation=dict(font_size=20, font_family="Arial"),
                        fillcolor="#5048E5", opacity=0.10, line_width=2
                        )

    return figure


def updatePlotForDate(date):
    class_start_time_1 = None
    class_end_time_1 = None
    class_start_time_2 = None
    class_end_time_2 = None
    lounge_start_time = None
    lounge_end_time = None
    DC_start_time = None
    DC_end_time = None

    # set the start and end times for each location depending on the day (based on the class schedule)
    match date:
        case Weekday.MONDAY:
            class_start_time_1 = MONDAY_CLASS_START_TIME_1
            class_end_time_1 = MONDAY_CLASS_END_TIME_1
            class_start_time_2 = MONDAY_CLASS_START_TIME_2
            class_end_time_2 = MONDAY_CLASS_END_TIME_2
            lounge_start_time = MONDAY_LOUNGE_START_TIME
            lounge_end_time = MONDAY_LOUNGE_END_TIME
            DC_start_time = MONDAY_DC_START_TIME
            DC_end_time = MONDAY_DC_END_TIME
        case Weekday.TUESDAY:
            class_start_time_1 = TUESDAY_CLASS_START_TIME_1
            class_end_time_1 = TUESDAY_CLASS_END_TIME_1
            class_start_time_2 = TUESDAY_CLASS_START_TIME_2
            class_end_time_2 = TUESDAY_CLASS_END_TIME_2
            lounge_start_time = TUESDAY_LOUNGE_START_TIME
            lounge_end_time = TUESDAY_LOUNGE_END_TIME
            DC_start_time = TUESDAY_DC_START_TIME
            DC_end_time = TUESDAY_DC_END_TIME
        case Weekday.WEDNESDAY:
            class_start_time_1 = WEDNESDAY_CLASS_START_TIME_1
            class_end_time_1 = WEDNESDAY_CLASS_END_TIME_1
            class_start_time_2 = WEDNESDAY_CLASS_START_TIME_2
            class_end_time_2 = WEDNESDAY_CLASS_END_TIME_2
            lounge_start_time = WEDNESDAY_LOUNGE_START_TIME
            lounge_end_time = WEDNESDAY_LOUNGE_END_TIME
            DC_start_time = WEDNESDAY_DC_START_TIME
            DC_end_time = WEDNESDAY_DC_END_TIME
        case Weekday.THURSDAY:
            class_start_time_1 = THURSDAY_CLASS_START_TIME_1
            class_end_time_1 = THURSDAY_CLASS_END_TIME_1
            class_start_time_2 = THURSDAY_CLASS_START_TIME_2
            class_end_time_2 = THURSDAY_CLASS_END_TIME_2
            lounge_start_time = THURSDAY_LOUNGE_START_TIME
            lounge_end_time = THURSDAY_LOUNGE_END_TIME
            DC_start_time = THURSDAY_DC_START_TIME
            DC_end_time = THURSDAY_DC_END_TIME

    figure = fig

    # enumerate through all of the subplots
    for index, plot in enumerate(plots, start=1):
        # Update E7 6008 section
        figure.update_traces(
            x=df.loc[(df['DateTime'] > class_start_time_1) & (df['DateTime'] < class_end_time_1) |
                     (df['DateTime'] > class_start_time_2) & (df['DateTime'] < class_end_time_2), 'DateTime'],
            y=df.loc[(df['DateTime'] > class_start_time_1) & (df['DateTime'] < class_end_time_1) |
                     (df['DateTime'] > class_start_time_2) & (df['DateTime'] < class_end_time_2), plot],
            selector=dict(name="E7 6008"),
            # selector=dict(name="Classroom"), # The name of the location is changed to be more general to generate graphs for our prototype that targets a more general third-person audience (incoming students/parents)
            row=index
        )

        # Update SYDE lounge section
        figure.update_traces(
            x=df.loc[(df['DateTime'] > lounge_start_time) & (df['DateTime'] < lounge_end_time), 'DateTime'],
            y=df.loc[(df['DateTime'] > lounge_start_time) & (df['DateTime'] < lounge_end_time), plot],
            selector=dict(name="SYDE lounge"),
            # selector=dict(name="Lounge/lunch room"), # The name of the location is changed to be more general to generate graphs for our prototype that targets a more general third-person audience (incoming students/parents)
            row=index
        )

        # Update DC library section
        figure.update_traces(
            x=df.loc[(df['DateTime'] > DC_start_time) & (df['DateTime'] < DC_end_time), 'DateTime'],
            y=df.loc[(df['DateTime'] > DC_start_time) & (df['DateTime'] < DC_end_time), plot],
            selector=dict(name="DC library"),
            # selector=dict(name="Library study space"), # The name of the location is changed to be more general to generate graphs for our prototype that targets a more general third-person audience (incoming students/parents)
            row=index
        )

    return figure


# LAYOUT COMPONENTS USING GRIDS:
# declare a top-level container
app.layout = dbc.Container([
    # we currently have a single row
    dbc.Row([
        # add a column on the left with the title, subtitle, week, buttons, and summary (all the elements other than the plots)
        dbc.Col([title, subtitle, week, mondayButton, tuesdayButton, wednesdayButton, thursdayButton, summaryTitle, summarySubtitle, summary, averagedWeeksTitle, averagedWeeks],
                width=4),
        # add a column on the right for the graph, and set it to display fig which has our 3 subplots
        dbc.Col([dcc.Graph(
            id='graph',
            figure=fig
        ), ], width=8)
    ]),
], fluid=True)  # set the container to expand fluidly to fill space on the page

# RUN THE APP:
if __name__ == '__main__':
    app.run_server(port=8053)
