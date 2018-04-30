from music21.stream import Stream
from music21.note import Note

def seqs2stream(song, dictionaries):
    """
    convert from our standard data format to music21's stream format
    (issue: output is one octave higher than what it should, doesn't affect key analysis)
    :returns: music21 stream object
    """
    dTseq, tseq, pseq = song["dTseqs"], song["tseqs"], song["pitchseqs"]
    out = Stream()
    curOffset = 0.
    for i in range(len(tseq)):
        dt, t, p = (dTseq[i], tseq[i], pseq[i])
        pitchtext = dictionaries['pitch_text'][p]
        if pitchtext[0] == 'b':
            pitchtext = pitchtext[1] + '-' + pitchtext[2]
        n = Note(pitchtext)
        curOffset += dictionaries['dTseqs'][dt]
        n.quarterLength = dictionaries['tseqs'][t]
        out.insert(curOffset, n)
    return out
