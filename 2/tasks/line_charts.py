import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../../Data/2010YumaAZ.csv')
days = [
'TUESDAY',
'WEDNESDAY',
'THURSDAY',
'FRIDAY',
'SATURDAY',
'SUNDAY',
'MONDAY']

data = []

for day in days:

    df2 = df[df['DAY'] == day]
    lst_time = df2['LST_TIME']
    t_hr_avg = df2['T_HR_AVG']

    trace = go.Scatter(x=lst_time,
                        y=t_hr_avg,
                        mode='lines',
                        name=day)
    data.append(trace)

layout = go.Layout(title='Daily temperature from June 1-7, 2010 in Yuma Arizona')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)
