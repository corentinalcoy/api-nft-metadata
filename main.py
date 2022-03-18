from fastapi import FastAPI, HTTPException

app = FastAPI()

metadata = [
    {
        "id": 0,
        "description": "Beans Loyalty program",
        "image": "https://bnsre.s3.amazonaws.com/static-v3/connect/img/app/logo-full-liana.svg",
        "name": "Beans Loyalty",
        "attributes": [{"key": "title", "value": "liana"}],
    },
    {
        "id": 1,
        "description": "Beans Referral program",
        "image": "https://bnsre.s3.amazonaws.com/static-v3/connect/img/app/logo-full-bamboo.svg",
        "name": "Beans Referral",
        "attributes": [{"key": "title", "value": "bamboo"}],
    },
    {
        "id": 2,
        "description": "Beans Email program",
        "image": "https://bnsre.s3.amazonaws.com/static-v3/connect/img/app/logo-full-foxx.svg",
        "name": "Beans Email",
        "attributes": [{"key": "title", "value": "foxx"}],
    },
    {
        "id": 3,
        "description": "Beans Popup program",
        "image": "https://bnsre.s3.amazonaws.com/static-v3/connect/img/app/logo-full-poppy.svg",
        "name": "Beans Loyalty",
        "attributes": [{"key": "title", "value": "poppy"}],
    },
    {
        "id": 4,
        "description": "Beans Widget program",
        "image": "https://bnsre.s3.amazonaws.com/static-v3/connect/img/app/logo-full-snow.svg",
        "name": "Beans Widget",
        "attributes": [{"key": "title", "value": "snow"}],
    },
    {
        "id": 6,
        "description": "Beans Social Connect Program ",
        "image": "https://bnsre.s3.amazonaws.com/static-v3/connect/img/app/logo-full-arrow.svg",
        "name": "Beans Social Connect",
        "attributes": [{"key": "title", "value": "arrow"}],
    },
]


@app.get("/trellix/token/metadata")
async def list_metadata():
    return metadata


@app.get("/trellix/token/metadata/{pk}")
async def read_metadata(pk: int):
    if pk > len(metadata) - 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return metadata[pk]
