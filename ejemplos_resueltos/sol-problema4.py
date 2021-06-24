
def info_cientifico(alias, dic_cientificos):
    data = dic_cientificos[alias]
    info = []
    for k in ('author', 'forename', 'surname', 'notes', 'born', 'died'):
        info.append(data.get(k,''))
    return info

# Diccionario para test
cientificos = {
                    'jgoodall': {'surname' : 'Goodall',
                                 'forename' : 'Jane',
                                 'born' : 1934,
                                 'died' : None,
                                 'notes' : 'primate researcher',
                                 'author' : ['In the Shadow of Man', 'The Chimpanzees of Gombe']
                                 },
                    'rfranklin': {'surname' : 'Franklin',
                                   'forename' : 'Rosalind',
                                   'born' : 1920,
                                   'died' : 1957,
                                   'notes' : 'contributed to discovery of DNA'
                                 },
                    'rcarson':   {'surname' : 'Carson',
                                  'forename' : 'Rachel',
                                  'born' : 1907,
                                  'died' : 1964,
                                  'notes' : 'raised awareness of effects of DDT',
                                  'author' : ['Silent Spring']
                                 }
}

# Test de las funciones
print(info_cientifico('jgoodall', cientificos))
print(info_cientifico('rfranklin', cientificos))
print(info_cientifico('rcarson', cientificos))