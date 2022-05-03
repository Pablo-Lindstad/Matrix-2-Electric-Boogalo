def minSum(list): #Funksjon for å finne pathen igjennom en matrise som har lavest "kostnad", tar en matrise som input og gir deg summen på den laveste pathen som output
    rows = len(list) #Finner antall rader og kolumner
    coloumns = len(list[0])
    for row in range(0,rows): #Går over alle radene
        for coloumn in range(0,coloumns): #Går over alle kollumnene, så den går igjennom kollumnen og når den kommer helt til høyre går den ned en rad
            if row == 0 and coloumn == 0: #Sjekker om det er første element i matrisen, om det er det gjøres ingenting siden den ikke har noen elementer over eller til venstre
                pass
            elif row == 0: #Sjekker om det er første raden, om det er det er det ingen elementer over og vi tar derfor å automatisk legger til tallet til venstre
                list[row][coloumn] += list[row][coloumn-1]
            elif coloumn == 0: #Sjekker om det er første kollumnen, om det er det er det ingen elementer til venstre så vi legger på tallet over
                list[row][coloumn] += list[row-1][coloumn]
            else: #Om det ikke er i første kollonen eller raden
                if list[row-1][coloumn] < list[row][coloumn-1]: #Sjekker om elementet over er mindre en det til høyre, om det er det legges det på 
                    list[row][coloumn] += list[row-1][coloumn]
                else: #Om ikke legges det andre på
                    list[row][coloumn] += list[row][coloumn-1]
    return(list[rows-1][coloumns-1]) #Returnerer siste element
#Funksjonen vil gå igjennom matrisen kollumne for kollumne og rad for rad og vil velge det tallet som er mindre for å ende opp med den ideele pathen, altså den minste summen i siste element



def maxSum(list): #Funksjon for å finne pathen igjennom en matrise som har høyest "kostnad", tar en matrise som input og gir deg summen på den høyeste pathen som output
    rows = len(list) #Finner antall rader og kolumner
    coloumns = len(list[0])
    for row in range(0,rows): #Går over alle radene
        for coloumn in range(0,coloumns): #Går over alle kollumnene, så den går igjennom kollumnen og når den kommer helt til høyre går den ned en rad
            if row == 0 and coloumn == 0: #Sjekker om det er første element i matrisen, om det er det gjøres ingenting siden den ikke har noen elementer over eller til venstre
                pass
            elif row == 0: #Sjekker om det er første raden, om det er det er det ingen elementer over og vi tar derfor å automatisk legger til tallet til venstre
                list[row][coloumn] += list[row][coloumn-1]
            elif coloumn == 0: #Sjekker om det er første kollumnen, om det er det er det ingen elementer til venstre så vi legger på tallet over
                list[row][coloumn] += list[row-1][coloumn]
            else: #Om det ikke er i første kollonen eller raden
                if list[row-1][coloumn] > list[row][coloumn-1]: #Sjekker om elementet over er større en det til høyre, om det er det legges det på 
                    list[row][coloumn] += list[row-1][coloumn]
                else: #Om ikke legges det andre på
                    list[row][coloumn] += list[row][coloumn-1]
    return(list[rows-1][coloumns-1]) #Returnerer siste element
#Funksjonen vil gå igjennom matrisen kollumne for kollumne og rad for rad og vil velge det tallet som er mindre for å ende opp med den ideele pathen, altså den minste summen i siste element



allPaths = [] #Tom liste, som skal ha alle pathene
def getPaths(matrix, path=[], row=0, coloumn=0): #Funksjon for å finne alle pather fra [0][0] til [-1][-1] i en matrise, tar en liste som input og har også med path, rad og kolumne som brukes til å gjøre den rekursiv, men er satt til null som default, som output gir den en liste med alle pathene i form av "kordinater", altså indexer
    #Finner antall rader og kolumner
    rows = len(matrix) 
    coloumns = len(matrix[0])
    #Sjekker om vi har nåd enden av matrisen, altså nederste rad og borteste kolumne
    if row == rows - 1 and coloumn == coloumns - 1:
        global allPaths #Gjør listen om til en global variabel for å kunne legge til pather fra inni funksjonen
        allPaths.append(path + [[row, coloumn]]) #Legger til pathen til listen med alle paths, på slutten av pathen legges det siste elementet i matrisen, altså det som har blitt nåd
        return #Returnerer
    path.append([row, coloumn]) #Legger til posisjonen til pathen
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

"""
Min
5445
6012
7143
6566
6393
5390

Max
12052
13721
13248
12761
12582
11824
"""