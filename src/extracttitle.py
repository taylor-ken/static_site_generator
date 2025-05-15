
def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        line = line.lstrip()
        if line.startswith('# '):
            return line[2:].strip()
    raise Exception('no h1 header')
    