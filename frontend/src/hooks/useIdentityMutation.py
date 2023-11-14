import httpx
from src.models.person_data import PersonData


async def post_data(data: PersonData):
    async with httpx.AsyncClient() as client:
        return await client.post(
            "http://localhost:8000/send-mail",
            json=data.model_dump(),
            timeout=30,
        )


async def use_identity_mutation(data: PersonData):
    isSuccess = True

    result = await post_data(data)
    response = result.json()

    if result.status_code == 500:
        isSuccess = False
    elif result.status_code == 422:
        response = {"detail": "Os seus dados foram enviados incorretamente."}
        isSuccess = False

    return (response.get("detail"), isSuccess)
