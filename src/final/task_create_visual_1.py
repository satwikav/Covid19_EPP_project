import pathlib

import pandas as pd
import plotly.express as px
import pytask

from src.config import BLD

scores = ["E_index_score", "R_index_score", "S_index_score"]
titles = ["Schools", "Private Gatherings", "Public Activities"]


def create_visual_1(df, score, title):
    fig = px.line(
        df,
        x="date",
        y=score,
        title="Level of Contact Stringency for %s over Time" % title,
        width=1000,
        height=600,
        template="simple_white",
        color_discrete_sequence=px.colors.qualitative.Antique,
    )
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="%s Stringency Index" % title,
        title_x=0.5,
        title_font=dict(size=20),
    )
    return fig


specifications = [
    (
        BLD / "data" / "df_visuals.csv",
        BLD / "figures" / f"Stringency_Index_for_{title}.png",
        score,
        title,
    )
    for score, title in zip(scores, titles)
]


@pytask.mark.parametrize("depends_on,produces, score, title", specifications)
def task_create_visual_1(depends_on, produces, score, title):
    data = pd.read_csv(depends_on)
    fig = create_visual_1(data, score, title)
    fig.write_image(str(pathlib.Path(produces)), format="png")
