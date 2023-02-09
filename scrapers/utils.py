import base64

def b64decode(str):
    str = str.replace('_','/')
    str += "=" * ((4 - len(str) % 4) % 4)
    return base64.b64decode(str)