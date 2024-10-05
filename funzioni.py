def crea_email(nome,cognome):
    email = nome[0]+"."+cognome+"@padrisomaschi.it"
    return email.lower()
nome = input("Inserisci il tuo nome:")
cognome = input("Inserisci il tuo cognome:")
print(crea_email(nome, cognome))
