/**
 * Clase que representa un grafo y proporciona métodos para agregar arcos
 * y realizar búsquedas en el grafo utilizando BFS y DFS.
 *
 * @param size Tamaño del grafo (número de vértices).
 */
public class Grafo(val size: Int) {
    // Lista de adyacencias para representar el grafo
    private var adyacencias = MutableList(size) { mutableListOf<Int>() }

    /**
     * Método para agregar un arco al grafo.
     * No hace nada si el arco ya existe. Lanza una RuntimeException si uno de los vértices
     * no pertenece al grafo.
     *
     * @param verticeInicial Vértice inicial del arco.
     * @param verticeFinal Vértice final del arco.
     */
    fun agregarArco(verticeInicial: Int, verticeFinal: Int) {
        if (verticeInicial !in 0 until size || verticeFinal !in 0 until size) {
            throw RuntimeException("${verticeInicial} o ${verticeFinal} no pertenecen al grafo")
        } 
        
        if (verticeFinal in adyacencias[verticeInicial]) {
            println("No se permiten arcos repetidos")
            return
        }

        adyacencias[verticeInicial].add(verticeFinal)
    }

    /**
     * Convierte la lista de adyacencias a una cadena de texto.
     *
     * @return Representación en cadena de la lista de adyacencias.
     */
    override fun toString(): String {
        return adyacencias.toString()
    }

    /**
     * Clase interna abstracta para representar una búsqueda en el grafo.
     */
    inner abstract class Busqueda {
        /**
         * Busca la cantidad de vértices desde el vértice D hasta el vértice H.
         *
         * @param D Vértice inicial.
         * @param H Vértice final.
         * @return Cantidad de vértices en el camino o -1 si no hay camino.
         */
        abstract fun buscar(D: Int, H: Int): Int
    }

    /**
     * Clase interna que implementa el algoritmo BFS para la búsqueda en grafos.
     */
    inner class BFS : Grafo.Busqueda() {
        override fun buscar(D: Int, H: Int): Int {
            if (D !in 0 until size || H !in 0 until size) {
                throw RuntimeException("${D} o ${H} no pertenecen al grafo")
            }

            // Inicializar listas para propiedades
            var distanciaHasta = MutableList(size) { -1 }
            var verticeYaExplorado = MutableList(size) { false }

            // Inicializar vértice raíz
            distanciaHasta[D] = 0
            verticeYaExplorado[D] = true

            // Inicializar cola (usando una lista mutable como cola)
            var cola: MutableList<Int> = mutableListOf()
            cola.add(D)

            // BFS
            while (cola.isNotEmpty()) {
                var actual = cola.removeAt(0)

                for (vertice in adyacencias[actual]) {
                    if (!verticeYaExplorado[vertice]) {
                        distanciaHasta[vertice] = distanciaHasta[actual] + 1
                        cola.add(vertice)
                    }
                }
                verticeYaExplorado[actual] = true
            }

            return distanciaHasta[H]
        }
    }

    /**
     * Clase interna que implementa el algoritmo DFS para la búsqueda en grafos.
     */
    inner class DFS : Grafo.Busqueda() {
        // Variables necesarias para DFS
        var tiempo = 0
        var predecesorDe = MutableList(size) { -1 }
        var verticeYaExplorado = MutableList(size) { false }
        var tiempoInicialDe = MutableList(size) { -1 }
        var tiempoFinalDe = MutableList(size) { -1 }

        override fun buscar(D: Int, H: Int): Int {
            if (D !in 0 until size || H !in 0 until size) {
                throw RuntimeException("${D} o ${H} no pertenecen al grafo")
            }

            // Ejecutar DFS con D como raíz.
            dfsVisit(D)

            var verticesExplorados = -1
            if (tiempoInicialDe[D] < tiempoInicialDe[H] && tiempoFinalDe[D] > tiempoFinalDe[H]) {
                verticesExplorados = calcularCantidadDeVerticesDesdeHasta(D, H)
            }

            // Reiniciar variables de la clase a su estado inicial
            reiniciarVariables()
            return verticesExplorados
        }

        /**
         * Realiza una visita DFS del grafo.
         *
         * @param verticeInicial Vértice inicial para la visita DFS.
         */
        fun dfsVisit(verticeInicial: Int) {
            tiempo += 1
            verticeYaExplorado[verticeInicial] = true
            tiempoInicialDe[verticeInicial] = tiempo

            for (verticeFinal in adyacencias[verticeInicial]) {
                if (!verticeYaExplorado[verticeFinal]) {
                    predecesorDe[verticeFinal] = verticeInicial
                    dfsVisit(verticeFinal)
                }
            }
            tiempo += 1
            tiempoFinalDe[verticeInicial] = tiempo
        }

        /**
         * Calcula la cantidad de vértices en el camino desde el vértice D hasta el vértice H.
         *
         * @param D Vértice inicial.
         * @param H Vértice final.
         * @return Cantidad de vértices en el camino.
         */
        fun calcularCantidadDeVerticesDesdeHasta(D: Int, H: Int): Int {
            var actual = H
            var contador = 0
            while (actual != D) {
                actual = predecesorDe[actual]
                contador += 1
            }
            return contador
        }

        /**
         * Reinicia las variables de la clase a su estado inicial.
         */
        fun reiniciarVariables() {
            tiempo = 0
            predecesorDe = MutableList(size) { -1 }
            verticeYaExplorado = MutableList(size) { false }
            tiempoInicialDe = MutableList(size) { -1 }
            tiempoFinalDe = MutableList(size) { -1 }
        }
    }
}
