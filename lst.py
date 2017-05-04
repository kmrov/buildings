import regex

list_txt = open("data/list.txt").read()

list_txt = regex.sub("([^\n])\n([^\n])", "\\1 \\2", list_txt)

buildings = [
    building.strip().replace("\n", " ").replace("  ", " ")
    for building in
    regex.findall(
        "\n\n.*?\d.*?\n\n", list_txt, overlapped=True
    )
]

with open("data/list2.txt", "w") as f:
    for building in buildings:
        print(building, file=f)
