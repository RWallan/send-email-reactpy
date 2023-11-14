from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from src.mail import EmailAPI
from src.models import OutputMessage, PersonData

app = FastAPI(
    title="Enviar Zen do Python por E-mail",
    description="API que envia o Zen do Python por e-mail.",
    contact={
        "name": "Richard Wallan", "url": "mailto:3am.richardwallan@gmail.com"
    },
    docs_url="/"
)

ORIGINS = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post(
    "/send-mail",
    status_code=status.HTTP_201_CREATED,
    response_model=OutputMessage
)
async def send_zen(person_data: PersonData):
    email = EmailAPI()

    has_sended = await email.send_email(
        person_data.firstName, person_data.secondName, person_data.email
    )

    if not has_sended:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Algo de errado aconteceu. Tente novamente mais tarde!"
        )

    return OutputMessage(detail="Em breve você receberá um e-mail.")
