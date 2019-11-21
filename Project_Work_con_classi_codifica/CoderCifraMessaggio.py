# Classe incaricata di cifrare il messaggio

class Coder():

    cifratura = {
        'a': 'jdsjl43315',
        'b': 'dvnhm79114',
        'c': '12617ghd19',
        'd': '45433gfd13',
        'e': '98bbbv2115',
        'f': '008767ggv3',
        'g': 'jdsjl43321',
        'i': '12617ghd3r',
        'l': '45433gfd4v',
        'm': '98bbbv2554',
        'n': '008767ggvx',
        'o': 'jdsjl43387',
        'p': 'dvnhm7977z',
        'q': '12617ghd0v',
        'r': '45433gfd9c',
        's': '98bbbv288y',
        't': '008767ggvj',
        'u': '67ghgwjdvn',
        'v': '798ghvshc ',
        'z': 'jdyvghc32e',
        ' ': 'z2u45y7891',
        ',': '24gfvb879h',
        '.': 'mkfrth5489',
        '!': '89gt54sacb',
        'h': '0kj9gfdsa2',
        "'": 'nbvtyufdkh',
        '?': 'poiuqwert6'
    }
    decifratura = {v: k for k, v in cifratura.items()}

    def __init__(self, MessaggioPrivato):
        self.MessaggioPrivatoDaCifrare = MessaggioPrivato.messaggio.lower()

    def cifraMessaggioConfidenziale(self):
        self.parolaCifrata = ''
        for lettera in self.MessaggioPrivatoDaCifrare:
            for k in self.cifratura.keys():
                if lettera == k:
                    self.parolaCifrata += self.cifratura[k]
        return self.parolaCifrata

    def decifraMessaggioConfidenziale(self):
        self.parolaDecifrata = ''
        for i in range(0, len(self.parolaCifrata), 10):
            for k in self.decifratura.keys():
                if self.parolaCifrata[i:i + 10] == k:
                    self.parolaDecifrata += self.decifratura[k]
        return self.parolaDecifrata

