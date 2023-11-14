from enum import Enum

from reactpy import component, html


class SuccessEnum(Enum):
    success: bool = True
    danger: bool = False


@component
def SubmitMessage(message: str, isSuccess: bool):
    success_type = SuccessEnum(isSuccess).name
    if isSuccess:
        color = "green"
    else:
        color = "red"

    layout = html.div(
        {
            "class_name": f"alert alert-{success_type}",
            "role": "alert",
            "style": "padding: 0 4px; margin-top: 4px",
        },
        html.div(
            {"style": f"color: {color}"},
            message,
        ),
    )

    return layout
