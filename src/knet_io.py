import numpy as np

def read_knet(path):
    with open(path) as f:
        lines = f.readlines()
    hdr = {l[:18].strip(): l[18:].strip() for l in lines[:17]}
    fs = float(hdr["Sampling Freq(Hz)"].replace("Hz", ""))
    num, den = hdr["Scale Factor"].split("(gal)/")
    acc = np.array(" ".join(lines[17:]).split(), float) * float(num) / float(den)
    return acc - acc.mean(), fs, hdr