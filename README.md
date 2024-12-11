# Script di Avvio Applicazioni

Questo script bash è stato creato per avviare rapidamente alcune applicazioni su Linux tramite un menu interattivo.
Permette di scegliere tra:

 - Firefox (browser)
 - Kitty (terminal)
 - Thunar (file manager)
 - Gparted (gestore partizioni)

(chiunque abbia necessità di avviare altre app potrà modificare il bash in maniera molto semplice per avviare
nuove applicazioni/comandi bash)

# Funzionamento

- Gestione SIGINT: Il segnale di interruzione (Ctrl+C) viene ignorato, continuando il ciclo principale.
- Menu interattivo: Usando dialog, l'utente può selezionare un'applicazione da lanciare.
- Esecuzione in background: Le applicazioni vengono avviate con nohup, permettendo l'esecuzione in background.
- Controllo annullamento: Se l'utente seleziona il menu, lo script ritorna al menu senza fare nulla.

# Dipendenze

    dialog
    nohup
    sudo (per Gparted)

# Creazione

Salva il codice in un file (ad esempio blauncher.sh).
Rendi eseguibile il file:

    chmod +x blauncher.sh

Esegui lo script:

    ./blauncher.sh

Lo script è stato creato per facilitare l'avvio rapido delle applicazioni in sistemi linux (nel mio caso debian 12)
senza bisogno di barre degli strumenti o desktop environment avanzati.
