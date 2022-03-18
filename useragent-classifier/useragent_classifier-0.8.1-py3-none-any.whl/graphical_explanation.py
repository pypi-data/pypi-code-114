import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
from typing import Dict, Any
import json
import plotly.graph_objects as go
from dash import Dash, html, dcc

def _df_to_plotly_table(df: pd.DataFrame) -> go:

    fig = go.Table(
        header=dict(values=[f"User Agent (found {df.shape[0]})", "Cluster"],
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[df.ua, df.cluster],
                fill_color='lavender',
                align='left'),
    )
    
    return fig

def produce_graph(importances: Dict[str, Any], predicted: pd.DataFrame, width: int=1500, height: int = 5000):

    df = pd.DataFrame(importances)
    df = df.reset_index()

    df = df.melt(id_vars=['index'], value_vars=[x for x in df.columns if x != "index"])

    df = df.rename(columns={"index": "Word/ngram", "variable": "cluster", "value": "importance_score"})

    n_unique_cluster = df.cluster.nunique()

    fig = make_subplots(rows=n_unique_cluster, cols=2,
                        # shared_xaxes=False, 
                        # shared_yaxes=False, 
                        subplot_titles=[f"Cluster {i}" for i in range(n_unique_cluster) for _ in range(2)],
                        x_title="Word / ngram",
                        y_title="Importance",
                        specs=[[{"type": "bar"}, {"type": "table"}] for _ in range(n_unique_cluster)]
                        )
    fig.update_layout(width=width, height=height)

    for cluster in df.cluster.unique():
        data = df.loc[df.cluster == cluster]
        data = data.dropna()
        data = data.sort_values(by="importance_score", ascending=False)

        preds = predicted.loc[predicted.cluster == cluster, :]

        fig.add_trace(
            px.bar(data, x='Word/ngram', y='importance_score', width=width, height=height).data[0],
            row=cluster+1, col=1
        )
        fig.add_trace(_df_to_plotly_table(preds), row=cluster+1, col=2)

    return fig

def run_server(importances: Dict[str, Any], predicted: pd.DataFrame):

    app = Dash(__name__)

    app.layout = html.Div(children=[
        html.H1(children='User-Agent Cluster Explanation'),

        html.Div(children='''
            A simple web app explaining User Agent clusters.
        '''),

        dcc.Graph(
            id='example-graph',
            figure=produce_graph(importances, predicted),
            style={"overflow": "scroll", 'height': 'auto', "width": "auto"},
        )
    ])

    app.run_server(debug=True)
    