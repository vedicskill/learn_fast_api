from router_example import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router=router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}



