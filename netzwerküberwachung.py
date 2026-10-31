servers = [
        ["WebSrv01", "192.168.1.10", True], #0
        ["DB-Server", "192.168.1.20", False], #1
        ["BackupSrv", "192.168.1.30", True], #2
        ["MailSrv", "192.168.1.40", True] #3
    ]

def main():
    while True:
        print()
        print("Du bist im Hauptmenü")
        print(" 1) Serverliste ausgeben")
        print(" 2) Serverspezifische Info ausgeben")
        print(" 3) Serverstatus ändern")
        print(" 4) Offline Server ausgeben")
        print(" 5) Programm beenden")
        print()
        while True:
            try:
                menue_wahl = int(input("Wähle eine Aktion: "))
                if menue_wahl in (1 ,2 ,3 ,4, 5):
                    break
                else:
                    print("Gib 1, 2, 3, 4 oder 5ein!")
            except ValueError:
                print("Gib 1, 2, 3, 4 oder 5 ein!")
        if menue_wahl == 5:
            print()
            print("Auf Wiedersehen!")
            break
        elif menue_wahl == 1:
            tabelle_ausgeben(servers[0], servers[1], servers[2], servers[3])
            continue
        elif menue_wahl == 2:
            print()
            print("Zu welchem Server sollen Informationen angezeigt werden?")
            eingabe = get_servername()
            print()
            get_serverinfo(eingabe)
            print()
            continue
        elif menue_wahl == 3:
            print()
            print("Welcher Serverstatus soll geändert werden?")
            eingabe = get_servername()
            servers[0], servers[1], servers[2], servers[3] = status_aendern(eingabe, servers[0], servers[1], servers[2], servers[3])
            continue
        elif menue_wahl == 4:
            print()
            print("Ausgefallene Server: ")
            print()
            get_server_offline(servers[0], servers[1], servers[2], servers[3])
            continue

def tabelle_ausgeben(erster, zweiter, dritter, vierter):
    sn ="SERVER-NAME"
    si = "SERVER-IP"
    ss = "SERVER-STATUS"
    l = "<16"
    r = ">16"
    m = "^16"
    rot = "\033[1;1;31m"
    gruen = "\033[1;1;32m"
    gelb = "\033[1;1;33m"
    ende = "\033[0m"
    erreichbar = "erreichbar"
    ausgefallen = "ausgefallen"
    zeilegruen = (f"{gruen}{erreichbar:{m}}{ende}")
    zeilerot = (f"{rot}{ausgefallen:{m}}{ende}")
    
    if erster[2] == True:
        ersterfeld = zeilegruen
    else:
        ersterfeld = zeilerot
    if zweiter[2] == True:
        zweiterfeld = zeilegruen
    else:
        zweiterfeld = zeilerot
    if dritter[2] == True:
        dritterfeld = zeilegruen
    else:
        dritterfeld = zeilerot
    if vierter[2] == True:
        vierterfeld = zeilegruen
    else:
        vierterfeld = zeilerot

    print(" "+ 16*"_"+" "+16*"_"+" "+16*"_"+" ")
    print("|"+ 16*" "+"|"+16*" "+"|"+16*" "+"|")
    print(f"|{sn:^16}|{si:^16}|{ss:^16}|")
    print("|"+ 16*"_"+"|"+16*"_"+"|"+16*"_"+"|")
    print("|"+ 16*" "+"|"+16*" "+"|"+16*" "+"|")
    print(f"|{erster[0]:{l}}|{erster[1]:{m}}|{ersterfeld}|")
    print("|"+ 16*"_"+"|"+16*"_"+"|"+16*"_"+"|")
    print("|"+ 16*" "+"|"+16*" "+"|"+16*" "+"|")
    print(f"|{zweiter[0]:{l}}|{zweiter[1]:{m}}|{zweiterfeld}|")
    print("|"+ 16*"_"+"|"+16*"_"+"|"+16*"_"+"|")
    print("|"+ 16*" "+"|"+16*" "+"|"+16*" "+"|")
    print(f"|{dritter[0]:{l}}|{dritter[1]:{m}}|{dritterfeld}|")
    print("|"+ 16*"_"+"|"+16*"_"+"|"+16*"_"+"|")
    print("|"+ 16*" "+"|"+16*" "+"|"+16*" "+"|")
    print(f"|{vierter[0]:{l}}|{vierter[1]:{m}}|{vierterfeld}|")
    print("|"+ 16*"_"+"|"+16*"_"+"|"+16*"_"+"|")

