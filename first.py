from dash import Dash, html, dcc, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)


app.layout = html.Div(children=[
    
    html.H1(children='Психология отношений',
#    style={
#        'textAlign': 'center',                                   Пока обходимся без стайла.    
#            'color': colors['text'],                               Потом своё состряпаю в css
#            'fontFamily': 'Comic Sans MS'
#            }
            ),


#Контейнер Div для каждой кнопки, чтоб одна над другой была
#Теперь нужно придумать, как им функции добавить и куда они должны отправлять... 
    html.Div(
        html.Button('Вход', id='button', n_clicks=0)         
    ),

    html.Div(
        html.Button('Регистрация', id='button', n_clicks=0)
    )
                        ]
            )


#инфа про layout DASH:   https://dash.plotly.com/layout          
#инфа про кнопки: https://dash.plotly.com/dash-html-components/button
#Дальше, видимо, делаем отдельную функцию (или функции?) для кнопок
#    def блаблабла 
                

if __name__ == '__main__':
    app.run_server(debug=True)