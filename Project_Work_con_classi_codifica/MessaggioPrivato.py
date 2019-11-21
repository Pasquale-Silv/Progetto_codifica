class MessaggioPrivato():

    def __init__(self, oggetto, messaggio, Mittente, Destinatario, data):
        self.oggetto = oggetto
        self.messaggio = messaggio
        self.Mittente = Mittente.nome + " " + Mittente.cognome
        self.Destinatario = Destinatario.nome + " " + Destinatario.cognome
        self.data = data

