# # # Создайте массив состоящий из словарей с данными
nedvijimost = [
     {
         'status': 'jilichnyi',
         'ploshad_s': 58
      },
     {
         'status': 'komercheskii',
         'ploshad_s': 35
     },
     {
         'status': 'sotsialnyi',
          'ploshad_s': 200
     },
      {
          'status': 'komercheskii',
          'ploshad_s': 160,
      }
    ]

def filter(arr):
    newMass = []
    for i in arr:
        if i["ploshad_s"] >= 100:
            newMass.append(i)
    return newMass


filterArray = filter(nedvijimost)
print(filterArray)
def addKey(mass):
    for i in mass:
        i["sold"] = "yes"
    return mass


addedMass = addKey(filterArray)
def v_kontse(mass):
    for slovar in mass:
        print(slovar)


v_kontse(addedMass)