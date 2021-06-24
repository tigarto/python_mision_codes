# Forma 1
def obtenerParticulaMasEscasa1(dictPart: dict) -> str:
    minProb = 1   # Probabilidad minima (Se inicia asumiendo el maximo valor que es 1)
    particulaEscasa = ""
    for (partName,prob) in dictPart.items():
        if prob <= minProb:
            particulaEscasa = partName
            minProb = prob
    return particulaEscasa

def obtenerParticulaMasEscasa2(dictPart: dict) -> str:
    minProb = 1   # Probabilidad minima (Se inicia asumiendo el maximo valor que es 1)
    particulaEscasa = ""
    for partName in dictPart:
        if dictPart[partName] <= minProb:
            particulaEscasa = partName
            minProb = dictPart[partName]
    return particulaEscasa

# Explore otras posibles formas

observacion1 = {'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14}
partObs1 = obtenerParticulaMasEscasa1(observacion1)
print(partObs1)

observacion2 = {'neutron': 0.55, 'proton': 0.21, 'meson': 0.07, 'muon': 0.03, 'neutrino': 0.14}
partObs2 = obtenerParticulaMasEscasa2(observacion2)
print(partObs2)