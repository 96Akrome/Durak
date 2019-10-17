FLAGS = -g -XX:+PrintCompilation
JC = javac
.SUFFIXES: .java .class
.java.class:
        $(JC) $(JFLAGS) $*.java
CLASSES =
	Grafo.java

default: classes
classes: $(CLASSES:.java=.class)
clean:
	$(RM) *.class
