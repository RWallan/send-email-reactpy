from enum import Enum

from reactpy import component, html


class AlignEnum(Enum):
    left_loading: int = 0
    center_loading: int = 1
    right_loading: int = 2


@component
def PrimaryLoading(align: AlignEnum):
    layout = html.div(
        {"class_name": AlignEnum(align).name},
        html.div(
            {"class_name": "lds-ellipsis"},
            html.div(),
            html.div(),
            html.div(),
            html.div(),
        ),
    )
    return layout
