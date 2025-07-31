import hmac
import hashlib

# Generate a BizFly signature using the current time, project token, and API secret
def generate_bizfly_signature(time_now: str, project_token: str, api_secret: str) -> str:
    message = (time_now + project_token).encode('utf-8')
    secret = api_secret.encode('utf-8')
    signature = hmac.new(secret, message, hashlib.sha512).hexdigest()
    return signature
