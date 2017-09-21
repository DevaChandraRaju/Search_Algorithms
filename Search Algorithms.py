# -*- coding: utf-8 -*-
"""
@author: Deva Chandra Raju Malla

List Search Algorithms
1) Binary Search
2) Linear/Sequential search

Graph Search Algorithms
1) Breadth-First-Search - http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
2) Depth First Search - http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
3) Dijkstra's Algorithm
4) A* Algorithm
5) brute-force search
    Brute-force search should proceed in a systematic way by exploring nodes in some predetermined order or simply by selecting nodes at random. Search programs either return only a solution value when a goal is found or record and return the solution path. The most important brute-force techniques are as below.


Refer http://bigocheatsheet.com/ for BIGO notation and cheat sheet
"""

def binary_search(item_list,item):
    ## List should be in sorted order
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
	
    
def Sequential_Search(dlist, item):
    ## Search list can be in any order
    pos = 0
    found = False
    
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    
    return found, pos


def DFS_dist_from_node(query_node, parents):
    """Return dictionary containing distances of parent GO nodes from the query"""
    ## Uses LIFO
    result = {}
    stack = []
    stack.append( (query_node, 0) )
    while len(stack) > 0:
        print("stack=", stack)
        node, dist = stack.pop()
        result[node] = dist
        if node in parents:
            for parent in parents[node]:
                # Get the first member of each tuple, see 
                # http://stackoverflow.com/questions/12142133/how-to-get-first-element-in-a-list-of-tuples
                stack_members = [x[0] for x in stack]
                if parent not in stack_members:
                    stack.append( (parent, dist+1) )
    return result
    
def BFS_dist_from_node(query_node, parents):
    """Return dictionary containing minimum distances of parent GO nodes from the query"""
    ## Uses FIFO
    result = {}
    queue = []
    queue.append( (query_node, 0) )
    while queue:
        print("queue=", queue)
        node, dist = queue.pop(0)
        result[node] = dist
        if node in parents: # If the node *has* parents
            for parent in parents[node]:
                # Get the first member of each tuple, see 
                # http://stackoverflow.com/questions/12142133/how-to-get-first-element-in-a-list-of-tuples
                queue_members = [x[0] for x in queue]
                if parent not in result and parent not in queue_members: # Don't visit a second time
                    queue.append( (parent, dist+1) )
    return result


if __name__ == "__main__":
    

    print("Search Algorithms")
    print(binary_search([1,2,3,5,8], 6))
    print(binary_search([1,2,3,5,8], 5))
    print(binary_search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3))
    print(binary_search([0, 1, 3, 8, 14, 18, 19, 34, 52], 17))


    print("Graph Search Algorithms")
    parents = dict()
    parents = {'N1': ['N2', 'N3', 'N4'], 'N3': ['N6', 'N7'], 'N4': ['N3'], 'N5': ['N4', 'N8'], 'N6': ['N13'],
               'N8': ['N9'], 'N9': ['N11'], 'N10': ['N7', 'N9'], 'N11': ['N14'], 'N12': ['N5']}

    print("Depth-first search:")
    dist = DFS_dist_from_node('N1', parents)
    print(dist)
    
    print("Breadth-first search:")
    dist = BFS_dist_from_node('N1', parents)
    print(dist)
    

    