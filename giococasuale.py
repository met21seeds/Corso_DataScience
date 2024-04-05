import random

def genera_numero_segreto():
  "Genera un numero casuale tra 1 e 100"
  return random.randint(1, 100)

# Generazione del numero segreto
num_segreto = genera_numero_segreto()

# numero di tentativi massimi
tentativi_max = 5

# Ciclo per i tentativi
for tentativo in range(1, tentativi_max + 1):
  # Richiedi all'utente di inserire un numero
  num_inserito = int(input(f"Tentativo {tentativo}/{tentativi_max}: Inserisci un numero tra 1 e 100: "))

  # Controlla se il numero inserito è quello giusto
  if num_inserito == num_segreto:
    print(f"Hai indovinato! Il numero segreto era {num_segreto}.")
    break
  # Fornisci un indizio all'utente
  elif num_inserito < num_segreto:
    print("Il numero segreto è più alto.")
  else:
    print("Il numero segreto è più basso.")

# Messaggio di fine gioco
if tentativo == tentativi_max:
  print(f"Mi dispiace, hai esaurito i tentativi. Il numero segreto era {num_segreto}.")
