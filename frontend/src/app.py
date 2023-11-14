from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from reactpy import component, html
from reactpy.backend.fastapi import Options, configure
from src.pages import FormPage, ProductDetails

app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")


@component
def App():
    app = html.div(
        {"class_name": "container"},
        FormPage(),
        ProductDetails(),
    )

    return app


configure(
    app,
    App,
    options=Options(
        head=html.head(
            html.title("Send Email With ReactPy"),
            html.link({"href": "/static/index.css", "rel": "stylesheet"}),
            html.meta({"charset": "utf-8"}),
            html.meta(
                {
                    "name": "viewport",
                    "content": "width=device-width, initial-scale=1",
                }
            ),
            html.link(
                {
                    "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css",  # noqa E501
                    "rel": "stylesheet",
                    "integrity": "sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN",  # noqa E501
                    "crossorigin": "anonymous",
                }
            ),
            html.script(
                {
                    "src": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js",  # noqa E501
                    "integrity": "sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL",  # noqa E501
                    "crossorigin": "anonymous",
                }
            ),
        )
    ),
)
