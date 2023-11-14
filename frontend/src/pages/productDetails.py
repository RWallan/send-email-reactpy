from reactpy import component, html


@component
def ProductDetails():
    layout = html.div(
        {"class_name": "product-details"},
        html.h2("O Zen do Python"),
        html.p("Você irá receber o Zen do Python diretamente no seu e-mail!"),
        html.p("Tente também descobrir o easter egg abaixo!"),
        html.span("import this"),
    )

    return layout
