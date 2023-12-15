def productoPunto(vector1, vector2)
    result = 0
    
    threads = []
  
    vector1.each_with_index do |element1, index|
      threads << Thread.new(element1, vector2[index]) do |e1, e2|
        producto = e1 * e2
        Thread.current[:resultado_parcial] = producto
      end
    end
  
    threads.each { |thread| thread.join; result += thread[:resultado_parcial] }
  
    result
  end
  
  # Ejemplo de uso:
  vector_a = [1, 2, 3, 4]
  vector_b = [5, 6, 7, 8]
  
  result = productoPunto(vector_a, vector_b)
  
  puts "El producto punto de los vectores es: #{result}"
  