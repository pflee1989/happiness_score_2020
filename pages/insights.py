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
        
            ## Insights
            
            The pircure below demonstrates the importance of each factor. The tags for the nation state are removed because of data 
            
            leakage issues. The graph clearly shows that the level of social support, mostly shown in generosity to family and loved
            
            ones, is colinear with perceived freedom to make life choices. In the grand scheme, when one is free to make life choices, 
            
            and is supported by loved ones and friends to pursue happiness, that person is likely to be happy. Namely, if you live in 
            
            a loving and stable network, you are more than likely to feel very happy, to the maximal degree that intervening variables
            
            such as, regional (gropolitical) factors, would allow so.
            
             
            
             
            
                      
             

            """
        
        ), 
    
    # html.Img(src='assets/Rating Distribution.PNG', className='img-fluid'),

    html.Img(src='assets/Permutation_Importances.png', className='img-fluid')
    
    ],
)



       
layout = dbc.Row([column1])