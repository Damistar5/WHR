import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv('world-happiness-report-2021.csv')

# Create the choropleth map figure
fig = px.choropleth(
    df,
    locations='Country name',  # Column containing country names
    locationmode='country names',  # Use country names for location mode
    color='Ladder score',  # Column containing happiness scores
    hover_name='Country name',  # Column to display on hover
    color_continuous_scale=px.colors.sequential.Plasma,  # Choose color scale
    title='World Happiness Report',  # Title of the map
    labels={'Happiness Score': 'Happiness Score'},  # Custom label for the color scale
    template='plotly_dark'  # Choose plotly template
)

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='World Happiness Report'),

    dcc.Graph(
        id='world-happiness-map',
        figure=fig,
        style={'height': '800px', 'width': '100%'} 
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
