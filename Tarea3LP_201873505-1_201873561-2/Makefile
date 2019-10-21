FLAGS = -g -XX:+PrintCompilation
JC = javac
.SUFFIXES: .java .class
.java.class:
	$(JC) $(JFLAGS) $*.java

CLASSES = \
	Main.java \
	Ciudad.java \
	Edificacion.java \
	Empresa.java \
	Grafo.java \
	Pais.java \
	Vehiculo.java 
default: classes
classes: $(CLASSES:.java=.class)
clean:
	$(RM) *.class


