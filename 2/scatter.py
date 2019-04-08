import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(21)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(x=random_x,y=random_y,mode='markers',marker=dict(
                    size=4,
                    color='rgb(255,155,44)',
                    symbol='pentagon',
                    line={'width':12}
                    ))]

layout = go.Layout(title='The plot', xaxis={'title':'X AXIS'},yaxis=dict(title='Y AXIS'),hovermode='closest')

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='scatter.html')
