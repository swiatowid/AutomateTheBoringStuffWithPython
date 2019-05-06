#! python3

tableData = [['apples', 'oranges', 'cherries', 'bananas'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]


def printTable(n):
    for j in range(len(n[0])):
          
        for i in range(len(n)):    
            margin = len(max(n[i], key = len)) #użycie max dla list NIE wygląda max(len...)
            print(n[i][j].rjust(margin), end = ' ') # end pozwala na kontynuację print w jednym wierszu
            i = i + 1
        
        print('') # Zamiana wiersza  

            
printTable(tableData) 