/**
 * Universidad Simon Bolivar
 * Problema 1. Seccion b.i:
 * Dada una cadena de caracteres w y un entero no–negativo k, calcular
 * la rotación de k posiciones de la cadena w.
 * 
 * @author Jose Perez, Carnet 16-10882
 */
public class Rotacion {
    public static void main(String[] args) throws Exception {
        String palabra = "hola"; // Palabra a rotar
        int rotacion = 5; // Rotaciones
        int tamano = palabra.length();

        // Precondicion
        if (rotacion < 0) {
            throw new Error("No se permiten rotaciones negativas");
        }

        System.out.println("Palabra a rotar: " + palabra);
        System.out.println("Rotaciones a realizar: " + rotacion);

        // Recalcular para solo hacer las rotaciones necesarias
        if (rotacion >= tamano) {
            rotacion = rotacion % tamano;
        }

        // Imprimir palabra con las rotaciones aplicadas
        System.out.println(rotar(palabra, tamano, rotacion));
    }

    /**
     * Implementacion recursiva de la funcion que calcula la rotacion de una palabra
     * dada
     * 
     * @param palabra  String que es la palabra a rotar
     * @param tamano   int no negativo que es el tamano de la palabra
     * @param rotacion int no negativo que es la cantidad de rotaciones a realizar
     * @return Un string que es la palabra con las rotaciones efectuadas
     */
    public static String rotar(String palabra, int tamano, int rotacion) {

        if (tamano == 0 || rotacion <= 0) {
            return palabra;
        }

        palabra = palabra.substring(1, tamano) + palabra.charAt(0);

        return rotar(palabra, tamano, rotacion - 1);
    }

}
