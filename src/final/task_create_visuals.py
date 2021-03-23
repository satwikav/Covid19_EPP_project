import pathlib

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import pytask
import seaborn as sns

from src.config import BLD

scores = ["E_index_score", "R_index_score", "S_index_score"]
mobility = [
    "workplaces_percent_change_from_baseline",
    "transit_stations_percent_change_from_baseline",
    "residential_percent_change_from_baseline",
    "retail_and_recreation_percent_change_from_baseline",
]
education = mobility[:]
del education[3]
education.extend(["E_index_score"])


def create_visual_2(df):
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
        title_x=0.5,
        title_font=dict(size=20),
    )
    return fig


def create_visual_3(df):
    sns.set(font_scale=1.65, style="white")
    count = 1
    plt.subplots(figsize=(40, 30))
    plt.suptitle(
        "Deviation in Mobility from Baseline According to Level of Contact Stringency",
        size=50,
    )
    for i in scores:
        for t in mobility:
            plt.subplot(3, 4, count)
            sns.lineplot(x=df[i], y=df[t])
            count += 1
    return plt


def create_visual_5(df):
    fig = px.line(
        df,
        x="date",
        y=education,
        title="Changes in Mobility vs. School Stringency Index over Time",
        width=1200,
        height=600,
        color_discrete_sequence=px.colors.qualitative.Antique,
    )
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Baseline Changes for Various Mobility Types, in %",
        legend_title="Legend:",
        title_x=0.5,
        title_font=dict(size=20),
        legend=dict(y=0.85, x=1),
        template="simple_white",
    )
    return fig


@pytask.mark.depends_on(
    BLD / "data" / "df_visuals.csv",
)
@pytask.mark.produces(
    {
        "visual_2": BLD / "figures" / "Stringency_Index_over_time.png",
        "visual_3": BLD / "figures" / "Mobility_vs_Sub_Score_indices.png",
        "visual_5": BLD / "figures" / "Mobility_vs_Education_Sub_Score_Index.png",
    }
)
def task_create_visuals(depends_on, produces):
    data = pd.read_csv(depends_on)
    fig2 = create_visual_2(data)
    fig2.write_image(str(pathlib.Path(produces["visual_2"])), format="png")
    fig3 = create_visual_3(data)
    fig3.savefig(produces["visual_3"])
    fig5 = create_visual_5(data)
    fig5.write_image(str(pathlib.Path(produces["visual_5"])), format="png")
