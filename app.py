from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RequestModel(BaseModel):
    user_input: str

def ai_policy_check(text):
    print(f"Simulating AI policy check for input: {text}")

    if "delete" in text.lower() or "drop" in text.lower():
        return False, "Policy Violation: Destructive action detected."
    return True, "Policy Passed."

@app.post("/validate")
def validate_policy(request: RequestModel):
    allowed, reason = ai_policy_check(request.user_input)
    return {"allowed": allowed, "reason": reason}

