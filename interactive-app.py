
from dash import Dash, dcc, Output, Input  # pip install dash
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots

df = px.pd.read_csv('https://raw.githubusercontent.com/malakali542/D1-361/main/13_41_10_30_6_2022.csv')

# Build components
app = Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])
mytitle = dcc.Markdown(children='Epic Title')
summary = dcc.Markdown(children='Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                'Cras luctus purus a sapien rutrum, et interdum justo faucibus. '
                                'Fusce odio lectus, tempor vitae maximus in, dictum non urna. M'
                                'aecenas vehicula rutrum arcu, sit amet vehicula diam scelerisque non. '
                                'Aenean vitae condimentum massa, quis iaculis massa. Nam in facilisis erat, '
                                'in pellentesque nisl. Etiam dignissim suscipit erat, quis lacinia mauris cursus nec. '
                                'Vestibulum et aliquam ex.')
mygraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=['Monday', 'Tuesday', 'Wednesday', 'Thursday'],
                        value='Monday',  # initial value displayed when page first loads
                        clearable=False)

fig = make_subplots(rows=3, cols=1, subplot_titles=("Temperature", "Humidity", "Light"), vertical_spacing=0.30)
fig.add_trace((go.Scatter(
    x=df["Time"],
    y=df[" temperature"],
    mode="lines",
    name="temperature",
)), row=1, col=1)

fig.add_trace((go.Scatter(
    x=df["Time"],
    y=df[" humidity"],
    mode="lines",
    name="humidity"
)), row=2, col=1)

fig.add_trace((go.Scatter(
    x=df["Time"],
    y=df[" light"],
    mode="lines",
    name="light"
)), row=3, col=1)

# customize layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([mytitle, dropdown, summary], width=4),
        dbc.Col([dcc.Graph(
            id='graph',
            figure=fig
        ), ], width=8)
    ]),
], fluid=True)

# Run app
if __name__ == '__main__':
    app.run_server(port=8053)
