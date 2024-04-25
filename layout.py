import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


''''
The ladder score represents the happiness score. Indicators:
Top Countries with least and most happiness. Country rankings based on Healthy life
 expectancy, Freedom to make life choices, GDP per capita
 , social support, perception of corruption, generosity
'''

def create_choropleth_map():

    df = pd.read_csv('world-happiness-report-2021.csv')


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

    # Create a dcc.Graph component to render the choropleth map
    graph = dcc.Graph(figure=fig,style={'height': '800px', 'width': '100%'})

    return graph

def display_clickable_container():
    # Define the address and corresponding link
    address = {'title': 'Address 1', 'link': '/address1'}

    # Create a list to hold the clickable container
    clickable_containers = []

    # Create the clickable container
    container = dbc.Col(
        dbc.Card(
            [
                html.Img(src='assets/image_name.png', className='card-img-top', style={'width': '100%'}),
                dbc.CardBody(
                    html.A(
                        address['title'],
                        href=address['link'],
                        style={'text-decoration': 'none', 'color': 'inherit'}
                    )
                )
            ],
            style={'cursor': 'pointer', 'border-radius': '15px', 'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'padding': '20px', 'height': '700px'}  # Adjust the height as needed
        ),
        width=4,  # Adjust the width to control the number of columns per row
        className='mb-3',
    )
    clickable_containers.append(container)

    # Return the clickable container wrapped in a row
    return dbc.Row(clickable_containers)

def create_life_expectancy_scatter_from_csv():
    # Read the CSV file
    df = pd.read_csv('world-happiness-report-2021.csv')

    # Create scatter plot figure
    fig = go.Figure()

    # Add scatter trace for life expectancy
    fig.add_trace(go.Scatter(
        x=df['Country name'],
        y=df['Healthy life expectancy'],
        mode='markers',
        marker=dict(
            size=12,
            color=df['Ladder score'],  # Color points by happiness score
            colorscale='Viridis',  # Choose color scale
            colorbar=dict(title='Happiness Score'),  # Add color bar
            line=dict(width=1, color='DarkSlateGrey'),  # Outline marker points
        ),
        text=df['Country name'],  # Text to display on hover
        hoverinfo='text+y',
    ))

    # Customize layout
    fig.update_layout(
        title='Country Life Expectancy vs Happiness Score',
        xaxis=dict(title='Country'),
        yaxis=dict(title='Healthy Life Expectancy'),
        showlegend=False,
        template='plotly_dark',
        height=800,  # Adjust height as needed
        width=1900,  # Adjust width as needed
        margin=dict(l=50, r=50, b=100, t=100),  # Adjust margins
    )
    graph = dcc.Graph(figure=fig,style={'height': '600px', 'width': '100%'})

    return graph

def create_freedom_to_country_graph():
    # Create bar plot figure
    df = pd.read_csv('world-happiness-report-2021.csv')
    fig = px.bar(
        df,
        x='Country name',
        y='Freedom to make life choices',
        template='plotly_dark',
        title='Freedom to Make Life Choices by Country',
        labels={'Freedom to make life choices': 'Freedom Score', 'Country name': 'Country'},
        width=1000,  # Adjust width as needed
        height=600,  # Adjust height as needed
    )

    # Customize layout
    fig.update_layout(
        xaxis_title=None,
        yaxis_title='Freedom Score',
        height=1000,  # Adjust height as needed
        width=2000,
        margin=dict(l=100, r=100, t=100, b=50),  # Adjust margins
    )
    graph = dcc.Graph(figure=fig,style={'height': '600px', 'width': '150%'})

    return graph


def create_gdp_choropleth_map():
    # Read the CSV file
    df = pd.read_csv('world-happiness-report-2021.csv')

    # Create the choropleth map figure for GDP per capita
    fig = px.choropleth(
        df,
        locations='Country name',  # Column containing country names
        locationmode='country names',  # Use country names for location mode
        color='Logged GDP per capita',  # Column containing GDP per capita scores
        hover_name='Country name',  # Column to display on hover
        color_continuous_scale='Viridis',  # Choose color scale
        title='World Happiness Report - GDP per Capita',  # Title of the map
        labels={'Logged GDP per capita': 'Logged GDP per capita'},  # Custom label for the color scale
        template='plotly_dark'  # Choose plotly template
    )

    # Create a dcc.Graph component to render the choropleth map
    graph = dcc.Graph(figure=fig, style={'height': '700px', 'width': '100%'})

    return graph

def create_social_support_line_chart():

    df = pd.read_csv('world-happiness-report-2021.csv')

    df_sorted = df.sort_values(by='Social support', ascending=False)

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df_sorted['Country name'], y=df_sorted['Social support'], mode='lines', name='Social Support'))


    fig.update_layout(title='Social Support by Country', xaxis={'tickangle': 45})

    graph = dcc.Graph(figure=fig, style={'height': '600px', 'width': '100%'})

    return graph

def create_corruption_bar_chart():

    df = pd.read_csv('world-happiness-report-2021.csv')


    avg_corruption = df.groupby('Regional indicator')['Perceptions of corruption'].mean().reset_index()


    fig = px.bar(avg_corruption, x='Regional indicator', y='Perceptions of corruption',
                 title='Average Perceptions of Corruption by Regional Indicator',
                 labels={'Perceptions of corruption': 'Average Corruption Score', 'Regional indicator': 'Regional Indicator'},
                 template='plotly_dark')
    
    graph = dcc.Graph(figure=fig, style={'height': '600px', 'width': '100%'})

    return graph

def create_generosity_scatter_plot():

    df = pd.read_csv('world-happiness-report-2021.csv')

    fig = px.scatter(df, x='Country name', y='Generosity',
                     title='Generosity Score by Country',
                     labels={'Generosity': 'Generosity Score', 'Country name': 'Country'},
                     template='plotly_dark')
    
    fig.update_layout(xaxis_tickangle=-45)

    graph = dcc.Graph(figure=fig, style={'height': '600px', 'width': '100%'})

    return graph