def get_servername():
    while True:
        try:
            eingabe = input("Servername: ")
            if type(eingabe) != str:
                print("Der Servername muss als String Case Sensitiv eingegeben werden!")
                continue
            elif eingabe not in [servers[0][0],servers[1][0],servers[2][0],servers[3][0]]:
                print("Es gibt kein Server mit diesem Namen. (Groß- und Kleinschreibung beachten!)")
            else:
                break
        except ValueError:
            print("Der Servername muss buchstabengetreu Case Sensitiv eingegeben werden!")
    return eingabe

def get_serverinfo(eingabe):
    if eingabe == servers[0][0]:
        print(f"Servername: \033[1;1;33m{servers[0][0]}\033[0m")
        print(f"Serverip: \033[1;1;33m{servers[0][1]}\033[0m")
        print(f"Serverstatus: \033[1;1;33m{servers[0][2]}\033[0m")
    elif eingabe == servers[1][0]:
        print(f"Servername: \033[1;1;33m{servers[1][0]}\033[0m")
        print(f"Serverip: \033[1;1;33m{servers[1][1]}\033[0m")
        print(f"Serverstatus: \033[1;1;33m{servers[1][2]}\033[0m")
    elif eingabe == servers[2][0]:
        print(f"Servername: \033[1;1;33m{servers[2][0]}\033[0m")
        print(f"Serverip: \033[1;1;33m{servers[2][1]}\033[0m")
        print(f"Serverstatus: \033[1;1;33m{servers[2][2]}\033[0m")
    elif eingabe == servers[3][0]:
        print(f"Servername: \033[1;1;33m{servers[3][0]}\033[0m")
        print(f"Serverip: \033[1;1;33m{servers[3][1]}\033[0m")
        print(f"Serverstatus: \033[1;1;33m{servers[3][2]}\033[0m")

def status_aendern(eingabe, erster, zweiter, dritter, vierter):
    if eingabe == erster[0]:
        if erster[2] == True:
            erster[2] = False
        else:
            erster[2] = True
        print("Erfolg!")
        print(f"{eingabe} online auf {erster[2]} geändert!")
        print()
    elif eingabe == zweiter[0]:
        if zweiter[2] == True:
            zweiter[2] = False
        else:
            zweiter[2] = True
        print("Erfolg!")
        print(f"{eingabe} online auf {zweiter[2]} geändert!")
        print()
    elif eingabe == dritter[0]:
        if dritter[2] == True:
            dritter[2] = False
        else:
            dritter[2] = True
        print("Erfolg!")
        print(f"{eingabe} online auf {dritter[2]} geändert!")
        print()
    elif eingabe == vierter[0]:
        if vierter[2] == True:
            vierter[2] = False
        else:
            vierter[2] = True
        print("Erfolg!")
        print(f"{eingabe} online auf {vierter[2]} geändert!")
        print()
    return erster, zweiter, dritter, vierter

def get_server_offline(erster, zweiter, dritter, vierter):
    print()
    print(" "+ 16*"_"+" "+16*"_"+" ")
    print(f"|{"SERVER-NAME":^16}|{"SERVER-STATUS":^16}|")
    name_list = [erster[0]] + [zweiter[0]] + [dritter[0]] + [vierter[0]]
    off_list = [erster[2]] + [zweiter[2]] + [dritter[2]] + [vierter[2]]
    rueckgabe = []
    counter = -1
    for i in off_list:
        counter += 1
        if i == False:
            rueckgabe.append(name_list[counter])
            print("|"+ 16*"_"+"|"+16*"_"+"|")
            print(f"|{name_list[counter]:^16}|\033[1;1;31m{"offline":^16}\033[0m|")
    if rueckgabe == []:
        print()
        print("Alle Server sind online!")
    else:
        print("|"+ 16*"_"+"|"+16*"_"+"|")
        print()
        print(f"Server, die offline sind: {rueckgabe}")

main()