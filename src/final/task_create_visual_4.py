import pathlib

import pandas as pd
import plotly.express as px
import pytask

from src.config import BLD

baselines = [
    "workplaces_percent_change_from_baseline",
    "transit_stations_percent_change_from_baseline",
    "residential_percent_change_from_baseline",
    "retail_and_recreation_percent_change_from_baseline",
    "grocery_and_pharmacy_percent_change_from_baseline",
]
titles = [
    "Workplaces",
    "Transit Stations",
    "Residential",
    "Retail and Recreation",
    "Grocery and Pharmacy",
]
colours = ["#547482", "#C87259", "#F1B05D", "#7A8C87", "#C8B05C"]


def create_visual_4(df, baseline, title, colour):
    fig = px.line(
        df,
        x="date",
        y=[baseline, "stringency_index_score"],
        title="Comparison of %s Mobility Trend with Aggregate Stringency Index over Time"
        % title,
        width=1200,
        height=600,
        color_discrete_sequence=[colour, "#3C2030"],
        template="simple_white",
    )
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Baseline Change for %s Mobility, in %%" % title,
        legend_title="Legend:",
        legend=dict(y=0.75, x=1),
        title_x=0.5,
        title_font=dict(size=20),
    )
    return fig


specifications = [
    (
        BLD / "data" / "df_visuals.csv",
        BLD / "figures" / f"{title}_vs_Stringency_Index.png",
        baseline,
        title,
        colour,
    )
    for baseline, title, colour in zip(baselines, titles, colours)
]


@pytask.mark.parametrize("depends_on,produces, baseline,title,colour", specifications)
def task_create_visual_4(depends_on, produces, baseline, title, colour):
    data = pd.read_csv(depends_on)
    fig = create_visual_4(data, baseline, title, colour)
    fig.write_image(str(pathlib.Path(produces)), format="png")
