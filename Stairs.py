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


"""







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





liste1 = (0)
liste2 = (2, 4 )
liste3 = (0, 5, 6 )
liste4 = (7, 2, 9, 10 )
liste5 = (25, 11, 1, 0, 5 )
liste6 = (1, 88, 51, 88, 61, 4 )
liste7 = (93, 12, 73, 36, 71, 65, 34 )
liste8 = (233, 5, 2, 1, 6, 7, 55, 1 )
liste9 = (16, 111, 213, 9, 23, 433, 1, 34, 13 )
liste10 =(5, 23, 453, 789, 123, 200, 212, 345, 556, 99 )
tuples = [liste1, liste2, liste3, liste4, liste5, liste6, liste7, liste8, liste9, liste10]
matrix = tuplesToMatrix(tuple)


getPaths(matrix)
print(maxSumPath(allPaths, tuplesToMatrix(tuples)))