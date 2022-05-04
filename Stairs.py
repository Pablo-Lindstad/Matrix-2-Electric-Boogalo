def tuplesToMatrix(tuples): #Funksjon for å gjøre en liste med tuples om til en matrix, tar en liste med tuples som input og gir en matrix av de samme listene som output.
    matrix = [] #Ny matrix
    for tuple in tuples: #Går igjennom hver tuple i listen med tuples
        try: #Om det er en tuple med flere elementer
            temp = [] #Ny liste for å sende til matrixen
            for number in tuple: #Går igjennom hvert tall i tupelen
                temp.append(number) #Legger til tallet i listen
            matrix.append(temp) #Legger til listen til matrixen
        except TypeError: #Om tupelen kun har et element
            temp = [] #Liste for å sende til matrixen
            temp.append(tuple) #Legger til elementet til listen
            matrix.append(temp) #Legger listen til matrixen
    return (matrix) #Returnerer matrixen



allPaths = [] #Tom liste, som skal ha alle pathene
def getPaths(matrix, path=[], row=0, coloumn=0): #Funksjon for å finne alle pather fra [0][0] til nederste rad i en matrise, tar en liste som input og har også med path, rad og kolumne som brukes til å gjøre den rekursiv, men er satt til null som default, som output gir den en liste med alle pathene i form av "kordinater", altså indexer
    #Finner antall rader og kolumner på den raden den er
    rows = len(matrix) 
    coloumns = len(matrix[coloumn])
    #Sjekker om vi har nåd nederste raden i matrisen
    if row == rows - 1:
        global allPaths #Gjør listen om til en global variabel for å kunne legge til pather fra inni funksjonen
        allPaths.append(path + [[row,coloumn]]) #Legger til pathen til listen med alle paths, på slutten av pathen legges det siste elementet i matrisen, altså det som har blitt nåd
        return #Returnerer
    path.append([row,coloumn]) #Legger til posisjonen til pathen
    if row + 1 < rows and coloumn - 1 > -1: #Sjekker om det er et element en rad under og til venstre for den nåverende posisjonen
        getPaths(matrix, path, row + 1, coloumn - 1) #Om det er det kjøres funksjonen rekursivt fra det elementet
    if row + 1 < rows: #Sjekker om det er en rad under for den nåverende posisjonen
        getPaths(matrix, path, row + 1, coloumn) #Om det er det kjøres funksjonen rekursift fra elementet på samme posisjon på raden under
    if row + 1 < rows and coloumn + 1 <= coloumns: #Sjekker om det er element på raden under til høre for den nåverende posisjonen
        getPaths(matrix, path, row + 1, coloumn + 1) #Om det er det kjøres funksjonen rekursivt fra den posisjonen
    path.pop() #Fjerner siste elementet fra pathen
"""
Koden starter øverst i venstre hjørne og skal nederst til venstre, den gjør det ved å rekursivt gå igjennom matrisen for å få hver path, den starter ved å sjekke om den har nåd enden av matrisen, om den har det legger den pathen til i en liste med alle pather.
Om den ikke har nåd enden av pathen legger den til posisjonen i pathen, deretter sjekker den om det er et element til høyre, om det er det kaller den funksjonen fra det punktet som da også blir lagt til i matrisen.
Deretter sjekker den om det er et punkt under, om det er det kaller den på funksjonen fra punktet under.
Til slutt så fjerner den objektet fra pathen, dermed kommer den først til å gå helt til høyre og rett ned første som første path, deretter vil den fjerne elementer så den kommer et punkt tilbake og vil da gå ned et punkt fra høyre og etter det til høyre.
Den fortsetter til den har gått igjennom alle pather og lagt den til i listen.

Programmet starter på første raden og skal ned til nederste rad, den gjør det ved å kjøre rekusivt igjennom matrisen for å få hver path, den starter ved å sjekke om den har nåd nederste rad, om den har det legger den pathen til i listen med pather.
Om den ikke har nåd enden legger den til posisjonen i pathen
Så sjekker den om det er et element på posisjonen til venstre en rad under, om det er det kjører den koden derifra, deretter gjør den det samme med rett under og under og til venstre
Til slutt fjerner den posisjonen fra pathen, altså går et skritt tilbake så pathen blir riktig
Så når koden kjører vil den først gå rett ned, deretter gå ned til nest siste og deretter til høyre og så ned, så til høyre 2 fra bunn osv.
"""



def minSumPath(paths,matrix): #Funksjon for å finne pathen i en liste med pather som har den laveste verdien igjennom en matrise, tar en liste med pather og matrisen den gjelder til som input og gir verdien av den laveste pathen igjennom matrisen som output
    minSum = 0 #Variabel for den minste summen
    for path in paths: #Går igjennom hver path
        sum = 0 #Sum av denn pathen
        for coordinate in path: #Går igjennom hver kordinat i pathen
            sum += matrix[coordinate[0]][coordinate[1]] #Legger til verdien av kordinaten til pathen
        if sum < minSum or minSum == 0: #Sjekker om summen av pathen er mindre en den minste summen eller om det er den første pathen
            minSum = sum #Om det er det blir det den nye minste pathen
    return minSum #Returnerer den minste pathen



