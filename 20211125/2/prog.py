import sys
print(sys.stdin.buffer.read().decode(errors='replace').encode('latin1', 'replace').decode('cp1251', 'replace'))
