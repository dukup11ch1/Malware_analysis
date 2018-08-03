import hashlib
def md5(fp):
    hash=hashlib.md5()
    hash.update(fp.read())
    return hash.hexdigest()

def sha1(fp):
    hash=hashlib.sha1()
    hash.update(fp.read())
    return hash.hexdigest()

def sha256(fp):
    hash=hashlib.sha256()
    hash.update(fp.read())
    return hash.hexdigest()
