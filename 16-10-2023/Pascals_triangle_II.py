class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Maak een lijst 'driehoek' met 'rowIndex+1' lege lijsten
        driehoek = []
        for i in range(0, rowIndex + 1):
            driehoek.append([])

        # Vul de eerste rij van de driehoek met 1
        driehoek[0].append(1)

        # Vul de randen van de driehoek met 1
        for i in range(1, rowIndex + 1):
            driehoek[i].append(1)
            driehoek[i].append(1)

        # Bereken de waarden binnen de driehoek
        for i in range(2, rowIndex + 1):
            for j in range(1, len(driehoek[i]) - 1):
                # De waarde is de som van twee waarden bovenaan in de vorige rij
                driehoek[i][j] += driehoek[i - 1][j - 1] + driehoek[i - 1][j]

        # Retourneer de rowIndex-rij van de driehoek
        return driehoek[rowIndex]


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a=rowIndex
        b=[]
        for i in range(0,a+1) :
            b.append([])
        print(b)
        b[0].append(1)
        for i in range(1,a+1) :
            for j in range(0,i+1) :
                b[i].append(0)
        for i in range(1,a+1) :
            b[i][0]=1
            b[i][len(b[i])-1]=1
        for i in range(2,a+1) :
            for j in range(1,len(b[i])-1) :
                b[i][j]+=b[i-1][j-1]+b[i-1][j]
        return b[a]





