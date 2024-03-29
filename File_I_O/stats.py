# HOW TO GET NUMBER OF CHARACTERS/LINES,WORDS etc
def statistics(file):
    with open(file) as file:
        lines = file.readlines()
    return {
        'lines': len(lines),
        'words': sum([len(line.split(" ")) for line in lines]),
        'characters': sum([len(line) for line in lines])
    }
