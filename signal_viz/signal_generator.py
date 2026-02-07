import pandas as pd
import plotly.express as px
import numpy as np


def generate_random_sequence():
    t = np.linspace(0, 10, 700)
    signal = np.sin(t) + 0.4 * np.random.normal(size=len(t))
    new_arr = []
    for i in range(0, len(t)):
        new_arr.append([i, signal[i]])

    df_signal = pd.DataFrame(data=new_arr, columns=["time", "Random Signal"])

    return df_signal


def generate_random_signal_plot(df_signal):
    fig = px.line(x=df_signal['time'], y=df_signal['Random Signal'], title='random signal')
    fig.update_layout(hovermode="x unified")
    fig.update_traces(mode="lines", hovertemplate=None)
    fig_for_front = fig.to_html()

    return fig_for_front
