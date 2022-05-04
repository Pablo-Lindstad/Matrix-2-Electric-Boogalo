def mazeValid(maze): #Funksjon for å sjekke om det finnes en vei igjennom en labyrint, hvor 1 er gyldig vei og 0 er ugyldig, tar en maze som input, altså en matrix med 1 og 0 for å indikere vegger og gir True som output om det finnes en gyldig vei igjennom og False om det ikke gjør det
    visited = [] #Lager en liste for besøkte kordinater
    queue = [[0,0]] #Lager en liste som skal fungere som queue, legger startpunktet inni den
    while len(queue) > 0: #Går så lenge det er igjen elementer i queuen, altså så lenge det er ubesøkte ruter
        temp = queue.pop(0) #Tar første elementet fra queuen og finner rad og kolonne
        row = temp[0]
        coloumn = temp[1]
        rows = len(maze) #Finner antall rader og kolonner
        coloumns = len(maze[0])
        visited.append([row,coloumn]) #Legger til kordinatene i listen med besøkte elementer 

        up = [row+1,coloumn] #Lager kordinater for hver av retningene den kan bevege seg
        down = [row-1,coloumn]
        right = [row,coloumn+1]
        left = [row,coloumn-1]
        directions = [up,down,right,left]

        for direction in directions: #Går over hver av retningene
            if direction == [rows-1, coloumns-1]: #Sjekker om den har nåd slutten av labyrinten
                return True #Om den har det returnerer den true
            elif direction in visited: #Sjekker om den allerede har vært innom kordinatene
                continue #Om den har vært innom går den til neste kordinat
            elif direction[0] < 0 or direction[1] < 0 or direction[0] > rows-1 or direction[1] > coloumns-1: #Sjekker om kordinatene er innafor mazen
                continue #Om det er utenfor så går den til neste kordinaten
            elif maze[direction[0]][direction[1]] == 0: #Om den ikke kan bevege seg til kordinaten
                continue #Fortsetter til neste kordinat
            elif maze[direction[0]][direction[1]] == 1: #Om den kan bevege seg til kordinaten 
                queue.append(direction) #Legger til kordinaten i køen
    return False #Om den går igjennom alle kordinatene og ikke finner en vei til slutten returnerer den false