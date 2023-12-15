KC=	kotlinc
KFLAG=	-cp

all:	\
	Grafo.class \
	MainKt.class
	
Grafo.class: Grafo.kt
	$(KC) Grafo.kt

MainKt.class: main.kt Grafo.class 
	$(KC) $(KFLAG) . main.kt
clean:
	rm -rf *.class META-INF