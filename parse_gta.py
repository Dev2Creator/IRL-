import json

data = open('gta_text_main.txt', 'rb').read()
parts = data.split(b'\x00')
d = {}
for p in parts:
    try:
        s = p.decode('cp1252', errors='ignore')
        if s.startswith('['):
            idx = s.find(']')
            if idx != -1:
                key = s[1:idx]
                val = s[idx+1:]
                d[key] = val
    except:
        pass

with open('irl/gta_data.py', 'w', encoding='utf-8') as f:
    f.write('GTA_TEXTS = ' + json.dumps(d, indent=4) + '\n')
