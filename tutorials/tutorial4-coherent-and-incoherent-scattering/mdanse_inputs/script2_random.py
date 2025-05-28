import random

isotopes = ["Atm1"] * 128 + ["Atm2"] * 128

mapping = {}
for i in range(256):
    random_element = random.choice(isotopes)
    isotopes.remove(random_element)
    mapping[str(i)] = random_element

print(str(mapping).replace("'", '"'))
