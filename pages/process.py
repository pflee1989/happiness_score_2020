# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process

            You may have found this graph for social support below almost identical to that of freedom to make life choices. You are right. 
            
            As, we examined the relationship between social support and region, we found the most indicative factor, social support, also
            
            determined by region. This makes sense-- some regions offer more stable social networks than others do. I must clarify that 
            
            some Eastern cultures may express happiness in more reserved manner. Thus, our numbers may be lower than the perceived  
            
            level of happiness, or freedom to make life choices, or social support. 

            """
        ),
        html.Img(src='assets/Social_Support_and_Refion.png', className='img-fluid'),
    ],
    
)

layout = dbc.Row([column1])