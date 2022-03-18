from fastapi import FastAPI, HTTPException

app = FastAPI()

metadata = [
    {
        "id": 0,
        "description": "Libanais Quatro Tag NFT",
        "external_url": "https://unicore-beta.s3.amazonaws.com/media/tags/8f90cb4c1e5549e3884ff8f302cc9984.png",
        "image": "https://unicore-beta.s3.amazonaws.com/media/tags/8f90cb4c1e5549e3884ff8f302cc9984.png",
        "name": "Quatro Libanais Tag NFT",
    },
    {
        "id": 0,
        "description": "Pizza Quatro Tag NFT",
        "external_url": "https://unicore-beta.s3.amazonaws.com/media/tags/22ecf7bc506f4716b46fa470c5ff9c2f.png",
        "image": "https://unicore-beta.s3.amazonaws.com/media/tags/22ecf7bc506f4716b46fa470c5ff9c2f.png",
        "name": "Quatro Pizza Tag NFT",
    },
]


@app.get("/metadata")
async def list_metadata():
    return metadata


@app.get("/metadata/{pk}")
async def read_metadata(pk: int):
    if pk > len(metadata) - 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return metadata[pk]
