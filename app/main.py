from fastapi import FastAPI
import threading
from app.routes import router
from app.utils import update_data_periodically

app = FastAPI()
app.include_router(router)

threading.Thread(target=update_data_periodically, daemon=True).start()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)