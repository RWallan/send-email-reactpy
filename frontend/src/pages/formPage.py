from reactpy import component, event, hooks, html
from src.components.Input.PrimaryInput import PrimaryInput, PrimaryInputProps
from src.components.Submit.SubmitButton import SubmitButton, SubmitButtonProps
from src.components.Submit.submitMessage import SubmitMessage
from src.hooks.useIdentityMutation import use_identity_mutation
from src.models.person_data import PersonData


@component
def FormPage(context: hooks.Context[hooks._Type]):
    email, setEmail = hooks.use_state("")
    firstName, setFirstName = hooks.use_state("")
    secondName, setSecondName = hooks.use_state("")

    disabled, setDisabled = hooks.use_state(False)
    loading, setLoading = hooks.use_state(False)

    submitMessage, setSubmitMessage = hooks.use_state("")
    context = hooks.use_context(context)

    def FirstNameChangeHandler(event):
        setFirstName(event["target"]["value"])
        context["setFirstNameShared"](event["target"]["value"])

    @event(prevent_default=True)
    async def submit(event):
        setLoading(True)
        setDisabled(True)
        setSubmitMessage("")

        response, isSuccess = await use_identity_mutation(
            PersonData(
                firstName=firstName, secondName=secondName, email=email
            ),
        )

        setSubmitMessage(SubmitMessage(response, isSuccess))
        setDisabled(False)
        setLoading(False)

    layout = html.form(
        {"method": "post", "on_submit": submit},
        html.div(
            {"class_name": "name-form-container"},
            PrimaryInput(
                PrimaryInputProps(
                    name="First Name",
                    value=firstName,
                    onChange=FirstNameChangeHandler,
                    label="Nome*",
                    placeholder="John",
                )
            ),
            PrimaryInput(
                PrimaryInputProps(
                    name="Second Name",
                    value=secondName,
                    onChange=lambda event: setSecondName(
                        event["target"]["value"]
                    ),
                    label="Sobrenome*",
                    placeholder="Doe",
                )
            ),
        ),
        PrimaryInput(
            PrimaryInputProps(
                name="Email",
                value=email,
                onChange=lambda event: setEmail(event["target"]["value"]),
                label="Digite o seu e-mail*",
                placeholder="example@email.com",
                type="email",
            )
        ),
        SubmitButton(SubmitButtonProps(loading=loading, disabled=disabled)),
        submitMessage,
    )

    return layout
