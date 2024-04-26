def pad_version(v):
    l = v.split(".")
    padded = ""
    for v in l:
        padded += v.rjust(10, "0")
        padded += "."
    return padded

def minor_version(v1, v2):
    return pad_version(v1) < pad_version(v2)

def equal_version(v1, v2):
    return pad_version(v1) == pad_version(v2)

def major_version(v1, v2):
    return not minor_version(v2, v1) and not equal_version(v2, v1)
