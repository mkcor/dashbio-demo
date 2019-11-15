# adapted from http://github.com/plotly/dash-bio/blob/master/tests/dashbio_demos/app_alignment_viewer.py

import base64
import json
import os

import dash_core_components as dcc
import dash_html_components as html
from dash_bio import AlignmentViewer


with open("./data/drosophila.fasta", encoding="utf-8") as data_file:
    dataset = data_file.read()


def layout():
    return html.Div(
        id="alignment-body",
        className="app-body",
        children=[
            html.Div(
                [
                    html.Div(
                        id="alignment-control-tabs",
                        className="control-tabs",
                        children=[
                            dcc.Tabs(
                                id="alignment-tabs",
                                value="what-is",
                                children=[
                                    dcc.Tab(
                                        label="About",
                                        value="what-is",
                                        children=html.Div(
                                            className="control-tab",
                                            children=[
                                                html.H4(
                                                    className="what-is",
                                                    children="Building custom analytics web apps for bioinformatics with Plotly’s Dash Bio",
                                                ),
                                                html.P(
                                                    """
                                                    Why Dash?
                                                    Why Dash Bio?
                                                    Today we shall focus on sequencing tools.
                                                    """
                                                ),
                                                html.Ul(
                                                    [
                                                        html.Li(
                                                            "The Plotly Team @plotly"
                                                        ),
                                                        html.Li(
                                                            "Shammamah Hossain @shammamah"
                                                        ),
                                                        html.Li(
                                                            "Marianne Corvellec @mkcor"
                                                        ),
                                                    ]
                                                ),
                                                html.P(
                                                    """
                                                    Multiple Sequence Alignment (MSA) is
                                                    used to align multiple (at least three) DNA or protein sequences.
                                                    The data are contained in a multi-FASTA file.
                                                    """
                                                ),
                                                html.P(
                                                    """
                                                    Find more about the MSA component at
                                                    https://github.com/plotly/react-alignment-viewer.
                                                    """
                                                ),
                                            ],
                                        ),
                                    ),
                                    dcc.Tab(
                                        label="Data",
                                        value="alignment-tab-select",
                                        children=html.Div(
                                            className="control-tab",
                                            children=[
                                                html.Div(
                                                    className="app-controls-block",
                                                    children=[
                                                        html.Div(
                                                            className="fullwidth-app-controls-name",
                                                            children="Upload data in multi-FASTA format",
                                                        ),
                                                        html.Div(
                                                            id="alignment-file-upload-container",
                                                            children=[
                                                                dcc.Upload(
                                                                    id="alignment-file-upload",
                                                                    className="control-upload",
                                                                    children=html.Div(
                                                                        [
                                                                            "Click here to select a data file"
                                                                        ]
                                                                    ),
                                                                )
                                                            ],
                                                        ),
                                                    ],
                                                )
                                            ],
                                        ),
                                    ),
                                    dcc.Tab(
                                        label="Graph",
                                        value="control-tab-customize",
                                        children=html.Div(
                                            [
                                                dcc.Loading(
                                                    className="dashbio-loading",
                                                    children=html.Div(
                                                        [
                                                            AlignmentViewer(
                                                                id="alignment-chart",
                                                                height=725,
                                                                data=dataset,
                                                            )
                                                        ]
                                                    ),
                                                ),
                                                dcc.Store(id="alignment-data-store"),
                                            ]
                                        ),
                                    ),
                                    dcc.Tab(
                                        label="Acknowledgments",
                                        value="control-tab-select2",
                                        children=html.Div(
                                            className="control-tab",
                                            children=[
                                                html.Div(
                                                    className="app-controls-name",
                                                    children="Thank you!",
                                                ),
                                                html.Ul(
                                                    [
                                                        html.Li(
                                                            "Gian Marco Franceschini @GMFranceschini"
                                                        ),
                                                        html.Li(
                                                            "Kamil Slowikowski @slowkow"
                                                        ),
                                                        html.Li(
                                                            "Austin Davis-Richardson @audy"
                                                        ),
                                                        html.Li(
                                                            "Germain Salvato Vallverdu @gVallverdu"
                                                        ),
                                                    ]
                                                ),
                                                html.Div(id="alignment-events"),
                                            ],
                                        ),
                                    ),
                                ],
                            )
                        ],
                    )
                ]
            )
        ],
    )


COLORSCALES_DICT = [
    {"value": "clustal2", "label": "Clustal2"},
    {"value": "clustal", "label": "Clustal"},
    {"value": "nucleotide", "label": "Nucleotide"},
]

CONSERVATION_COLORS_OPT = [
    "Blackbody",
    "Bluered",
    "Blues",
    "Earth",
    "Electric",
    "Greens",
    "Greys",
    "Hot",
    "Jet",
    "Picnic",
    "Portland",
    "Rainbow",
    "RdBu",
    "Reds",
    "Viridis",
    "YlGnBu",
    "YlOrRd",
]

GAP_COLORS_OPT = [
    "black",
    "grey",
    "white",
    "turquoise",
    "blue",
    "green",
    "red",
    "purple",
]
