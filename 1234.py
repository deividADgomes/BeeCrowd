try:
    while True:
        text = input()
        tex = ''
        teste = ''
        o = 0

        tex = text.replace(' ', '')

        for i in range(0, len(tex)):
            if i % 2 == 0:
                teste += tex[i].upper()
            else:
                teste += tex[i].lower()

        text = list(text)

        for i in range(0, len(text)):
            if text[i] != ' ':
                text[i] = teste[o]
                o += 1
        tex = ''
        for i in text:
            tex += i

        print(tex)
except EOFError:
    pass
try:
    while True:
        text = input()
        tex = ''
        teste = ''
        o = 0

        tex = text.replace(' ', '')

        for i in range(0, len(tex)):
            if i % 2 == 0:
                teste += tex[i].upper()
            else:
                teste += tex[i].lower()

        text = list(text)

        for i in range(0, len(text)):
            if text[i] != ' ':
                text[i] = teste[o]
                o += 1
        tex = ''
        for i in text:
            tex += i

        print(tex)
except EOFError:
    pass
