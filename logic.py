import random

def zar(kenar):
    sonuc = random.randint(1, kenar)

    return(sonuc)

def oldur():
    kelimeler = [
        "kertenkele", "salak",
        "geri zekalı", "yoksul",
        "köpek", "çok akıllı"
    ]

    return random.choice(kelimeler)