# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# import plotly.express as px


# Imports from this application
from app import app


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## How Happy Could You Be in 2020, the Year of Many Changes? 
            
           
            
            The reality is more than our perceptions, but our perception are certainly a part of the reality. 
            
            As we discover, it is not just about money, or how free we feel to make life choices. It also depends on whether you feel supported by your loved ones and friends, among other geopolitical factors you may perceive where you are. 
            
                  
            
            Let's Find Out!

                         
            """
        ),
       
        
        
        dcc.Link(dbc.Button('See How Happy You May Be', color='primary'), href='/Predictions')
    ],
    md=5,
)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
    
    
    
    ],
md=1,
)

column3 = dbc.Col(
    [
    #  html.Img(src='assets/ksr.png', className='img-fluid'),

    html.Img(src='assets/life_choices.png', className='img-fluid'),      ],
md=6,
)

layout = dbc.Row([column1,column2, column3])