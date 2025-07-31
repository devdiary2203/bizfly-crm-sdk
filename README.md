# Bizfly CRM Python Client

A lightweight and extensible Python SDK for interacting with [Bizfly CRM API](https://crm.vn/apidoc/doc/).  
Easily integrate Bizfly CRM into your Python applications with support for authentication, GET/POST/PUT/DELETE requests, and robust error handling.

---

## 🚀 Features
- Simple and reusable client class
- Supports authentication via `access_token`, `api_secret`, and `project_token`
- Handles all API methods: `GET`, `POST`, `PUT`, `DELETE`
- JSON-based request/response support
- Basic error handling and timeout control

---

## Installation

```bash
pip install bizfly_crm_sdk
````

> *Note: Replace this with actual PyPI link if published, or use local install:*

```bash
pip install -e .
```

---

## Usage

```python
from bizfly_crm.base_table import Client

client = Client(
    access_key="your_access_key",
    access_sign="your_access_sign",
    project_token="your_project_token"
)

# Example: Get customer list
response = client.get("/customer", params={"limit": 10})

# Example: Create a new customer
response = client.post("/customer", json={
    "name": "Nguyen Van A",
    "phone": "0123456789"
})

# Example: Update customer
response = client.put("/customer/123", json={"email": "new@example.com"})

# Example: Delete customer
response = client.delete("/customer/123")
```

---

## API Reference

You can find the full official API documentation here:
👉 [https://crm.vn/apidoc/doc/](https://crm.vn/apidoc/doc/)

---

## Development & Testing

```bash
# Clone the repository
git clone https://github.com/devdiary2203/bizfly-crm-sdk
cd bizfly-crm-sdk

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

---

## Contribution

Contributions, issues and feature requests are welcome!
Feel free to open a [pull request](https://github.com/devdiary2203/bizfly-crm-sdk) or [issue](https://github.com/devdiary2203/bizfly-crm-sdk/issues).

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
