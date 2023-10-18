/**
 * Universidad Simon Bolivar
 * Problema 1. Seccion b.ii:
 * Dada una matriz cuadrada A (cuya dimensión es N × N), calcular el producto
 * A × A' donde A' es A transpuesta.
 * 
 * @author Jose Perez, Carnet 16-10882
 */
public class MatrizProducto {

    public static void main(String[] args) {

        // Matriz de prueba. Se asume que la matriz ingresada es cuadrada
        int[][] A = { { 1, 2, 3 }, { 4, 2, 7 }, { 3, 2, 5 } };

        int[][] Atranspuesta = obtenerTranspuesta(A);
        int[][] resultado = multiplicarMatrices(A, Atranspuesta);

        System.out.println("Matriz de Prueba: ");
        imprimirMatriz(A);
        System.out.println("Transpuesta de la Matriz: ");
        imprimirMatriz(Atranspuesta);
        System.out.println("Resultado de Matriz*MatrizTranspuesta: ");
        imprimirMatriz(resultado);

    }

    /**
     * Funcion que calcula la multiplicacion de dos matrices
     * 
     * @param A Matriz de enteros a multiplicar
     * @param B Matriz de enterosa multiplicar
     * @return Matriz resultante de la multiplicacion
     */
    public static int[][] multiplicarMatrices(int[][] A, int[][] B) {
        int tamano = A.length;

        int resultado[][] = new int[tamano][tamano];

        for (int i = 0; i < tamano; i++) {
            for (int j = 0; j < tamano; j++) {
                resultado[i][j] = 0;
                for (int k = 0; k < tamano; k++) {
                    resultado[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        return resultado;
    }

    /**
     * Funcion que imprime una matriz
     * 
     * @param A Matriz de enteros a imprimir
     */
    public static void imprimirMatriz(int[][] A) {
        int tamano = A.length;
        for (int i = 0; i < tamano; i++) {
            for (int j = 0; j < tamano; j++) {
                System.out.print(A[i][j] + " ");
            }
            System.out.println();
        }
    }

    /**
     * Funcion que obtiene la transpuesta de una matriz
     * 
     * @param A Matriz de enteros
     * @return Matriz transpuesta de A
     */
    public static int[][] obtenerTranspuesta(int[][] A) {
        int tamano = A.length;
        int[][] transpuesta = new int[tamano][tamano];
        for (int i = 0; i < tamano; i++) {
            for (int j = 0; j < tamano; j++) {
                transpuesta[j][i] = A[i][j];
            }
        }
        return transpuesta;
    }
}