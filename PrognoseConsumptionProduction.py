#plottet die Prognose bestehend aus Verbrauch und Erzeugung
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime

def plotPrognose(productionDF, consumptionDF):
    
    prog2030 = consumptionDF[['Datum', 'Anfang', 'Verbrauch [kWh]']].copy()
    buf = productionDF[productionDF['Datum'].dt.year == 2022]
    prog2030['Total Production[kWh]'] = buf['Total Production'] * 1000
    
    # Create traces
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x=prog2030['Datum'], y=prog2030['Verbrauch [kWh]'],
    mode='lines',
    name='Verbrauch',
    line=dict(color='red')))
    
    fig.add_trace(go.Scatter(x=prog2030['Datum'], y=prog2030['Total Production[kWh]'],
    mode='lines',
    name='Total Production',
    line=dict(color='blue')))
    
    fig.show()

    oneDayPlot(prog2030)

    print(prog2030)
    print("Prognose geplottet (hoffentlich)")

def oneDayPlot(prog2030):
    selected_date_str = input("geben Sie das Datum im Format TT.MM.JJJJ ein: ")
    selected_date = datetime.strptime(selected_date_str, "%d.%m.%Y")

    # Create a new Plotly subplot figure
    fig = make_subplots()

    # Add the energy consumption trace
    fig.add_trace(
        go.Scatter(
            x=prog2030['Anfang'].dt.strftime('%H:%M'), 
            y=prog2030['Verbrauch [kWh]'],
            mode='lines',
            name='Total Consumption',
            fill='tozeroy'
        )
    )

    # Add the renewable energy production trace
    fig.add_trace(
        go.Scatter(
            x=prog2030['Anfang'].dt.strftime('%H:%M'),
            y=prog2030['Total Production[kWh]'],
            mode='lines',
            name='Total Renewable Production',
            fill='tozeroy'
        )
    )


    fig.update_layout(
        title=f'Energy Production and Consumption on {selected_date}',
        xaxis=dict(title='Time (hours)'),
        yaxis=dict(title='Energy (MWh)'),
        showlegend=True
    )


    # Show the plot using st.plotly_chart
    fig.show()

