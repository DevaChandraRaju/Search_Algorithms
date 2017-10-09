# Search_Algorithms
List and Graph search algorithms



# Dijkstra's Algorithm - 
  - Let distance of start vertex from start vertex = 0
  - Let distance of all other vertices from start = infinity
  
  - WHILE vertices remain unvisited
          Visit unvisited vertex with smallest known diatnce from start vertex(call this 'current vertex')
          FOR each unvisited neighbour of the current vertex
              Calculate the distance from start vertex
              If the calculated distance of this vertex is less than the known distance
                  Update shortest diatnce to this vertex
                  Update the previous vertex with the current vertex
              end if
           NEXT unvisited neighbour
           Add the current vertext to the list of visited vertices
     END WHILE
