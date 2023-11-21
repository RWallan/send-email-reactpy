from reactpy import component, hooks, html


@component
def ProductDetails(context: hooks.Context[hooks._Type]):
    context = hooks.use_context(context)
    layout = html.div(
        {"class_name": "product-details"},
        html.h2("O Zen do Python"),
        html.p(
            f"Olá{' ' + context['firstNameShared'] if context['firstNameShared'] else ''}. " # noqa E501
            "Você irá receber o Zen do Python diretamente no seu e-mail!"
        ),
        html.p("Tente também descobrir o easter egg abaixo!"),
        html.span("import this"),
    )

    return layout
