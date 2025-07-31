import requests
from requests.exceptions import RequestException, Timeout, HTTPError, ConnectionError


class HttpClient:
    def __init__(self, base_url=None, default_headers=None, timeout=10, **kwargs):
        self.base_url = base_url.rstrip("/") if base_url else ""
        self.default_headers = default_headers or {}
        self.timeout = timeout

    def _full_url(self, endpoint):
        return f"{self.base_url}/{endpoint.lstrip('/')}" if self.base_url else endpoint

    def _request(self, method, endpoint, **kwargs):
        url = self._full_url(endpoint)
        headers = {**self.default_headers, **kwargs.pop("headers", {})}
        try:
            response = requests.request(
                method=method.upper(),
                url=url,
                headers=headers,
                timeout=kwargs.pop("timeout", self.timeout),
                **kwargs
            )
            response.raise_for_status()
            return response.json() if "application/json" in response.headers.get("Content-Type", "") else response.text

        except Timeout:
            print(f"[Timeout] {method} {url}")
        except HTTPError as e:
            print(f"[HTTPError] {method} {url} - Status: {e.response.status_code}")
        except ConnectionError:
            print(f"[ConnectionError] {method} {url}")
        except RequestException as e:
            print(f"[RequestException] {method} {url} - {str(e)}")

        return None

    def get(self, endpoint, params=None, **kwargs):
        return self._request("GET", endpoint, params=params, **kwargs)

    def post(self, endpoint, data=None, json=None, **kwargs):
        return self._request("POST", endpoint, data=data, json=json, **kwargs)

    def put(self, endpoint, data=None, json=None, **kwargs):
        return self._request("PUT", endpoint, data=data, json=json, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)
