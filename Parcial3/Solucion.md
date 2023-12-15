- Universidad Simón Bolívar
- CI3641 - Lenguajes de Programación I
- Trimestre Sep-Dic 2023
- Estudiante José A. Pérez E; Carné 16-10882

---
# Examen 1
## Problema 1: Lenguaje Kotlin
Kotlin, seleccionado como el lenguaje de interés, se caracteriza por ser un lenguaje de programación de alto nivel ampliamente reconocido como multiparadigma. Aunque no es puramente funcional, permite la programación funcional y destaca por facilitar la programación orientada a objetos. Este lenguaje, considerado como el sucesor de Java, se ha ganado popularidad, especialmente en el desarrollo de aplicaciones móviles para Android. No obstante, su versatilidad se extiende a diversas áreas, como la ciencia de datos, proyectos en el lado del servidor, así como en el lado del cliente con JavaScript y JavaFX.

### a) Descripción del Lenguaje
### i. Manipulación de Objetos

En Kotlin, la creación de objetos se realiza a través del uso de clases. Estos objetos se instancian mediante la clase correspondiente, que puede tener un constructor por defecto definido como campos en la creación de la clase o uno personalizado. Por ejemplo:

```kotlin
class GrafoDirigido {
    constructor(númeroDeVértices: Int) { … }
    constructor(archivo: String) { … }
}
```

La instancia de objetos de la clase `GrafoDirigido` puede realizarse de dos maneras: proporcionando un número entero para la creación de un grafo dirigido con una cantidad específica de vértices, o suministrando el nombre de un archivo para crear un grafo a partir de un archivo con vértices y lados predefinidos.

En Kotlin, la orientación a objetos se manifiesta a través de funciones definidas dentro de las clases, conocidas como métodos. Estos métodos son, por defecto, públicos, permitiendo la manipulación de objetos fuera de la clase. Para funciones auxiliares internas, se utiliza la declaración `private fun`. La aplicación de métodos a un objeto se realiza mediante la notación `objeto.método(@args)`, y es importante destacar que los métodos pueden devolver valores o `Unit`.

Kotlin facilita la implementación de características adicionales para objetos, como comparabilidad, iterabilidad y representación en cadenas de texto, mediante la herencia de clases, permitiendo la definición de reglas específicas para objetos instanciados.

### ii. Manejo de Memoria

El lenguaje Kotlin incorpora un esquema automatizado para el manejo de memoria. Utiliza un recolector de basura para eliminar objetos o variables sin referencias, considerándolos no utilizables. Estos objetos son eliminados de la memoria, contribuyendo a la eficiencia en la gestión de recursos.

### iii. Asociación de Métodos

En Kotlin, la asociación de métodos es dinámica por defecto. En el siguiente ejemplo:

```kotlin
open class A {
    open fun f() {
        println("Función f en clase A")
    }
}

class B : A() {
    override fun f() {
        println("Función f en clase B")
    }

    fun g() {
        println("Función g en clase B")
    }
}

fun main() {
    val x: A = B() // Instancia de B asignada a una variable de tipo A
    x.f() // Llama a la versión de f() definida en B
}
```

La llamada `x.f` invocará la versión de `f` definida en la clase B si existe, basándose en el tipo dinámico de la instancia en tiempo de ejecución. Sin embargo, se puede establecer una asociación estática declarando la función `f` en `A` como final.

### iv. Jerarquía de Tipos

En Kotlin, la herencia simple se logra mediante clases. Por ejemplo:

```kotlin
class Vehículo { … }
class Auto : Vehículo { … }
class Motocicleta : Vehículo { … }
class Yamaha : Motocicleta { … }
```

La jerarquía de clases se presenta de la siguiente manera:

```
            Vehículo
            /       \
           /         \
          /           \
        Auto     Motocicleta
                        \
                         \
                          \
                        Yamaha
```

