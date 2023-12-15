def explorar(path, hilo_actual)
    puts "Inicio -->    Hilo: #{hilo_actual}    Directorio: /#{path}"
  
    # Lista de subrutas
    path_list = Dir.entries(path).select { |dir| dir != "." && dir != ".." }
    countFiles = 0

    # Lista para almacenar los hilos creados en esta ruta
    hilos = []
  
    # Obtener los subdirectorios del path
    path_list.each do |elem|
      sub = File.join(path, elem)
      if File.directory?(sub)
        # Variable global para contar los hilos creados en total
        $countThreads +=  1
        contador = $countThreads
        # Crear un hilo por cada subdirectorio encontrado
        hilo_nuevo = Thread.new { explorar(sub, contador) }
        hilos << hilo_nuevo
      elsif File.file?(sub)
        countFiles += 1
      end
    end
  
    puts "Fin    <--    Hilo: #{hilo_actual}    Directorio: /#{path} tiene #{countFiles} ficheros"

    # Esperar a que todos los hilos hayan terminado
    hilos.each(&:join)
  
  end
  
  def main
    # path de ejemplo 'path'
    path = 'path'
    $countThreads = 0
    Thread.new { explorar(path, $countThreads) }.join
  end
  
  main
  