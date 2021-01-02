import re

with open('audio_extension.txt', 'r') as f:
    for line in f:
        matched = re.search(r'<a[^>]*>\.(.*)</a>', line)
        print(matched.group(1).lower())