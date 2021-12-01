import sys
import struct

inp = sys.stdin.buffer
fmt = "<4sI4s4sI2s2sII2s2s4sI"
sz = struct.calcsize(fmt)
part = inp.read(sz)
if len(part) != sz:
    print('NO')
    exit(0)
res = struct.unpack(fmt, part)
if not (res[0] == b"RIFF" and res[2] == b"WAVE"):
    print("NO")
    exit(0)
file_size = res[1]
format_type = int.from_bytes(res[5], 'little')
channels_num = int.from_bytes(res[6], 'little')
sample_rate = res[7]
bps = int.from_bytes(res[10], 'little')
data_size = res[12]
print(f"Size={file_size}, Type={format_type}, Channels={channels_num}, Rate={sample_rate}, Bits={bps}, Data size={data_size}")
