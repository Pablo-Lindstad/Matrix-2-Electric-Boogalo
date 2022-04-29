allPaths = [] #Tom liste, som skal ha alle pathene
def getPaths(matrix, path=[], row=0, coloumn=0): #Funksjon for å finne alle pather fra [0][0] til [-1][-1] i en matrise, tar en liste som input og har også med path, rad og kolumne som brukes til å gjøre den rekursiv, men er satt til null som default, som output gir den en liste med alle pathene i form av "kordinater", altså indexer
    #Finner antall rader og kolumner
    rows = len(matrix) 
    coloumns = len(matrix[0])
    #Sjekker om vi har nåd enden av matrisen, altså nederste rad og borteste kolumne
    if row == rows - 1 and coloumn == coloumns - 1:
        global allPaths #Gjør listen om til en global variabel for å kunne legge til pather fra inni funksjonen
        allPaths.append(path + [matrix[row][coloumn]]) #Legger til pathen til listen med alle paths, på slutten av pathen legges det siste elementet i matrisen, altså det som har blitt nåd
        return #Returnerer

    path.append(matrix[row][coloumn]) #Legger til posisjonen til pathen

    if row < rows and coloumn + 1 < coloumns: #Sjekker om vi har nåd høyre side av matrisen, ved å se om det er et element til til høyre
        getPaths(matrix, path, row, coloumn + 1) #Om vi ikke er det kjøres funksjonen rekursivt fra elementet til høyre
 
    if row + 1 < rows and coloumn < coloumns: #Samme som over, bare nedover, så når den har nåd høyre side av en matrise går den ned en rad og fortsetter
        getPaths(matrix, path, row + 1, coloumn)
    
    path.pop() #Fjerner siste elementet fra pathen
"""
Koden starter øverst i venstre hjørne og skal nederst til venstre, den gjør det ved å rekursivt gå igjennom matrisen for å få hver path, den starter ved å sjekke om den har nåd enden av matrisen, om den har det legger den pathen til i en liste med alle pather.
Om den ikke har nåd enden av pathen legger den til posisjonen i pathen, deretter sjekker den om det er et element til høyre, om det er det kaller den funksjonen fra det punktet som da også blir lagt til i matrisen.
Deretter sjekker den om det er et punkt under, om det er det kaller den på funksjonen fra punktet under.
Til slutt så fjerner den objektet fra pathen, dermed kommer den først til å gå helt til høyre og rett ned første som første path, deretter vil den fjerne elementer så den kommer et punkt tilbake og vil da gå ned et punkt fra høyre og etter det til høyre.
Den fortsetter til den har gått igjennom alle pather og lagt den til i listen.
"""
