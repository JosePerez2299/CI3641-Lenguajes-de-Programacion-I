KC=	kotlinc
KFLAG=	-cp

all:	\
	Secuencia.class \
	Pila.class \
	Cola.class \
	MainKt.class
	
Secuencia.class: Secuencia.kt
	$(KC) Secuencia.kt

Pila.class: Pila.kt Secuencia.class
	$(KC) $(KFLAG) . Pila.kt

Cola.class: Cola.kt Secuencia.class
	$(KC) $(KFLAG) . Cola.kt

MainKt.class: main.kt Cola.class Pila.class
	$(KC) $(KFLAG) . main.kt
clean:
	rm -rf *.class META-INF