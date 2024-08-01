# GitHub Copilot: Generate a Pydantic model for handling JSON input with a single field called "text".

# GitHub Copilot: Create a FastAPI POST endpoint `/tokens` that accepts a JSON body with a "text" field and returns a list of tokens using the generate() function.

from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

@app.get("/")
async def read_root():
    return {"message": "Welcome to the API! Created by [Your Name]"}
