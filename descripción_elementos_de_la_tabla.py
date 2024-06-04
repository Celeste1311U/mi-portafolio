import periodictable as pt

# Diccionario con las traducciones de los nombres de algunos elementos
traducciones = {
    "hydrogen": "Hidrógeno",
    "helium": "Helio",
    "lithium": "Litio",
    "beryllium": "Berilio",
    "boron": "Boro",
    "carbon": "Carbono",
    "nitrogen": "Nitrógeno",
    "oxygen": "Oxígeno",
    "fluorine": "Flúor",
    "neon": "Neón",
    "sodium": "Sodio",
    "magnesium": "Magnesio",
    "aluminum": "Aluminio",
    "silicon": "Silicio",
    "phosphorus": "Fósforo",
    "sulfur": "Azufre",
    "chlorine": "Cloro",
    "argon": "Argón",
    "potassium": "Potasio",
    "calcium": "Calcio",
    "scandium": "Escandio",
    "titanium": "Titanio",
    "vanadium": "Vanadio",
    "chromium": "Cromo",
    "manganese": "Manganeso",
    "iron": "Hierro",
    "cobalt": "Cobalto",
    "nickel": "Níquel",
    "copper": "Cobre",
    "zinc": "Zinc",
    "gallium": "Galio",
    "germanium": "Germanio",
    "arsenic": "Arsénico",
    "selenium": "Selenio",
    "bromine": "Bromo",
    "krypton": "Kriptón",
    "rubidium": "Rubidio",
    "strontium": "Estroncio",
    "yttrium": "Itrio",
    "zirconium": "Circonio",
    "niobium": "Niobio",
    "molybdenum": "Molibdeno",
    "technetium": "Tecnecio",
    "ruthenium": "Rutenio",
    "rhodium": "Rodio",
    "palladium": "Paladio",
    "silver": "Plata",
    "cadmium": "Cadmio",
    "indium": "Indio",
    "tin": "Estaño",
    "antimony": "Antimonio",
    "tellurium": "Telurio",
    "iodine": "Yodo",
    "xenon": "Xenón",
    "cesium": "Cesio",
    "barium": "Bario",
    "lanthanum": "Lantano",
    "cerium": "Cerio",
    "praseodymium": "Praseodimio",
    "neodymium": "Neodimio",
    "promethium": "Prometio",
    "samarium": "Samario",
    "europium": "Europio",
    "gadolinium": "Gadolinio",
    "terbium": "Terbio",
    "dysprosium": "Disprosio",
    "holmium": "Holmio",
    "erbium": "Erbio",
    "thulium": "Tulio",
    "ytterbium": "Iterbio",
    "lutetium": "Lutecio",
    "hafnium": "Hafnio",
    "tantalum": "Tantalio",
    "tungsten": "Tungsteno",
    "rhenium": "Renio",
    "osmium": "Osmio",
    "iridium": "Iridio",
    "platinum": "Platino",
    "gold": "Oro",
    "mercury": "Mercurio",
    "thallium": "Talio",
    "lead": "Plomo",
    "bismuth": "Bismuto",
    "polonium": "Polonio",
    "astatine": "Astato",
    "radon": "Radón",
    "francium": "Francio",
    "radium": "Radio",
    "actinium": "Actinio",
    "thorium": "Torio",
    "protactinium": "Protactinio",
    "uranium": "Uranio",
    "neptunium": "Neptunio",
    "plutonium": "Plutonio",
    "americium": "Americio",
    "curium": "Curio",
    "berkelium": "Berkelio",
    "californium": "Californio",
    "einsteinium": "Einsteinio",
    "fermium": "Fermio",
    "mendelevium": "Mendelevio",
    "nobelium": "Nobelio",
    "lawrencium": "Laurencio",
    "rutherfordium": "Rutherfordio",
    "dubnium": "Dubnio",
    "seaborgium": "Seaborgio",
    "bohrium": "Bohrio",
    "hassium": "Hassio",
    "meitnerium": "Meitnerio",
    "darmstadtium": "Darmstadtio",
    "roentgenium": "Roentgenio",
    "copernicium": "Copernicio",
    "nihonium": "Nihonio",
    "flerovium": "Flerovio",
    "moscovium": "Moscovio",
    "livermorium": "Livermorio",
    "tennessine": "Tenesino",
    "oganesson": "Oganesón"
}

tabla = []

while True:
    a = int(input('Ingrese el Z del elemento (0 para terminar): '))
    if a == 0:
        break
    elemento = pt.elements[a]
    nombre_en_espanol = traducciones.get(elemento.name, elemento.name)

    if elemento in tabla:
        print(f'El elemento {nombre_en_espanol} ya se encuentra en la lista')
    else:
        tabla.append(elemento)
        print(f'Se agregó el elemento {nombre_en_espanol} ')

for i in tabla:
    nombre_en_espanol = traducciones.get(i.name, i.name)
    densidad = i.density
    if densidad is None:
        densidad = 'No tiene'
    else:
        densidad = round(densidad, 2)
    print(f'\n{nombre_en_espanol.capitalize()}\nSímbolo: {i.symbol}\nNúmero atómico (z): {i.number}\nDensidad: {densidad}\nPeso molar: {round(i.mass, 2)}\n')