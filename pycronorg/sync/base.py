from abc import ABC
from typing import Optional


class BaseApi(ABC):
    _AUTH_KEY = 'Authorization'
    _DEFAULT_BASE_PATH = 'https://api.cron-job.org'
    _DEFAULT_HEADERS = {
        'Content-Type': 'application/json',
    }

    def __init__(
        self, 
        token: str, 
        *, 
        base_path: Optional[str] = None, 
        headers: Optional[dict] = None,
    ) -> None:
        self._token = token
        self._headers = headers or self._DEFAULT_HEADERS
        self._headers[self._AUTH_KEY] = f'Bearer {self._token}'
        self._base_path = base_path or self._DEFAULT_BASE_PATH


