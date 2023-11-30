from typing import Optional
from pycronorg.schemas import (
    History,
    JobDetailUpdate,
    JobsDetails, 
    JobDetail,
    JobDetailCreate,
)
from .base import BaseApi


class JobsApi(BaseApi):
    _DEFAULT_BASE_PATH = "jobs"
    Schema = JobDetail 

    def __init__(self, token, *, base_path=None, headers=None) -> None:
        super().__init__(token, base_path=base_path, headers=headers)
        self._base_path = f"{base_path}/jobs"

    def all(self) -> Optional[JobsDetails]:
        res = self._safe_response(self._proxy_request.get(self._url, headers=self._headers))
        return JobsDetails(**res.json())
    
    def get(self, jobId: int):
        url = f"{self._url}/{jobId}"
        res = self._safe_response(self._proxy_request.get(url, headers=self._headers))
        return JobsDetails(**res.json())

    def delete(self, jobId: int):
        url = f"{self._url}/{jobId}"
        self._safe_response(self._proxy_request.delete(url, headers=self._headers))

    def create(self, jobDetail: JobDetailCreate):
        self._safe_response(
            self._proxy_request.put(
                self._url, 
                headers=self._headers, 
                json=jobDetail.dict(),
            )
        )

    def update(self, jobDetail: JobDetailUpdate):
        url = f"{self._url}/{jobDetail.jobId}"
        self._safe_response(
            self._proxy_request.patch(
                url, 
                headers=self._headers, 
                json=jobDetail.dict(exclude_unset=True),
            )
        )

    def retrive_history(self, jobId):
        url = f"{self._url}/{jobId}/history"
        res = self._safe_response(self._proxy_request.get(url, headers=self._headers))
        return History(**res.json())