def maxSumPath(paths, matrix): #Funksjon for å finne pathen i en liste med pather som har den høyeste verdien igjennom en matrise, tar en liste med pather og matrisen den gjelder til som input og gir verdien av den høyeste pathen igjennom matrisen som output
    maxSum = 0 #Variabel for den største summen
    for path in paths: #Går igjennom hver path
        sum = 0 #Sum av denne pathen
        for coordinate in path: #Går igjennom hver koordinat i pathen
            sum += matrix[coordinate[0]][coordinate[1]] #Legger til verdien av kordinaten til summen
        if sum > maxSum or maxSum == 0: #Sjekker om summen av pathen er større en den største påathen eller om det er den første pathen
            maxSum = sum #Setter summen til maxsummen
    return maxSum #Returnerer den største summen



def minSum(matrix): #Funksjon for å finne ruten igjennom en matrix med økende lengde på kolonner med laveste sum, tar en matrix som har 1 tall på første rad, 2 på andre osv. som input og gir summen på den pathen som har lavest verdi som output.
    rows = len(matrix) #Finner antall rader
    for row in range(0,rows): #Går over hver rad
        for coloumn in range(0,row+1): #Går over hver kolonne
            if row == 0: #Sjekker om det er det første elementet
                pass #Om det er det kan vi fortsette siden det ikke har noen tall over seg
            elif row == 1 and coloumn == 0: #Sjekker om det er første objektet i andre rad
                matrix[row][coloumn] += matrix[0][0] #Om det er det kan vi legge på første tallet siden det er det eneste over
            elif coloumn == 0: #Sjekker om det er første kolonne, så tredje rad og nedover
                matrix[row][coloumn] += min(matrix[row-1][coloumn], matrix[row-1][coloumn+1]) #Om det er det så velger den fra tallet over og det over og til høyre siden det er alle mulighetene
            elif coloumn == len(matrix[row])-1: #Sjekker om det er tallet helt ytterst på kolonnen
                matrix[row][coloumn] += matrix[row-1][coloumn-1] #Om det er det har den kun tallet over til venstre å velge fra
            elif coloumn == len(matrix[row])-2: #Sjekker om det er tallet nest ytterst på hver kolonne 
                matrix[row][coloumn] += min(matrix[row-1][coloumn-1],matrix[row-1][coloumn]) #Om det er det har den kun tallet over og over og til venstre å velge mellom
            else: #Om det er ingen av de andre
                matrix[row][coloumn] += min(matrix[row-1][coloumn-1], matrix[row-1][coloumn], matrix[row-1][coloumn+1]) #Da har den alle de tre tallene over seg og velger mellom over og til venstre, rett over og over og til høyre
    return min(matrix[-1]) #Returnerer det minste tallet på den nederste raden
#Funksjonen vil gå igjennom hver rad og kolonne og finne det valget som er billigst underveis og legge dette til seg selv, ved å gjøre dette finner vi på nederste raden den billigste måten å komme til hver av de stedene på og kan da velge den laveste



def maxSum(matrix): #Funksjon for å finne ruten igjennom en matrix med økende lengde på kolonner med laveste sum, tar en matrix som har 1 tall på første rad, 2 på andre osv. som input og gir summen på den pathen som har størst verdi som output.
    rows = len(matrix) #Finner antall rader
    for row in range(0,rows): #Går over hver rad
        for coloumn in range(0,row+1): #Går over hver kolonne
            if row == 0: #Sjekker om det er det første elementet
                pass #Om det er det kan vi fortsette siden det ikke har noen tall over seg
            elif row == 1 and coloumn == 0: #Sjekker om det er første objektet i andre rad
                matrix[row][coloumn] += matrix[0][0] #Om det er det kan vi legge på første tallet siden det er det eneste over
            elif coloumn == 0: #Sjekker om det er første kolonne, så tredje rad og nedover
                matrix[row][coloumn] += max(matrix[row-1][coloumn], matrix[row-1][coloumn+1]) #Om det er det så velger den fra tallet over og det over og til høyre siden det er alle mulighetene
            elif coloumn == len(matrix[row])-1: #Sjekker om det er tallet helt ytterst på kolonnen
                matrix[row][coloumn] += matrix[row-1][coloumn-1] #Om det er det har den kun tallet over til venstre å velge fra
            elif coloumn == len(matrix[row])-2: #Sjekker om det er tallet nest ytterst på hver kolonne 
                matrix[row][coloumn] += max(matrix[row-1][coloumn-1],matrix[row-1][coloumn]) #Om det er det har den kun tallet over og over og til venstre å velge mellom
            else: #Om det er ingen av de andre
                matrix[row][coloumn] += max(matrix[row-1][coloumn-1], matrix[row-1][coloumn], matrix[row-1][coloumn+1]) #Da har den alle de tre tallene over seg og velger mellom over og til venstre, rett over og over og til høyre
    return max(matrix[-1]) #Returnerer det største tallet på den nederste raden
#Funksjonen vil gå igjennom hver rad og kolonne og finne det valget som er dyrest underveis og legge dette til seg selv, ved å gjøre dette finner vi på nederste raden den dyreste måten å komme til hver av de stedene på og kan da velge den høyeste