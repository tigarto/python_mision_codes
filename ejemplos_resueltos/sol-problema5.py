
def db_consistent(alias, dic_cientificos):
    keys = tuple(dic_cientificos[alias].keys())
    if len(keys) == 6:
        for k in keys:
            if k not in ('author', 'forename', 'surname', 'notes', 'born', 'died'):
                return False
        return True
    else:
        return False


# Diccionario para test
cientificos = {
                    'jgoodall': {'surname': 'Goodall',
                                 'forename': 'Jane',
                                 'born': 1934,
                                 'died': None,
                                 'notes': 'primate researcher',
                                 'author': ['In the Shadow of Man', 'The Chimpanzees of Gombe']
                                 },
                    'rfranklin': {'surname': 'Franklin',
                                  'forename': 'Rosalind',
                                  'born': 1920,
                                  'died': 1957,
                                  'notes': 'contributed to discovery of DNA'
                                 },
                    'rcarson':   {'surname': 'Carson',
                                  'forename': 'Rachel',
                                  'born': 1907,
                                  'died': 1964,
                                  'notes': 'raised awareness of effects of DDT',
                                  'author': ['Silent Spring']
                                 }
}


# Test de las funciones
print(db_consistent('jgoodall', cientificos))
print(db_consistent('rfranklin', cientificos))
print(db_consistent('rcarson', cientificos))