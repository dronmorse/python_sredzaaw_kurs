#w tym przypadku, wszystkie zmienne są przypisane do tego samego obiektu (10), więc dostają ten sam id. Jeżeli zmienimy wartość,
# id też sięzmieni
a,b,c = 10,10,10
print (a,b,c,"\n%a"%id(a),id(b),id(c))

#to działa trochę dziwnie - bez appenda to tak samo jak wcześniej, ale jeżeli zappendujemy do jednej list wartość 4, appenduje
#się od razu do wszystkich (zmienne są ze sobą powiązane) ale id pozostaje takie samo dla wszystkich
a=b=c=[1,2,3]
a.append(4)
print (a,b,c,"\n%s"%id(a),id(b),id(c))

#no i tutaj niby dla małej operacji +1-1 powinien rozpoznać, że objekt (10) jest taki sam, a dla 1234567890 już nie. W praktyce
#w nowej wersji Pythona ten problem nie występuje
y = 10
x = y+1234567890-1234567890
print (id(x),id(y))