import re
import collections


def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())


select_STTM = r"(?: )*SELECT ((?: )*\w+(((?: )*,(?: )*\w+)*)?|\*)(?: )* FROM (\w+)"
inner_join_STTM = r"( INNER JOIN (?: )*\w+)?"

valid = re.compile(select_STTM + inner_join_STTM)
#print(displaymatch(valid.match("SELECT aasdfa , asdasd FROM tabla")))
statement = "SELECT col1 , col2 FROM tabla"
print ("columnas = " + (valid.match(statement)).groups()[0] + " from: " + (valid.match(statement)).groups()[3] )


update_STTM = r"(?: )*UPDATE (?: )*(\w+) (?: )*SET (?: )*(\w+)(?: )*=(?: )* (?: )*(\w+)((?: )*,(?: )*(\w+)(?: )*=(?: )*(\w+))*"
statement = "UPDATE tabla SET columna = valor , col2 = val2, col3     =               val3, col4=val4"

