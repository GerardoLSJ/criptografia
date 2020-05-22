def bytes_from_int(val):
    remaining = val
    byte_length = 0

    while remaining != 0:
        remaining = remaining >> 8
        byte_length += 1

    return val.to_bytes(byte_length, "big", signed=False)




import json 
import hmac
from hashlib import sha256
from base64 import urlsafe_b64encode, urlsafe_b64decode

segments = []

header_dict = {
    "typ": "JWT",
    "alg": "HS256"
}

# json_header = json.dumps(header_dict).encode("utf-8")
# print("json_header",json_header)
json_header = json.dumps(header_dict, separators=(",", ":")).encode("utf-8")
print("json_header",json_header)
header = urlsafe_b64encode(json_header) #.replace(b"=", b"")
segments.append(header)

payload_dict = {
    "user_id": 1
}

json_payload = json.dumps(payload_dict, separators=(",", ":")).encode("utf-8")
payload = urlsafe_b64encode(json_payload).replace(b"=", b"")
segments.append(payload)

print("segments")
print(segments)

SECRET = b'abc123' #.encode("utf-8")
signing_input = b".".join(segments)

sig = hmac.new( SECRET, signing_input, sha256)
signature = urlsafe_b64encode(sig.digest()).replace(b"=", b"")
segments.append(signature)

token = b'.'.join(segments)

print(token)


