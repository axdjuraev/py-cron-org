from typing import Optional
from pydantic import BaseModel, Field


class Auth(BaseModel):
    enable: bool = False
    user: str = ""
    password = ""


class Notification(BaseModel):
    onFailure: bool = False
    onSuccess: bool = False
    onDisable: bool = False


class ExtendedData(BaseModel):
    headers: Optional[dict] = None
    body: Optional[str] = None


class Scheldule(BaseModel):
    timezone = "Europe/Berlin"
    expiresAt: int = 0  
    hours: list[int] = Field(default_factory=lambda: [-1])
    mdays: list[int] = Field(default_factory=lambda: [-1])
    minutes: list[int] = Field(default_factory=lambda: [0, 15, 30, 45])
    months: list[int] = Field(default_factory=lambda: [-1])
    wdays: list[int] = Field(default_factory=lambda: [-1])


class JodDetail(BaseModel):
    jobId: int
    enabled: bool = True
    title: str = "Example Job"
    url: str = "https://example.com/"
    saveResponses: bool = False
    lastStatus: int = 0
    lastDuration: int = 0
    lastExecution: int = 0
    nextExecution: int = 0
    type: int = 0
    requestTimeout: int = 300
    redirectSuccess: bool = False
    folderId: int = 0
    scheldule: Scheldule
    auth: Optional[Auth] = None
    notification: Optional[Notification] = None
    extendedData: Optional[ExtendedData] = None
    requestMethod: int = 0


class JobsDetails(BaseModel):
    jobs: list[JodDetail]
    someFailed: bool = False


