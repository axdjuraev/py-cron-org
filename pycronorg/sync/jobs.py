from typing import Optional
from pycronorg.schemas import JobsDetails
from .base import BaseApi


class JobsApi(BaseApi):
    _DEFAULT_BASE_PATH = "jobs"

    def __init__(self, token, *, base_path=None, headers=None) -> None:
        super().__init__(token, base_path=base_path, headers=headers)
        self._base_path = f"{base_path}/jobs"

    def all(self) -> Optional[JobsDetails]:
        res = self._proxy_request.get(self._url, headers=self._headers)

        if not res.ok:
            return None

        return JobsDetails(**res.json())

