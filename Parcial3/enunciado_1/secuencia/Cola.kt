class Cola<T> : Secuencia<T> {

    private val cola: MutableList<T> = mutableListOf()
    
    override fun agregar(valor: T) {
        cola.add(valor)
    }
    override fun remover() : T {
        if (this.vacio()) {
            throw NoSuchElementException("Error, la cola esta vacia")
        }
        return cola.removeFirst()
    }
    override fun vacio() : Boolean {
        return cola.size == 0
    }

    override fun toString() : String {
        return cola.toString()
    }
}