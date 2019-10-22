FLAGS = -g
JC = javac
.SUFFIXES: .java .class
.java.class:
	$(JC) $(JFLAGS) $*.java

CLASSES =  Main.java\
	Estructuras/Empresa.java \
	Estructuras/Vehiculo.java \
	Estructuras/Edificacion.java \
	Estructuras/Ciudad.java \
	Estructuras/Grafo.java \
	Estructuras/Pais.java

default: classes
classes: $(CLASSES:.java=.class)

Main.class: Empresa.class Vehiculo.class Ciudad.class Edificacion.class Grafo.class Pais.class

clean:
	$(RM) *.class
