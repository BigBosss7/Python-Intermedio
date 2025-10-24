"""
Operaciones
"""
s1 = "Hola"
s2 = "Python"

# Concatenación
print(s1+ ", " +s2 + "!")

#Repeticióm
print(s1 * 3)   
# Indexación
print(s1[0] + s1[1]+ s1[2]+ s1[3])
# longitud
print(len(s2))
# Subcadena (slicing)
print(s2[2:5]) 
print(s2[2:])
print(s2[0:2])
print(s2[:3])
# Búsqueda
print(s2.find("th"))
print("Ho" in s1)
# Reemplazo
print(s1.replace("la", "la, Mundo"))
# División
print(s2.split("t"))
# Cambio de mayúsculas y minúsculas
print(s1.upper())
print("saul barrera")

#Paliondrmo

"""
Extraer 
"""

def check(word1:str, wordS2: str):

# Palíndromopr 

    print(f"¿{word1} es un palíndromo?: {word1 == word1[::-1]}") 
    print(f"¿{wordS2} es un palíndromo?: {wordS2 == wordS2[::-1]}")


# Anagramas
    print(f"¿{word1} es anagrama de {wordS2}?: {sorted(word1) == sorted(wordS2)}")
    # Isogramas
    
    def isogram(word:str)-> bool:
        word_dict = dict()
        for caracter in word:
            word_dict[caracter] = word_dict.get(caracter, 0) + 1
        
        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break  
        return isogram
    
    print(f"¿{word1} es un isograma?: {isogram(word1)}")
    print(f"¿{wordS2} es un isograma?: {isogram(wordS2)}")
    
check("radar", "python")
#check("amor", "roma")
