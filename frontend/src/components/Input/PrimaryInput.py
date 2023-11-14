from typing import Callable, Literal

from pydantic.dataclasses import dataclass
from reactpy import component, html


@dataclass
class PrimaryInputProps:
    name: str
    value: str
    onChange: Callable
    label: str
    placeholder: str
    type: Literal["text", "password", "email"] = "text"


@component
def PrimaryInput(props: PrimaryInputProps):
    layout = html.div(
        {"class_name": "input-container"},
        html.label(
            {
                "for": "exampleInputEmail",
                "class_name": "label",
            },
            props.label,
        ),
        html.input(
            {
                "class_name": "form-control",
                "type": props.type,
                "id": "exampleInputEmail",
                "name": props.name,
                "value": props.value,
                "on_change": props.onChange,
                "placeholder": props.placeholder,
                "required": True,
            }
        ),
    )

    return layout
