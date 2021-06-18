from __future__ import division
from nltk.corpus import inaugural
inaugural.fileids()
for fileid in inaugural.fileids():
    avg = sum(len(sent) for sent in inaugural.sents(
    fileids=[fileid])) / len(inaugural.sents(fileids=[fileid]))
    print (fileid, avg)
