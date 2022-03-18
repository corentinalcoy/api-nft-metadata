from fastapi import FastAPI, HTTPException

app = FastAPI()

metadata = [
    {
        "id": 0,
        "description": "Beans Loyalty program",
        "image": "https://bnsre.s3.amazonaws.com/static-v3/connect/img/app/logo-full-liana.svg",
        "name": "Beans Loyalty",
    },
    {
        "id": 1,
        "description": "Beans Referral program",
        "image": "https://bnsre.s3.amazonaws.com/static-v3/connect/img/app/logo-full-bamboo.svg",
        "name": "Beans Referral",
    },
    {
        "id": 2,
        "description": "Beans Email program",
        "image": "https://bnsre.s3.amazonaws.com/static-v3/connect/img/app/logo-full-foxx.svg",
        "name": "Beans Email",
    },
    {
        "id": 3,
        "description": "Beans Popup program",
        "image": "https://bnsre.s3.amazonaws.com/static-v3/connect/img/app/logo-full-poppy.svg",
        "name": "Beans Loyalty",
    },
    {
        "id": 4,
        "description": "Beans Widget program",
        "image": "https://bnsre.s3.amazonaws.com/static-v3/connect/img/app/logo-full-snow.svg",
        "name": "Beans Widget",
    },
    {
        "id": 6,
        "description": "Beans Social Connect Program ",
        "image": "https://bnsre.s3.amazonaws.com/static-v3/connect/img/app/logo-full-arrow.svg",
        "name": "Beans Social Connect",
    },
]


@app.get("/trellix/metadata")
async def list_metadata():
    return metadata


@app.get("/trellix/metadata/{pk}")
async def read_metadata(pk: int):
    if pk > len(metadata) - 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return metadata[pk]
