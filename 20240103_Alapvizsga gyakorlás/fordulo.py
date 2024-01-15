from fogadasi_fordulo import fogadasi_fordulo

fordulok: list[fogadasi_fordulo] = []


def beolvas(fajlnev):
    fajl = open(fajlnev,'r',encoding='utf-8' )
    fajl.readline()
    for sor in fajl:
        fordulok.append(fogadasi_fordulo(sor.strip()))
    fajl.close()

def osszes_fordulo():
    return len(fordulok)

def telitatalalatos_szelvenyek_szama():
    darab = 0
    for f in fordulok:
        darab += f.T13p1
    return darab

def volt_dontetlen_mentes_fordulo() -> bool:
    for f in fordulok:
        if f.volt_döntetlen() == False:
            return True
    return False