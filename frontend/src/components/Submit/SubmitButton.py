from pydantic.dataclasses import dataclass
from reactpy import component, html
from src.components.Loading.PrimaryLoading import AlignEnum, PrimaryLoading


@dataclass
class SubmitButtonProps:
    loading: bool
    disabled: bool


@component
def SubmitButton(props: SubmitButtonProps):
    layout = html.button(
        {
            "class_name": "btn btn-dark",
            "type": "submit",
            "disabled": props.disabled,
        },
        PrimaryLoading(AlignEnum.center_loading)
        if props.loading
        else "Enviar!",
    )

    return layout
