def pad_version(v):
    l = v.split(".")
    padded = ""
    for i, v in enumerate(l):
        padded += v.rjust(10, "0")
        padded += "."
    return padded

def minor_version(v1, v2):
    return pad_version(v1) < pad_version(v2)
