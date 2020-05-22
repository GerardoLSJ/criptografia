import hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

print("Audio 8.7 MB: ", md5("blues.mp3"))
print("Imagen JPG 9.9MB: ", md5("imagen.jpg"))