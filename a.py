allPaths = [] #Tom liste, som skal ha alle pathene
def getPaths(matrix, path=[], row=0, coloumn=0): #Funksjon for å finne alle pather fra [0][0] til [-1][-1] i en matrise, tar en liste som input og har også med path, rad og kolumne som brukes til å gjøre den rekursiv, men er satt til null som default, som output gir den en liste med alle pathene i form av "kordinater", altså indexer
    #Finner antall rader og kolumner
    rows = len(matrix) 
    coloumns = len(matrix[0])
    print("START")
    #Sjekker om vi har nåd enden av matrisen, altså nederste rad og borteste kolumne
    if row == rows - 1 and coloumn == coloumns - 1:
        print("FERDIG")
        global allPaths #Gjør listen om til en global variabel for å kunne legge til pather fra inni funksjonen
        allPaths.append(path + [matrix[row][coloumn]]) #Legger til pathen til listen med alle paths, på slutten av pathen legges det siste elementet i matrisen, altså det som har blitt nåd
        return #Returnerer

    path.append(matrix[row][coloumn]) #Legger til posisjonen til pathen

    if row < rows and coloumn + 1 < coloumns: #Sjekker om vi har nåd høyre side av matrisen, ved å se om det er et element til til høyre
        print ("HØYRE")
        getPaths(matrix, path, row, coloumn + 1) #Om vi ikke er det kjøres funksjonen rekursivt fra elementet til høyre
 
    if row + 1 < rows and coloumn < coloumns: #Samme som over, bare nedover, så når den har nåd høyre side av en matrise går den ned en rad og fortsetter
        print ("NEDE")
        getPaths(matrix, path, row + 1, coloumn)
    
    print (path)
    path.pop() #Fjerner siste elementet fra pathen, 
    print (path)
    print()



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

getPaths(matrix)
print(allPaths)