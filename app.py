# adapted from http://github.com/plotly/dash-bio/blob/master/tests/dashbio_demos/utils/app_wrapper.py
# and http://github.com/plotly/dash-bio/blob/master/tests/dashbio_demos/app_alignment_viewer.py

import base64

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app_layout import dataset, layout

# instantiate a Dash app
app = dash.Dash(__name__)

# add some styling (CSS) if you like

page_layout = layout()

app_title = "Dash Bio demo"
app_name = "MSA"
standalone = False
bg_color = "#C71585"
font_color = "#F3F6FA"
app.layout = html.Div(
    id="main_page",
    children=[
        dcc.Location(id="url", refresh=False),
        html.Div(
            id="app-page-header",
            children=[
                html.A(
                    id="dashbio-logo",
                    children=[
                        html.Img(
                            src="data:image/png;base64,{}".format(
                                base64.b64encode(
                                    open(
                                        "./assets/plotly-dash-bio-logo.png", "rb"
                                    ).read()
                                ).decode()
                            )
                        )
                    ],
                    href="/",
                ),
                html.H2(app_title),
                html.A(
                    id="gh-link",
                    children=["source"],
                    href="https://github.com/mkcor/dashbio-demo",
                ),
            ],
            style={"background": bg_color, "color": font_color},
        ),
        html.Div(id="app-page-content", children=page_layout),
    ],
)

# add file upload/selection to data store
@app.callback(
    Output("alignment-data-store", "data"),
    [
        Input("alignment-file-upload", "contents"),
        Input("alignment-file-upload", "filename"),
    ],
)
def update_storage(contents, filename):
    if (contents is not None) and ("fasta" in filename):
        content_type, content_string = contents.split(",")
        content = base64.b64decode(content_string).decode("UTF-8")
    else:
        content = dataset

    return content


# render main chart
@app.callback(
    Output("alignment-chart", "data"), [Input("alignment-data-store", "data")]
)
def update_chart(input_data):
    return input_data


# run app (Flask server) with hot reloading
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
