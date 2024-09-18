import signal
def zeit_abgelaufen (sig, frame):
    raise TimeoutError

def pfandEinwurf (betrag, einwurf):
    match (inputValidation (einwurf)):
        case "glas":
            betrag += 0.1
        case "plastik":
            betrag += 0.15
        case "dose":
            betrag += 0.25
        case _:
            print ("Du dulli, das gehört hier nicht rein")
    return betrag

def inputValidation (einwurf):
    if (einwurf in {"glas", "plastik", "dose"}):
        return einwurf
    else:
        return None

def beenden (pfand):
    print (f"Pfand: {pfand}€")

if __name__ == '__main__':
    print ("Schreibe 'exit' um den Einwurf zu beenden")
    pfand = 0.0
    signal.signal(signal.SIGALRM, zeit_abgelaufen)
    signal.alarm(5)
    try:
        while (True):
            einwurf = input ("Einwurf: ").lower ()
            signal.alarm (5) #Reset the timer
            if (einwurf == "exit"):
                beenden (pfand)
                break
            pfand = pfandEinwurf (pfand, einwurf)
    except TimeoutError:
        print ("Zeit abgelaufen")
        beenden (pfand)