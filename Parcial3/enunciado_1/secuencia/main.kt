fun main(){

    println("Se crea una Cola: ")
    println("Se agregan a la Cola: 1, 2, 3, 4  ")


    val cola = Cola<Int>()

    cola.agregar(1)
    cola.agregar(2)
    cola.agregar(3)
    cola.agregar(4)
    
    println("Cola resultante: " + cola) // Debe imprimir [1,2,3,4]

    println("Ahora vamos a eliminar todos los elementos")
    println(cola.remover()) // Debe imprimir 1
    println(cola.remover()) // Debe imprimir 2
    println(cola.remover()) // Debe imprimir 3
    println(cola.remover()) // Debe imprimir 4
    try {
        
        cola.remover() // Debe generar un error, pues la cola esta vacia
    }
    catch(e: NoSuchElementException) {
        println(e)
    }


    println("\n\nSe crea una Pila: ")
    println("Se agregan a la Pila: 1, 2, 3, 4  ")


    val pila = Pila<Int>()

    pila.agregar(1)
    pila.agregar(2)
    pila.agregar(3)
    pila.agregar(4)
    
    println("Pila resultante: " + pila) // Debe imprimir [1,2,3,4]

    println("Ahora vamos a eliminar todos los elementos")
    println(pila.remover()) // Debe imprimir 4
    println(pila.remover()) // Debe imprimir 3
    println(pila.remover()) // Debe imprimir 2
    println(pila.remover()) // Debe imprimir 1
    try {
        
        pila.remover() // Debe generar un error, pues la pila esta vacia
    }
    catch(e: NoSuchElementException) {
        println(e)
    }


    

    
}