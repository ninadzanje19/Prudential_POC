#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


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI()

# Pydantic models for request and response
class Quotation(BaseModel):
    name: str
    city: str
    age: int
    work: str

class QuotationResponse(BaseModel):
    quotation_id: str
    data: Quotation

class AnalyzeRequest(BaseModel):
    quotation_id: Optional[str] = None
    name: Optional[str] = None
    city: Optional[str] = None
    age: Optional[int] = None
    work: Optional[str] = None

class AnalyzeResponse(BaseModel):
    decision: str
    analyzed_data: dict

# In-memory storage for demonstration purposes
quotations: Dict[str, Quotation] = {}

@app.post("/quotation", response_model=QuotationResponse)
def create_quotation(quotation: Quotation):
    quotation_id = f"Q{len(quotations) + 1}"
    quotations[quotation_id] = quotation
    print(quotation_id)
    return {"quotation_id": quotation_id, "data": quotation}

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_policy(analyze_request: AnalyzeRequest):
    # Retrieve quotation data using quotation_id if provided.
    if analyze_request.quotation_id:
        if analyze_request.quotation_id not in quotations:
            raise HTTPException(status_code=404, detail="Quotation not found")
        quotation_data = quotations[analyze_request.quotation_id]
    else:
        # Validate that all required fields are provided
        if (
            analyze_request.name is None or
            analyze_request.city is None or
            analyze_request.age is None or
            analyze_request.work is None
        ):
            raise HTTPException(status_code=400, detail="Missing data fields for analysis")
        quotation_data = Quotation(
            name=analyze_request.name,
            city=analyze_request.city,
            age=analyze_request.age,
            work=analyze_request.work
        )

    # Business logic example:
    # Issue policy if age is under 50 and work is not "hazardous".
    decision = "Policy Issued" if quotation_data.age < 50 and quotation_data.work.lower() != "hazardous" else "Policy Not Issued"

    return {"decision": decision, "analyzed_data": quotation_data.dict()}

# To run the application:
# Save this code as main.py and run:
# uvicorn main:app --reload
