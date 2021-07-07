# Imports from 3rd party libraries
# import joblib
from joblib import load
import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# from joblib import load
# pipeline = load('assets/pipeline.joblib')

# Imports from this application
from app import app


model = load('assets/pipeline')

regional_indicators = ["Western Europe", "North America, Australia, and New Zeeland",
"Middle East and North Africa",           
"Latin America and Caribbean",            
"Central and Eastern Europe",
"East Asia",                              
"Southeast Asia",                         
"Commonwealth of Independent States",     
"Sub-Saharan Africa",                     
"South Asia"]

# sub_category_list = []

column1 = dbc.Col(
    [
        dcc.Markdown('''###### Region'''),
         dcc.Dropdown(
        id='Regional_indicator',
        options=[
        {'label': i, 'value': i} for i in regional_indicators
       ],
        value='Western Europe',
        className='mb-4'), 

        
    #     dcc.Markdown('''###### Sub Category'''),
    #      dcc.Dropdown(
    #     id='sub-category-dropdown',
    #     options=[
    #     {'label': i, 'value': i} for i in sub_category_list
    #    ],
    #     value='diy',
    #     className='mb-4'), 


        dcc.Markdown('''###### Social Suppoer'''),
        dcc.Slider(
            id='Social_support',
            min=0,
            max=1,
            step=.01,
            value=0,
        ),
        dcc.Markdown('', id='Social-Support-container'),
        
        dcc.Markdown('''###### Freedeom to Make Life Choices'''),
        dcc.Slider(
            id='Freedom_to_make_life_choices',
            min=0,
            max=1,
            step=.01,
            value=0,
        ),
        dcc.Markdown('', id='Freedom-Life-Choice-container'),
               

        ],
    )

column2 = dbc.Col(
    [
        dcc.Markdown('''###### Healthy Life Expectancy'''),
        dcc.Slider(
            id='Healthy_life_expectancy',
            min=0,
            max=82,
            step=.5,
            value=20,
        ),
        dcc.Markdown('', id='Life-Expectancy-slider-container'),


        dcc.Markdown('''###### Generosity (Charity Giving)'''),
        dcc.Slider(
            id='Generosity',
            min=0,
            max=1,
            step=.01,
            value=0,
        ),
        dcc.Markdown('', id='Generosity-slider-container'),

        dcc.Markdown('''###### Logged GDP Per Capita'''),
        dcc.Slider(
            id='Logged_GDP_per_capita',
            min=0,
            max=12,
            step=.1,
            value=0,
        ),
        dcc.Markdown('', id='GDP-container'),
        # dcc.Markdown('',id='prediction-content', style={
        # 'textAlign':'center',
        # 'font-size':30}), 

        # html.H2('Possibility of Success', className='mb-5'),
        # html.Div(id='prediction-content', className='lead') 
        dcc.Markdown('''###### Perceived Level of Corruption'''),
        dcc.Slider(
            id='Perceptions_of_corruption',
            min=0,
            max=1,
            step=.01,
            value=0,
        ),
        dcc.Markdown('', id='Perceptions-of-Corruption-container'),

        ],
    
    )

column3 = dbc.Col(
    [
        
        # dcc.Markdown('',id='prediction-content', style={
        # 'textAlign':'center',
        # 'font-size':30}), 

        html.H2('How Happy Do you Feel?', className='mb-5'),
        html.Div(id='prediction-content', className='lead') 
        
        ],
    
    )


# Takes inputs from user and returning to show their selection
@app.callback(
    dash.dependencies.Output('GDP-container', 'children'),
    [dash.dependencies.Input('Logged_GDP_per_capita', 'value')])
def update_output(value):
    return 'Logged Per Capita GDP: "{}" Out of 12'.format(value)

@app.callback(
    dash.dependencies.Output('Social-Support-container', 'children'),
    [dash.dependencies.Input('Social_support', 'value')])
def update_output(value):
    return 'Average Perceived Social Support: "{}" Out of 1.'.format(value)

@app.callback(
    dash.dependencies.Output('Freedom-Life-Choice-container', 'children'),
    [dash.dependencies.Input('Freedom_to_make_life_choices', 'value')])
def update_output(value):
    return 'Average Perceived Freedom to Make Life Choices: "{}" Out of 1.'.format(value)

@app.callback(
    dash.dependencies.Output('Life-Expectancy-slider-container', 'children'),
    [dash.dependencies.Input('Healthy_life_expectancy', 'value')])
def update_output(value):
    return 'Expected, on Avereage, to Live "{}" Years'.format(value)

@app.callback(
    dash.dependencies.Output('Perceptions-of-Corruption-container', 'children'),
    [dash.dependencies.Input('Perceptions_of_corruption', 'value')])
def update_output(value):
    return 'Perceived Level of Corruption: "{}" Out of 1.'.format(value)

@app.callback(
    dash.dependencies.Output('Generosity-slider-container', 'children'),
    [dash.dependencies.Input('Generosity', 'value')])
def update_output(value):
    return 'Average Score of Charity Giving: "{}" Out of 1.'.format(value)


@app.callback(
    Output('prediction-content','children'),
    [ Input('Generosity', 'value'),
      Input('Regional_indicator', 'value'),
      Input('Logged_GDP_per_capita', 'value'),
      Input('Social_support', 'value'),
      Input('Healthy_life_expectancy', 'value'),
      Input('Freedom_to_make_life_choices', 'value'),
      Input('Perceptions_of_corruption', 'value')
     ])

def predict(Generosity, Regional_indicator, Logged_GDP_per_capita,
       Social_support, Healthy_life_expectancy,
       Freedom_to_make_life_choices, Perceptions_of_corruption):
    df = pd.DataFrame(
        columns=['Generosity', 'Regional_indicator', 'Logged_GDP_per_capita',
       'Social_support', 'Healthy_life_expectancy',
       'Freedom_to_make_life_choices', 'Perceptions_of_corruption'],
        data=[[Generosity, Regional_indicator, Logged_GDP_per_capita,
       Social_support, Healthy_life_expectancy,
       Freedom_to_make_life_choices, Perceptions_of_corruption]])
    y_pred = model.predict(df)[0]
    # y_pred_prob = model.predict_proba(df)[0]*100 .format(round(y_pred_prob[1],2))
    if y_pred <= 3:
        return "Feeling {} out of 8: You're Not Too Happy".format(round(y_pred,2))
    elif y_pred > 3 and y_pred <=5:
        return "Feeling {} out of 8: You May Be Happy".format(round(y_pred,2))
    elif y_pred > 5 and y_pred <=6:
        return "Feeling {} out of 8: You Are Happy".format(round(y_pred,2))
    else:
        return "Feeling {} out of 8: You Are (Likely Very) Happy".format(round(y_pred,2))
    # else:
    #     return "This campaign is {}% likely to fail.".format(round(y_pred_prob[1],2))
layout = dbc.Row([column1, column2, column3])