# Import necessary libraries
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from layout import create_choropleth_map as map,display_clickable_container as cont,create_life_expectancy_scatter_from_csv as life, create_freedom_to_country_graph as free,create_gdp_choropleth_map as gdp,create_social_support_line_chart as social,create_corruption_bar_chart as cor,create_generosity_scatter_plot as gen

# Create Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], suppress_callback_exceptions=True)

# Navbar component
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row([
                    dbc.Col(
                        html.A(html.Img(src='assets/SNice.svg.png', height="40px",),href="/home")),
                        dbc.Col(dbc.NavbarBrand("World Happiness Report",className='ms-2',style={'color':'#00FF00','font-family':'Ultra, serif'}))
                ],
                align='center',
                className='g-0'
                ),
            dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink("Happiness Score", active='exact', href="/happinessscore")),
                        dbc.NavItem(dbc.NavLink("Life Expectancy", active='exact', href="/lifeexpectancy")),
                        dbc.NavItem(dbc.NavLink("Freedom", active='exact', href="/freedom")),
                        dbc.NavItem(dbc.NavLink("GDP Per Capita", active='exact', href="/gdppercapita")),
                        dbc.NavItem(dbc.NavLink("Social Support", active='exact', href="/socialsupport")),
                        dbc.NavItem(dbc.NavLink("Corruption", active='exact', href="/corruption")),
                         dbc.NavItem(dbc.NavLink("Generosity", active='exact', href="/generosity")),
                    ],
                    className="me-auto",
                    navbar=True,
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in range(3):  # Adjust the range to include all relevant indices, starting from 2
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)


# Set layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content', style={'backgroundColor': '#C0DFF3'})
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/happinessscore':
        return map()
    elif pathname =='/lifeexpectancy':
        return life()
    elif pathname == '/freedom':
        return free()
    elif pathname =='/gdppercapita':
        return gdp()
    elif pathname =='/socialsupport':
        return social()
    elif pathname =='/corruption':
        return cor()
    elif pathname =='/generosity':
        return gen()
    else:
        return map()

if __name__ == '__main__':
    app.run_server(port=8050, debug=True)
