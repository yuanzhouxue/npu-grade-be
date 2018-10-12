# coding: utf8

import base64
import os

import hashlib
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA


pub_key = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0cnl7FY0dSG5lgpIq/Yb
wqhykm1DYGFb0kD0IcjO4YlmK61EtZM4NWr6tNDNElN6eawLKZDxtzYaFnOUAFwx
PY75QRs+DE5coKxulPRDzboIauCdychQtR+H8adS+4i3gOmFRPjqoyqp+qchNeVk
t4Zv9yal7+6GpEFZ2uXVJVZoBGS5H57s2dojP4z8by6DlQtMZq2O2tGpPTnG7Y3t
+hR6HVri/9eiSjfzLhT3XO3Jcnykdz7Bb7LUWMmreQHIuY7res2wHqX8LyTiNTib
lzbPiw4MbY/xZ4B1alCKVSZXZFG0om6CkHAkw0Q8CLbYU8VN50I0VXaJJ7bdn4dk
2QIDAQAB
-----END PUBLIC KEY-----'''

private_key = '''-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA0cnl7FY0dSG5lgpIq/Ybwqhykm1DYGFb0kD0IcjO4YlmK61E
tZM4NWr6tNDNElN6eawLKZDxtzYaFnOUAFwxPY75QRs+DE5coKxulPRDzboIauCd
ychQtR+H8adS+4i3gOmFRPjqoyqp+qchNeVkt4Zv9yal7+6GpEFZ2uXVJVZoBGS5
H57s2dojP4z8by6DlQtMZq2O2tGpPTnG7Y3t+hR6HVri/9eiSjfzLhT3XO3Jcnyk
dz7Bb7LUWMmreQHIuY7res2wHqX8LyTiNTiblzbPiw4MbY/xZ4B1alCKVSZXZFG0
om6CkHAkw0Q8CLbYU8VN50I0VXaJJ7bdn4dk2QIDAQABAoIBAQC/tYGgDFLZqxz+
KJ2qTzelFevFNYX5oF6Zb3PpH6k2Xyn3xdnhGAyoe/9oltqf4ZstbvOwY10P8Ke8
VpgsEBOLTokmXu+/rShmR8yx39nKOTOR/3sRtzVRnuPLB/4EEDao3j1D/zfkLYux
m2L07pCwSXEt6KqA7HcryPCE4bx65agar/QVPlATsNJi1n2wf3SJ/Mz3JIHmZDwH
Eg0AaF+OE3K4m8TUTEtezELmEfYZR2uFj3PuyVh0jdz1eOJcSXwFYTKMt+y2r203
gh3NeNcVeqy6DY3JUJ6x+fB8v/sg9J4AXBg5TU04x+ukDVwI+R+grnktMtF4HFRl
DmMipSelAoGBAPLO7c3StnhwpMf+YeNKPBZ40ImU99+yI0xbgqMYwWhkN95EKWpc
gpvfvdXcno3K5I2a0M2OSLkUnYyDNQqQAwiZ9tUDaFXgvVJJo7eL7f4NNNawUL4k
fdepsOAAIVIP8H2yQwIuTqVBSFVuM/XxDwslvdCmbsH47SrXUJczEqfzAoGBAN0v
uCD2bFLw570IWwJ57vaxsV9Coz5XKqGnbmUbN3aZ4T0wDgZMEO/Q2+JGwEWkQaEL
CN6Foa+KAyd6hjYMn9Ylh9Gr94UNqT8ZzoxF4RP6RrKkNjisen1p1qJ83dqSazbf
cK5AAJkXRfyQ4ch8pEFa4t6d2oJ+eBJCWZQrYx8DAoGBAI35w4FzcXDRZPjwXOqb
cLEvKbkZGyt5LTyr0aJuikDxQN29e34O4+wjEwynOSrt9WB7oxZe2VUnocwUuIIZ
nTx9UqBRosN8axdfqdRchOflbv0OEdhs3Ayr05nXWaRzX4sQHjB7RU9J8fLKQqXP
s50wD2Kevuq7FGrVhfEzUvhTAoGALo0Zgo56c+ZRz34PsXC6M19ohjT/KGKuDUGw
wUS+Io72UatoeDjQI7jgXjonw0Bzs5If9r1HLyuryEZIMt3rUeWqNR2tRWp/oVEs
IGegnFTDRlu7MahTS0vYKXCAPL0uJWlXTMUZmx7D0wknC8v3we1/6/xq/aXiXW1r
bvzGqsMCgYEAk1r5i4WcZG2hVrtCTCP0tHe7V00S9OSyHoIr9aiYS5E/6nEA7pCX
7TAhbePe/gfjCxaHOFpA4aJCoPndY9WObiCE4FohekmZs2O8ofsAMElirrqoR2hq
9038vav9CfAG8ijW+LgEZmF4WWPihqrjBM/1xLEEP+rx32BCvxOvAU4=
-----END RSA PRIVATE KEY-----'''


def get_md5(src):
    m2 = hashlib.md5()
    m2.update(src.encode(encoding='utf8'))
    return m2.hexdigest()


# 加密
def rsa_encrypt(plain):
    rsa_key = RSA.importKey(pub_key)
    cipher = PKCS1_v1_5.new(rsa_key)
    x = cipher.encrypt(plain.encode())
    return base64.b64encode(x).decode()


def rsa_decrypt(plain):
    rsa_privkey = RSA.importKey(private_key)
    cipher = PKCS1_v1_5.new(rsa_privkey)
    x = cipher.decrypt(base64.b64decode(plain), None) #　解密失败返回None
    if x:
        x = x.decode()
    return x



if __name__ == "__main__":
    # res = rsa_encrypt('Helloworld')
    # print(res)
    print(rsa_decrypt('MwpZx5kuwmEOFyinjyvaRXe2WjdItBe/FMc7KvGQEAVDSmKRWY2liWCtlGMa3TbUevibr/BPEe/iqUEGO9NP3jUD4OwLCWiEG21hFYlhvg2GpvTwO0YG5JFQk6uOukQOTImTaeoEL0MGYuQ0A/pWNMYKj840T0cZxMLi075fGBHnRlnfAetHmLmon3C4HCZXq7d1g/SnOt2r6KLp9lSXBsG1zQvgUSlo2SRkTM3pviYyirMm03z6I1hNSAMyl5jYwI8x2oVsVoT8AgRT8sAaiEV76xSFE4vzd0GRiUkc4jAagkQvB7BHnlWxRaC49BfYfv5coXUfNG7+Xpys4pMYhg=='))
