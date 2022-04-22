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
def getPaths(matrix, path=[], row=0, coloumn=0):
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
    
    path.pop() #Fjerner siste elementet fra pathen, 



matrix = [
    [1, 2, 3,243],
    [4, 5, 6,234],
    [7, 8, 9,235],
    [23,454,2,123]
]



getPaths(matrix)
print(allPaths)