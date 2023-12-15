class Pila<T> : Secuencia<T> {

    private val pila: MutableList<T> = mutableListOf()

    override fun agregar(valor: T) {
        pila.add(valor)
    }

    override fun remover() : T {
        if (this.vacio()) {
            throw NoSuchElementException("Error, la pila esta vacia")
        }
        return pila.removeLast()
    }

    override fun vacio() : Boolean {
        return pila.size == 0
    }

    override fun toString() : String {
        return pila.toString()
    }
}