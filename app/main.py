from fastapi import FastAPI
import threading
from app.routes import router
from app.utils import automate_data_update

app = FastAPI()
app.include_router(router)

threading.Thread(target=automate_data_update, daemon=True).start()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)