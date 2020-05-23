import json 
import hmac
from hashlib import sha256
from base64 import urlsafe_b64encode, urlsafe_b64decode
# from app.settings import SECRET_KEY

SECRET_KEY = 'mg1sqmmv=d0t40%2c7)j9anuczm%5sp3b%om93ti30v%g3&i3n'
SECRET = SECRET_KEY.encode("utf-8")
def encode():
    segments = []
    header_dict = {
        "typ": "JWT",
        "alg": "HS256"
    }

    json_header = json.dumps(header_dict, separators=(",", ":")).encode("utf-8")
    header = urlsafe_b64encode(json_header).replace(b"=", b"")
    segments.append(header)

    payload_dict = {
        "user_id": 1
    }

    json_payload = json.dumps(payload_dict, separators=(",", ":")).encode("utf-8")
    payload = urlsafe_b64encode(json_payload).replace(b"=", b"")
    segments.append(payload)

    # SECRET = b'abc123'
    signing_input = b".".join(segments)

    sig = hmac.new( SECRET, signing_input, sha256)
    signature = urlsafe_b64encode(sig.digest()).replace(b"=", b"")
    segments.append(signature)

    token = b'.'.join(segments)
    print("TOKEN:")
    print(token)
    return token


test = b"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.xpCS8TTq1a53OIps1ByTdm6Sh-A1ZoCId3e2YYWjapU"
def decode(jwt):
    signing_input, crypto_segment = jwt.rsplit(b".", 1)
    header_segment, payload_segment = signing_input.split(b".", 1)
    header_data = base64url_decode(header_segment)
    payload = base64url_decode(payload_segment)
    print("DECODED:")
    print(header_data)
    print(payload)

    sig = hmac.new( SECRET, signing_input, sha256)
    signature = urlsafe_b64encode(sig.digest()).replace(b"=", b"")

    if(crypto_segment == signature):
        print("**** VALID SIGNATURE ****")
    else:
        print("*** !!!INVALID SIGNATURE ***")




def base64url_decode(input):
    rem = len(input) % 4

    if rem > 0:
        input += b"=" * (4 - rem)

    return urlsafe_b64decode(input)

jwt = encode()
print("------------")
decode(jwt)