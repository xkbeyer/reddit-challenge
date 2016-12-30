import sys
from os.path import basename

def uu_bytes_to_chars(threebytes):
    sixbit1 = threebytes[0] >> 2
    sixbit2 = ((threebytes[0] & 3) << 4) + (threebytes[1] >> 4)
    sixbit3 = ((threebytes[1] & 15) << 2) + (threebytes[2] >> 6)
    sixbit4 = threebytes[2] & 63
    return chr(sixbit1 + 32) + chr(sixbit2 + 32) + chr(sixbit3 + 32) + chr(sixbit4 + 32)

if __name__ == '__main__':
    indir = sys.argv[1]
    filename = basename(indir)

    infile = open(indir, 'rb')
    bytes = infile.read()
    infile.close()

    outfile = open(sys.argv[2], 'w')
    outfile.write('begin 644 ' + filename + '\n')
    while len(bytes) > 45:
        encblock = bytes[:45]
        bytes = bytes[45:]
        outline = 'M'
        for i in range(15):
            outline += uu_bytes_to_chars(encblock[3*i : 3*i + 3])
        outline += '\n'
        outfile.write(outline)
    else:
        linelength = len(bytes)
        if linelength % 3 != 0:
            bytes += b'0' * (3 - (linelength % 3))
        outline = chr(linelength + 32)
        for i in range(len(bytes) // 3):
            outline += uu_bytes_to_chars(bytes[3*i : 3*i + 3])
        outline += '\n`\nend\n'
        outfile.write(outline)
    outfile.close()
    
