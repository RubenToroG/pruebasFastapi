from fastapi import HTTPException, status
from sqlmodel import SQLModel

def internal_server_error():
    raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error has occurred! Please try again later"
        )

def not_found(detail="Source not found"):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=detail
    )

class ErrorMessage(SQLModel):
    detail: str

HTTP_RESPONSE_404 = {404:
                        {
                            "description": "The requested resource was not found",
                            "model": ErrorMessage
                        }
                    }
HTTP_RESPONSE_500 = {500: 
                        {
                            "description": "Internal error",
                            "model": ErrorMessage
                        }
                    }