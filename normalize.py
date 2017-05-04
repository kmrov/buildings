import re

replace = [
    ("ё", "е"),
    ("  ", " "),
    ('"', ""),
    ("/", "-"),
    ("г. москва, ", ""),
    ("д. -, ", ""),
    ("город", "г."),
    ("улица", "ул."),
    ("дом", "д."),
    ("корпус", "к."),
    ("корп.", "к."),
    ("бульвар", "б-р."),
    ("переулок", "пер."),
    ("проектируемый проезд №", "прпр"),
    ("проезд. проектируемый", "прпр"),
    ("проезд.", "пр."),
    ("проезд", "пр."),
    ("пр-кт.", "просп."),
    ("проспект", "просп."),
    ("поселение", "п."),
    ("дачный поселок", "дп."),
    ("поселок", "п."),
    ("шоссе", "ш."),
    ("набережная", "наб."),
    ("строение", "к."),
    ("стр.", "к."),
    ("большая", "б."),
    ("малая", "м."),
    ("большой", "б."),
    ("малый", "м."),
    ("линия.", "лин."),
    ("линия", "лин."),
    ("верхн.", "в."),
    ("верхний", "в."),
    ("верхняя", "в."),
    ("нижн.", "н."),
    ("нижний", "н."),
    ("нижняя", "н."),
    ("квартал", "кв-л."),
    ("средний", "ср."),
    ("средняя", "ср."),
    ("средн.", "ср."),
]

forward = [
    "ул.", "б-р.", "пер.", "пр.", "просп.", "ш.", "наб.", "лин.", "кв-л.",
]

for val in range(1, 25):
    forward.insert(0, "{}-я".format(val))
    forward.insert(0, "{}-й".format(val))

backward = [
    "б.", "м.", "н.", "в.", "ср."
]


def normalize_part(part):
    part = part.strip()
    for forward_part in forward:
        if forward_part in part and not part.startswith(forward_part):
            part = re.sub(
                "\s+{}\s+".format(forward_part),
                " ", part
            )

            part = re.sub(
                "\s+{}".format(forward_part),
                "", part
            )

            part = re.sub(
                "{}\s+".format(forward_part),
                "", part
            )

            part = forward_part + " " + part
    for backward_part in backward:
        if backward_part in part and not part.startswith(backward_part):
            part = re.sub(
                "\s+{}\s+".format(backward_part),
                " ", part
            )

            part = re.sub(
                "\s+{}".format(backward_part),
                "", part
            )

            part = re.sub(
                "{}\s+".format(backward_part),
                "", part
            )

            part = part + " " + backward_part

    return part


def normalize_address(address):
    address = address.lower()
    address = re.sub("(\d{3,5})-й", "\\1", address)
    for k, v in replace:
        address = address.replace(k, v)
    parts = [normalize_part(part) for part in address.split(",")]
    address = ", ".join(parts)
    if "д." not in address:
        address = address.replace("к.", "д.")
    return address
