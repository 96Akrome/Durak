FLAGS = -g -XX:+PrintCompilation
JC = javac
.SUFFIXES: .java .class
.java.class:
	$(JC) $(JFLAGS) $*.java



CLASSES = \
	Estructuras/Empresa.java \
	Estructuras/Vehiculo.java \
	Estructuras/Edificacion.java \
	Estructuras/Ciudad.java \
	Estructuras/Grafo.java \
	Estructuras/Pais.java

default: classes

Vehiculo.class: Empresa.class
Ciudad.class: Edificacion.class
Grafo.class: Ciudad.class
Pais.class : Grafo.class
Main.class: Empresa.class Vehiculo.class Ciudad.class Edificacion.class Grafo.class Pais.class

classes: $(CLASSES:.java=.class)

clean:
	$(RM) *.class
