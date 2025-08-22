import pandas as pd
import plotly.express as px
# import matplotlib.pyplot as plt
import numpy as np




def generate_random_signal_plot():


    # print('--------->')
    # Generate time series data
    # np.random.seed(42)
    t = np.linspace(0, 10, 700)  # time points
    signal = np.sin(t) + 0.4 * np.random.normal(size=len(t))  # sinusoid + noise

    df_signal = pd.DataFrame(data = signal, columns=['random signal'])

    df_signal.to_csv('random_signal')

    fig = px.line(df_signal,title='random signal')
    fig.update_layout(hovermode="x unified")
    fig.update_traces(mode="lines", hovertemplate=None)
    # fig.show()
    fig_for_front = fig.to_html()

    return fig_for_front