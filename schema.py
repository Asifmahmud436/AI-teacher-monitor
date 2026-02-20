from pydantic import BaseModel

class GetReport(BaseModel):
    teacher : str
    startDate : str | None = None
    endDate : str | None = None
    subject : str | None = None