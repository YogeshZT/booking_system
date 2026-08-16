from fastapi  import FastAPI

from api.auth import router as auth_router
from api.bookings import router as bookings_router
from api.rooms import router as rooms_router
from infrastructure.database import engine
from models.base import Base
import models

async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(title="Meeting room booking app",version="1.0.0", lifespan=lifespan)

app.include_router(auth_router)
app.include_router(bookings_router)
app.include_router(rooms_router)




