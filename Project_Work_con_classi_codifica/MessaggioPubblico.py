class MessaggioPubblico():

    def __init__(self, oggetto, messaggio, Mittente, Destinatario, data):
        self.oggetto = oggetto
        self.messaggio = messaggio
        self.mittente = Mittente.nome + " " + Mittente.cognome
        self.destinatario = Destinatario.nome + " " + Destinatario.cognome
        self.data = data

