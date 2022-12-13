colors = ["red","orange","green","violet","blue","yellow"]

def CreateColorTable(color,n):
    return color[:n+1]

for i in range(0,len(colors)):
    print (CreateColorTable(colors,i))

text = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli."

print (text[10:69])