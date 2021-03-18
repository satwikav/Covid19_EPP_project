import pathlib

import pandas as pd
import plotly.express as px
import pytask

from src.config import BLD


def plot_visual_1(df, path):
    fig = px.bar(
        df,
        x="date",
        y="stringency_index_score",
        color="stringency_index_score",
        labels={"stringency_index_score": "Heat Magnitude"},
        title="Level of Aggregate Contact Stringency Index over Time",
        width=1000,
        height=600,
        template="simple_white",
    )
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Aggregate Stringency Index",
        legend_title="Aggregate Stringency Index",
        font=20,
    )
    fig.write_image(str(pathlib.Path(path)), format="png")


@pytask.mark.depends_on(BLD / "data" / "df_visuals.csv")
@pytask.mark.produces(BLD / "figures" / "visual_1.png")
def task_visuals(depends_on, produces):
    data = pd.read_csv(depends_on)
    plot_visual_1(data, produces)
