FLAGS = -g -XX:+PrintCompilation
JC = javac
.SUFFIXES: .java .class
.java.class:
	$(JC) $(JFLAGS) $*.java

CLASSES = Main.java\
	Estructuras/Empresa.java \
	Estructuras/Vehiculo.java \
	Estructuras/Ciudad.java \
	Estructuras/Edificacion.java \
	Estructuras/Grafo.java \
	Estructuras/Pais.java 


default: classes
classes: $(CLASSES:.java=.class)
clean:
	$(RM) *.class
