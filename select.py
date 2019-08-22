import re
import collections


def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())


select_STTM = r" *SELECT  *(( *(\w+)( *, *(\w+))*)|(\*))  *FROM  *(.*)( *INNER JOIN  *(\w+))? *( ORDER BY  *(\w+)  *((ASC|DESC)))? *;"
where_STTM = r"blah"
valid = re.compile(select_STTM + inner_join_STTM)

insert_Regex = r" *INSERT  *INTO  *(\w+) *\( *(\w+) *( *, *(\w+))* *\) *VALUES *\( *(\w+) *( *, *(\w+) *)* *\) *;"


print ("ingrese query: \n")
statement = input()

columnas = valid.match(statement).groups()[0]
tabla = valid.match(statement).groups()[3]

if (len(columnas) > 1):
    columnas = re.split(r'\W+', columnas)
    print ("columnas:")
    print (columnas)
    # DO some magic here

    for col in columnas:
        print (col)
        # search col in the file's first line, get the index and print each line[index] 

else : # (columnas = "*")
    print ("columnas:")
    print (columnas)

print(tabla)

#file test
file = open("csv1.csv", "r")
for linea in file:
    print (linea)
file.close()