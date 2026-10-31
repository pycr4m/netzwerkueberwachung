# Netzwerk-Überwachung

Ein Python-Konsolenprogramm zur Verwaltung der Server eines Unternehmens. Über ein Hauptmenü können Server angezeigt, abgefragt, im Status umgeschaltet (Ping-Simulation) und die ausgefallenen Server gefiltert werden.

## Funktionen

| Menüpunkt | Funktion | Beschreibung |
|-----------|----------|--------------|
| 1 | Serverliste ausgeben | Formatierte Tabelle mit Servername, IP und Status (grün `erreichbar` / rot `ausgefallen`). |
| 2 | Serverspezifische Info ausgeben | Servername per `input()` eingeben, dann werden Name, IP und Status dieses Servers angezeigt. |
| 3 | Serverstatus ändern | Servername per `input()` eingeben, der Status wird umgeschaltet (Ping-Simulation, `True` ↔ `False`). |
| 4 | Offline Server ausgeben | Tabellarische Übersicht aller ausgefallenen Server (Ausfall-Statistik). Sind alle Server erreichbar, erscheint eine entsprechende Meldung. |
| 5 | Programm beenden | Beendet das Programm. |

## Datenstruktur

Jeder Server ist eine Liste aus Name, IP-Adresse und Status. Alle Server liegen in der Liste `servers`:

```python
servers = [
    ["WebSrv01",  "192.168.1.10", True],   # 0
    ["DB-Server", "192.168.1.20", False],  # 1
    ["BackupSrv", "192.168.1.30", True],   # 2
    ["MailSrv",   "192.168.1.40", True],   # 3
]
# True = erreichbar, False = ausgefallen
```

## Voraussetzungen

- **Python 3.12 oder neuer.** Der Code verwendet f-Strings mit gleichen Anführungszeichen innerhalb des Ausdrucks (z. B. `f"|{"SERVER-NAME":^16}|"`), das ist erst ab Python 3.12 erlaubt.
- Keine zusätzlichen Pakete, nur die Standardbibliothek.
- Ein Terminal mit Unterstützung für ANSI-Farben (für die farbige Ausgabe).

## Installation und Start

```bash
git clone https://github.com/pycr4m/netzwerkueberwachung.git
cd netzwerkueberwachung
python netzwerküberwachung.py
```

## Bedienung

Nach dem Start erscheint das Hauptmenü:

```
Du bist im Hauptmenü
 1) Serverliste ausgeben
 2) Serverspezifische Info ausgeben
 3) Serverstatus ändern
 4) Offline Server ausgeben
 5) Programm beenden

Wähle eine Aktion:
```

Ungültige Eingaben (Buchstaben oder Zahlen außerhalb von 1 bis 5) werden abgefangen und die Eingabe wird wiederholt.

**Hinweis:** Bei der Servername-Eingabe (Menüpunkt 2 und 3) muss die Groß- und Kleinschreibung exakt stimmen, z. B. `DB-Server` und nicht `db-server`. Bei einem unbekannten Namen wird die Eingabe erneut abgefragt.

## Beispielausgaben

**1) Serverliste** (Status im Terminal farbig: grün/rot)

```
 ________________ ________________ ________________
|                |                |                |
|  SERVER-NAME   |   SERVER-IP    | SERVER-STATUS  |
|________________|________________|________________|
|                |                |                |
|WebSrv01        |  192.168.1.10  |   erreichbar   |
|________________|________________|________________|
|                |                |                |
|DB-Server       |  192.168.1.20  |  ausgefallen   |
|________________|________________|________________|
...
```

**2) Serverinfo**

```
Zu welchem Server sollen Informationen angezeigt werden?
Servername: DB-Server

Servername: DB-Server
Serverip: 192.168.1.20
Serverstatus: False
```

**3) Status ändern**

```
Welcher Serverstatus soll geändert werden?
Servername: DB-Server
Erfolg!
DB-Server online auf True geändert!
```

**4) Offline Server**

```
Ausgefallene Server:

 ________________ ________________
|  SERVER-NAME   | SERVER-STATUS  |
|________________|________________|
|   DB-Server    |    offline     |
|________________|________________|

Server, die offline sind: ['DB-Server']
```

## Projektstruktur

```
netzwerkueberwachung/
├── netzwerküberwachung.py   # Hauptprogramm
└── README.md
```

## Funktionsübersicht im Code

| Funktion | Aufgabe |
|----------|---------|
| `main()` | Hauptmenü und Programmschleife |
| `tabelle_ausgeben()` | Gibt die Serverliste als farbige Tabelle aus |
| `get_servername()` | Fragt einen gültigen Servernamen ab |
| `get_serverinfo()` | Zeigt Name, IP und Status eines Servers |
| `status_aendern()` | Schaltet den Status eines Servers um |
| `get_server_offline()` | Filtert und zeigt alle ausgefallenen Server |

## Autor

[pycr4m](https://github.com/pycr4m)
