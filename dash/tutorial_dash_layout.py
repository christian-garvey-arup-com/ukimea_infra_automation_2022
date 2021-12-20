"""
SCRIPT FOR PLOTLYDASH TUTORIAL
--> **LAYOUT**

AUTHOR: C GARVEY
DATE: 2021/12/13

URL: https://dash.plotly.com/
CSS and JS to override templates: https://dash.plotly.com/external-resources
Dash core components: https://dash.plotly.com/dash-core-components 
"""

#-----------------------------------------
#----------Installation-----------
#-----------------------------------------
import dash
from dash import dcc
from dash import html
from dash import Dash, Input, Output, callback
from dash import dash_table as dt
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

#-----------------------------------------
#----------Layout (hot loading)-----------
#-----------------------------------------
"""

app = dash.Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 100],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    html.H2(children='Second header'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

# Don't like hot-reloading (i.e. automatic reload of data)? You can turn this off withapp.run_server(dev_tools_hot_reload=False)
# Visit http://127.0.0.1:8050/ in your web browser.
"""


#-----------------------------------------
#----------More about html components - APPLY COLOURS TO TEXT AND FIGURE-----
#-----------------------------------------
"""
app = dash.Dash(__name__)

# set html colours https://htmlcolorcodes.com/
colors = {
    'background': '#111111',
    'text': '#FFBF00'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

"""



#-----------------------------------------
#----------TABLES-----
#-----------------------------------------

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = dash.Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#FFBF00'
}

app.layout = html.Div([
    html.H4(children='US Agriculture Exports (2011)', style={
            'textAlign': 'center',
            'color': colors['text']
        }),
    generate_table(df),
    
])

#if __name__ == '__main__':
#    app.run_server(debug=True)



#-----------------------------------------
#----------VISULATIONS-----
#-----------------------------------------
# plots with plotly engine and library

app = dash.Dash(__name__)

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

# Call the data to plot
fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''


# Set up graphing and markdown. Graph renders interactive data visualizations using the open source plotly.js JavaScript graphing library
app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    ), 
    dcc.Markdown(children=markdown_text)
])


# run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)


#-----------------------------------------
#----------MARKDOWN-----
#-----------------------------------------

# app.layout = html.Div([
#     dcc.Markdown(children=markdown_text)
# ])


#-----------------------------------------
#----------CORE COMPONENTS - DROPDOWNS, GRAPHS-----
#-----------------------------------------
#https://dash.plotly.com/dash-core-components

app = dash.Dash(__name__)

app.layout = html.Div([
    ## NEW WRAPPER -- ALL BENEATH SECOND 'html.Div' IS 'WRAPPED' TOGETHER
    html.Div(children=[
        # introudce list of items on the dashboard which is wrapped by the html.Div fn.
        ## dropdown tool
        html.Label('Dropdown'),
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='MTL'
        ),
        ## multi-select dropdown tool
        html.Br(),
        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value=['MTL'],
            multi=True
        ),
        ## 
        html.Br(),
        html.Label('Button box'),
        dcc.RadioItems(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='MTL',
            #labelStyle={'display': 'inline-block'}
        ),
    ], style={'padding': 10, 'flex': 1}),

    ## NEW WRAPPER - SO NEW AREA ON THE DASHBOARD
    html.Div(children=[
        # checkbox tool
        html.Label('Checkboxes'),
        dcc.Checklist(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value=['MTL', 'SF']
        ),
        
        # text input bar
        html.Br(),
        html.Label('Text Input'),
        dcc.Input(value='MTL', type='text'),

        # slider tool
        html.Br(),
        html.Label('Slider'),
        dcc.Slider(
            min=0,
            max=9,
            marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
            value=5,
        ),
    ], style={'padding': 10, 'flex': 1})
], style={'display': 'flex', 'flex-direction': 'row'})

# if __name__ == '__main__':
#     app.run_server(debug=True)



#-----------------------------------------
#----------DASHTABLE - TABLES-----
#-----------------------------------------
#https://dash.plotly.com/datatable 

from dash import Dash, Input, Output, callback
from dash import dash_table as dt
import pandas as pd
import dash_bootstrap_components as dbc

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

# app = dash.Dash(__name__)

# app.layout = dash.dash_table.DataTable(
#     id='table',
#     columns=[{"name": i, "id": i} for i in df.columns],
#     data=df.to_dict('records'),
# )

# if __name__ == '__main__':
#     app.run_server(debug=True)


df = pd.read_csv('https://git.io/Juf1t')

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Label('Click a cell in the table:'),
    dt.DataTable(
        id='tbl', data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
    ),
    dbc.Alert(id='tbl_out'),
])

@callback(
    Output('tbl_out', 'children'), 
    Input('tbl', 'active_cell'))
def update_graphs(active_cell):
    return str(active_cell) if active_cell else "Click the table"

if __name__ == "__main__":
    app.run_server(debug=True)