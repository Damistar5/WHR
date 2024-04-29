import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


''''
The ladder score represents the happiness score. Indicators include:
-Top Countries with least and most happiness. 
-Country rankings based on Healthy life expectancy. 
-Freedom to make life choices.
-GDP per capita.
-Social support.
-Perception of corruption. 
-Generosity.
'''

def create_happiness_score_choropleth_map():

    df = pd.read_csv('world-happiness-report-2021.csv')

    fig = px.choropleth(
        df,
        locations='Country name',  # Column containing country names
        locationmode='country names',  # Use country names for location mode
        color='Ladder score',  # Column containing happiness scores
        hover_name='Country name',  # Column to display on hover
        color_continuous_scale=px.colors.sequential.Plasma,  # Choose color scale
        title='World Happiness Report - Ladder Score',  # Title of the map
        labels={'Happiness Score': 'Happiness Score'},  # Custom label for the color scale
        template='plotly_dark'  # Choose plotly template
    )

    # Create a dcc.Graph component to render the choropleth map
    graph = dcc.Graph(figure=fig,style={'height': '900px', 'width': '100%'})

    return graph

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
        width=1793,  # Adjust width as needed
        margin=dict(l=50, r=50, b=100, t=100),  # Adjust margins
    )
    graph = dcc.Graph(figure=fig,style={'height': '500px', 'width': '100%'})

    return graph

def create_freedom_to_country_graph():
    df = pd.read_csv('world-happiness-report-2021.csv')
    
    # Create lollipop chart
    fig = go.Figure()

    # Create the bar part
    fig.add_trace(go.Bar(
        x=df['Freedom to make life choices'],
        y=df['Country name'],
        orientation='h',
        marker=dict(color='black'),
        name='Freedom Score'
    ))

    # Create the 'lollipop' part (circle at the end of the line)
    fig.add_trace(go.Scatter(
        x=df['Freedom to make life choices'],
        y=df['Country name'],
        mode='markers',
        marker=dict(color='red', size=8),
        name='Freedom Score'
    ))
       
    # Customize layout
    fig.update_layout(
        title='Freedom to Make Life Choices by Country',
        xaxis_title='Freedom Score',
        yaxis_title=None,
        height=900,  # Adjust height as needed
        width=1800,  #Adjust width as needed
        margin=dict(l=50, r=100, t=50, b=100),  # Adjust margins
        xaxis_tickangle=-90  # Rotate country names for better readability
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
    graph = dcc.Graph(figure=fig, style={'height': '900px', 'width': '100%'})

    return graph

def create_social_support_bar_chart():
    # Load the dataset
    df = pd.read_csv('world-happiness-report-2021.csv')

    # Sort data by 'Social support'
    df_sorted = df.sort_values(by='Social support', ascending=False)

    # Create a bar chart figure
    fig = go.Figure()

    # Add a bar trace for social support
    fig.add_trace(go.Bar(
        x=df_sorted['Country name'],
        y=df_sorted['Social support'],
        name='Social Support',
        marker_color='blue'  # You can change the color to suit your theme
    ))

    # Customize layout
    fig.update_layout(
        title='Social Support by Country',
        xaxis=dict(title='Country', tickangle=-45),
        yaxis=dict(title='Social Support Score'),
        showlegend=False,
        template='plotly_dark',
        height=900,  # Adjust height as needed
        width=1800,  # Adjust width as needed
        margin=dict(l=50, r=50, b=100, t=100)  # Adjust margins to ensure full labels are visible
    )

    # Return a Dash Graph component that contains the figure
    graph = dcc.Graph(figure=fig, style={'height': '500px', 'width': '100%'})

    return graph

def create_corruption_bar_chart():

    df = pd.read_csv('world-happiness-report-2021.csv')

    # Calculate average perceptions of corruption by regional indicator
    avg_corruption = df.groupby('Regional indicator')['Perceptions of corruption'].mean().reset_index()

      # Define a color palette for the regions
    color_discrete_map = {
        'Western Europe': 'blue',
        'North America and ANZ': 'red',
        'Middle East and North Africa': 'orange',
        'Latin America and Caribbean': 'purple',
        'Central and Eastern Europe': 'green',
        'East Asia': 'yellow',
        'Southeast Asia': 'pink',
        'South Asia': 'grey',
        'Sub-Saharan Africa': 'brown'
    }

    # Create the bar chart with customized colors
    fig = px.bar(avg_corruption, x='Regional indicator', y='Perceptions of corruption',
                 title='Average Perceptions of Corruption by Regional Indicator',
                 labels={'Perceptions of corruption': 'Average Corruption Score', 'Regional indicator': 'Regional Indicator'},
                 template='plotly_dark',
                 color='Regional indicator',
                 color_discrete_map=color_discrete_map
                 )

    # Improve layout and styling
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
        xaxis_tickangle=-45,  # Rotate labels for better readability
        showlegend=True)  # Ensure the legend is shown
        
    graph = dcc.Graph(figure=fig, style={'height': '900px', 'width': '100%'})

    return graph

def create_generosity_scatter_plot():

    df = pd.read_csv('world-happiness-report-2021.csv')

    fig = px.scatter(df, x='Country name', y='Generosity',
                     title='Generosity Score by Country',
                     labels={'Generosity': 'Generosity Score', 'Country name': 'Country'},
                     template='plotly_dark')
    
    fig.update_layout(xaxis_tickangle= -45)

    graph = dcc.Graph(figure=fig, style={'height': '800px', 'width': '100%'})

    return graph
