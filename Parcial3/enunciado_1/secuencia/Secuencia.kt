interface Secuencia<T> {
    fun agregar(valor: T)
    fun remover(): T 
    fun vacio(): Boolean 
}