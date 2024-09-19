nomes = ["Ana", "Beatriz", "Daniel", "Elisa"]

print (nomes)

if ("Carlos" in nomes):
    print ("Carlos está na lista")
else:
    print ("Carlos não está na lista")

nomes[1] = "Bruna"

print (nomes)

Ana = nomes.count("Ana")

print (f"Ana aparece {Ana} vezes na lista")