Para abordar la falta de herencia múltiple de clases, Kotlin permite el uso de interfaces. Además, el lenguaje presenta soporte para polimorfismo paramétrico, permitiendo la creación de clases o funciones que no están limitadas a un tipo específico, sino que operan sobre un tipo genérico. Cabe destacar que en la jerarquía de tipos en Kotlin, todas las clases heredan de `Any`, que cumple el papel de raíz en la jerarquía, siendo análogo a `Object` en Java pero con menos métodos.

En cuanto a la manipulación de tipos "nullable", Kotlin introduce el uso de `?` para declarar tipos nulos, permitiendo que una variable pueda contener el valor `null` además de los valores del tipo especificado. La jerarquía de tipos se adapta para manejar nulos, y cualquier tipo puede tener una versión nullable.

En el ámbito del manejo de la varianza, Kotlin admite la especificación de cómo se relacionan los subtipos y supertipos en situaciones de uso mediante las anotaciones `in`, `out` y `inout` en las declaraciones de tipo. Por ejemplo, se puede tener `List<out T>`, indicando que la lista produce valores de tipo `T`, permitiendo obtener valores pero prohibiendo la adición de nuevos elementos.


### b) Implementación de *Secuencia* y *Grafo*

PENDIENTE POR AGREGAR ESTE ENLACE [enlace en línea](http://www.limni.net)




---
## Problema 2: Lenguaje Ruby

Mi primer nombre es **José**, 4 letras. El lenguaje escogido es **Ruby**

### a) Descripción del lenguaje

En Ruby, la concurrencia se puede lograr mediante varias opciones, y la implementación específica puede depender del contexto y de las necesidades del desarrollador. A continuación, se presenta una descripción general de los mecanismos de concurrencia en Ruby:

### **i. Capacidades nativas, librerías o herramientas externas:**
Ruby proporciona capacidades nativas para la concurrencia a través de la implementación de hilos y procesos. Los hilos (threads) permiten la ejecución concurrente dentro del mismo proceso, mientras que los procesos permiten la ejecución concurrente en diferentes procesos independientes. Además, Ruby también cuenta con librer

ías y gemas (paquetes de software) que ofrecen abstracciones más avanzadas para la concurrencia, como Celluloid, Concurrent Ruby, y otras basadas en el modelo de actores.

### **ii. Creación/manejo de tareas concurrentes y control de memoria compartida/pasaje de mensajes:**
- **Hilos (Threads):** Ruby permite la creación de hilos mediante la clase `Thread`. Los hilos comparten el espacio de memoria del proceso principal, lo que facilita el acceso a variables compartidas. Sin embargo, esto también puede llevar a problemas de sincronización y condiciones de carrera si no se manejan adecuadamente.

  ```ruby
  thread = Thread.new do
    # Código concurrente
  end
  ```

- **Procesos:** Ruby facilita la creación de procesos independientes mediante la clase `Process`. Los procesos tienen su propio espacio de memoria, lo que evita problemas de sincronización, pero también implica una comunicación más compleja entre ellos, generalmente a través de mecanismos como tuberías (pipes) o sockets.

  ```ruby
  process = Process.fork do
    # Código concurrente en un nuevo proceso
  end
  ```

- **Memoria compartida y pasaje de mensajes:** Para compartir datos entre hilos, se pueden utilizar variables compartidas o estructuras de datos específicas como `Mutex` para garantizar la sincronización adecuada. Para la comunicación entre procesos, se pueden utilizar IPC (Inter-Process Communication) mediante tuberías, sockets o mecanismos más avanzados proporcionados por las librerías de concurrencia.

### **iii. Mecanismo de sincronización:**
Ruby proporciona varios mecanismos de sincronización para manejar concurrencia y evitar problemas como condiciones de carrera. Algunos de los principales mecanismos son:
- **Mutex:** La clase `Mutex` (Mutual Exclusion) se utiliza para envolver secciones críticas de código, garantizando que solo un hilo puede ejecutar ese código a la vez.

  ```ruby
  mutex = Mutex.new
  mutex.synchronize do
    # Código crítico
  end
  ```

- **Condition Variable:** La clase `ConditionVariable` se utiliza junto con un `Mutex` para implementar comunicación entre hilos mediante señales.

  ```ruby
  mutex = Mutex.new
  condition = ConditionVariable.new

  # En un hilo
  mutex.synchronize do
    # Código que espera una condición
    condition.wait(mutex)
  end

  # En otro hilo
  mutex.synchronize do
    # Código que señala la condición
    condition.signal
  end
  ```

### b) Implementacion de *ProductoPunto* y *ContadorDirectorios*

PENDIENTE POR AGREGAR ESTE ENLACE [enlace en línea](http://www.limni.net)

---

## Problema 3: Ejecucion dinamica y estatica de Metodos:
Carné 16-10882.

Valor de las constantes: 
- X = 8
- Y = 8
- Z = 2

Pseudo codigo:
```kotlin
class Abra {
  int a = 8, b = 8

  fun cus(int x): int {
    a = b + x
    return pide(a)
  }

  fun pide(int y): int {
    return a - y * b
  }
}

class Cadabra extends Abra {
  Abra zo = new PataDeCabra()

  fun pide(int y): int {
    return zo.cus(a + b) - y
  }
}

class PataDeCabra extends Cadabra {
  int b = 10, c = 2
 
  fun cus(int x): int {
    a = x - 3
    c = a + b * c
    return pide(a * b + x)
  }
  
  fun pide(int y): int {
    return c - y * a
  }
}
```
Considere además el siguiente fragmento de código:

```kotlin
Abra ho = new Cadabra()
Abra po = new PataDeCabra()
Cadabra cir = new PataDeCabra()
print(ho.cus(9) + po.cus(9) + cir.cus(3))
```

## Solucion:

### Asociacion Estatica:


Marco de pila global:

|  | Marco de pila    |
|:-:       |:-:        |
|ho     |Abra|
|po    |Abra|
|cir      |Cadabra|
|print | ho.cus(9) + po.cus(9) + cir.cus(3)|


**Entonces, ahora veamos `ho.cus(9)`. Notemos que el metodo `cus` se refiere al de la Clase `Abra`, pues la asociacion es estatica:**

Marco de Pila:

|  | ho.cus(9)      |
|:-:       |:-:        |
|a      | 8 + 9 = 17|
|b       |8|
|x      |9|
return | pide(17)|

Notese que `pide(17)` se refiere al metodo en la Clase `Abra`. Veamos su marco de pila:

Marco de Pila
|  | pide(y)      |
|:-:       |:-:        |
|a      |17|
|b       |8|
|y     |17|
return | 17-17*8|

Asi, `ho.cus(9)` retorna `-119`

**Ahora veamos para `po.cus(9)`. Notemos que el objeto `po` tambien es del tipo `Abra`, por lo que la ejecucion del metodo `po.cus(9)` es analoga a `ho.cus(9)`**.

Asi, `po.cus(9)` retorna `-119`.

Ahora, veamos para `cir.cus(3)`:

`cir` es del tipo `Cadabra`, pero `Cadabra` no tiene el metodo `cus` implementado directamente, sino que hereda este de la Clase `Abra`, asi, se abre el marco de pila:


Marco de Pila:

|  |cir.cus(3)      |
|:-:       |:-:        |
|a      | 8 + 3 = 11|
|b       |8|
|x      |3|
return | pide(11)|

Abrimos el marco de pila para pide(11)

Marco de pila:
|  | pide(y)      |
|:-:       |:-:        |
|a      |8|
|b       |8|
|zo|Abra|
|y     |11|
return | zo.cus(16)-11|

`zo` es instancia de`Abra`, asi que abrimos su marco de pila:

Marco de Pila:

|  | zo.cus(x)      |
|:-:       |:-:        |
|a      | 8 + 16 = 24|
|b       |8|
|x      |16|
return | pide(24)|

Marco de pila:


|  | pide(y)      |
|:-:       |:-:        |
|a      | 24|
|b       |8|
|y      |24|
return | 24-24*8|

asi, `zo.cus(16)` retorna `-168-11 = -179`.

Finalmente, el programa imprime:`-417`