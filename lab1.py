import random
from collections import defaultdict
import heapq

class Graph():
    '''
    This class creates, stores and prints a Graph.
    '''
    def __init__(self, nodes):
        '''
        Initialization section of class, here results are stored and are used when output is requested.
        '''
        self.nodes = nodes
        self.choice = self.nodes[:]
        self.edges = []
        self.adjlist = []
        self.adjdict = defaultdict(list)
        v= len(self.nodes)
        self.matrix = [[0]*v for i in range(v)]

        self.MstAdjGraph = []



    def addEdge(self,node, u, w):
        '''
        A small function that manually adds an edge in the list for edges. ["node", "conencted to", "weight"]
        '''
        check = True
        for edges in self.edges:
            if node == u:
                check = False
                print("Cant connect node to itself")
                break
            if edges[0:2] == [node, u] or edges[0:2] == [u, node]:
                print("Connection already exists, cant add edge")
                check = False
                break
        if check == True:
            self.edges.append([node, u, w])

    def addRandomEdge(self):
        '''
        A function that connects nodes randomly, starting from the first node, removing it from a list of not yet visited
        nodes, and then connecting it to one of the remaining nodes that are not yet connected.
        This will be weighted towards the last items in the list due to probability, but this does not
        negatively impact the result since the task is only to generate a connected graph based on the nodes,
        which this algorithm accomplishes. It then assigns random weights to these generated edges.
        '''
        for node in self.nodes:
            if node < len(self.nodes):
                self.choice.remove(node)
                randomNode = random.sample(self.choice, 1)
                randomNode.append(node)
                randomNode.append(random.randint(1,9))
                self.edges.append(randomNode)

    def calculateList(self):
        '''
        A function that calculates an adjacency list based on the edges generated in AddRandomEdge, along with calculating the matrix.
        '''
        for node in self.nodes:
            self.adjlist.append(node)                       #add the node as integer to list
            tempList2 = []
            for edges in self.edges:
                for connection in range(len(edges)-1):
                    if node == edges[connection]:           #loop through each item in 2-d list, if there is a connection:
                        tempList = edges[:]                 #copy the edges[connection] item, remove the node element node from it
                        tempList.remove(node)               #then append it to tempList2
                        tempList2.append(tempList[:])
                        if node-1 != edges[1]-1:                            #extra statement needed for matrix
                            self.matrix[edges[1]-1][node-1] = edges[2]      #store values in self.matrix
                            self.matrix[node-1][edges[1]-1] = edges[2]
                            self.adjdict[node].append(tempList)
                            self.adjdict[tempList[0]].append([node, tempList[1]])
            self.adjlist.append(tempList2)                  #final tempList2 added to self.adjlist and then reset for each node
            tempList2 = []

    def adjacencyList(self):
        '''
        Print function for adjacency List.
        '''
        for item in self.adjlist:
            if isinstance(item, list):
                for lists in item:
                    print(" --> ", "[" + str(lists[0]) + "]", " (weight: " + str(lists[1]) + " )")
            else:
                print("Node", "["+ str(item) +"]:")

    def PrimAdjlist(self):
        W = 999
        Kant = []
        Svar = []								#Kollar så vi har rätt antal connections valda
        node = [7]                              #starting node
        Sindex = self.adjlist.index(node[0])
        AllE = [self.adjlist[Sindex]]			#Lägger till startnoden
        AllE = AllE + self.adjlist[Sindex+1]	#och dess connections till alla edges att välja mellan
        Koll = []								#lista som håller om vi kan ta den edgen beroende på om vi har varit på den noden den vill gå till
        nodePrev = 0
        currNode = 0
        currNodeFinal = 0
        stAdjGraph = []						#Listan funktionen retunerar
        itCount =  0
        while len(Svar) < len(self.nodes) -1:											#O(n-1) * O(n-1) = O
            for edges in AllE:
                for iteration, item in enumerate(AllE):
                    print("iteration:" , iteration)
                itCount = itCount + 1
                print("TOTAL:" , itCount)													#O(v) v = antal edges för den aktiva noden + de edges som inte blev valda i de förra varven (Worst case antagligen )
                if isinstance(edges, int):												#Om "Edgen" som kommer är en int så vet vi vilken nod de nästkommande edges tillhör
                    currNode = edges
                else:
                    if edges[1] < W and edges[0] not in Koll:							#Om vi hittar en väg som är billigast och inte har tagits för:
                        currNodeFinal = currNode										#sätt currNodeFinal till den senaste noden hittad så vi vet var vi kom ifrån
                        W = edges[1]														#Sätter weight till weighten av den nya edgen
                        Kant = edges 														#Sätter Kant till den edgen vi hitta
                    if AllE.count(edges) >= 2:											#Om det finns 2 eller fler av samma edge så tar vi bort så det finns en
                        AllE.remove(edges)
            AllE.remove(Kant)
            MstAdjGraph = MstAdjGraph + [[Kant[1], currNodeFinal, Kant[0]]]             #[weight, node, to]
            Svar = Svar + [Kant]
            nodePrev = node
            node = [Kant[0]]
            W = 999																		#Resetar Weight
            index = self.adjlist.index(node[0])											#Hittar index av nästa nod och hittar den edges
            AllE.append(self.adjlist[index])
            AllE = AllE + self.adjlist[index+1]
            Koll = Koll + node + nodePrev

        return(MstAdjGraph)																#Retunerar svaret

    def prim_Adj_matrix(self):
        INF = 9999999
        resultList=[]
        # number of vertices
        V = len(self.nodes)
        # 2d array and size 5x5
        # Bring the information from self.matrix
        G = self.matrix
        # track that which element selected
        # the selected element set to True

        selected = [0] * len(self.nodes)
        # number of edges
        no_edge = 0
        """ e = V - 1
            e is number of edge
            v = number vertices
            and then we choose a randomly element
        """
        selected[6] = True                #starting node wanted -1 = selected


        # print for edge and weight
        while (no_edge < V - 1):

            """ 
                * For every V in the set selected, find the all adjacent vertices
                * choose the edges who cost smallest
                * check if the V is already selected or not, if already selected discord it, otherwise
                * choose the edges who cost smallest
            """
            minimum = INF
            x = 0
            y = 0

            for i in range(V):
                if selected[i]:
                    for j in range(V):
                        if ((not selected[j]) and G[i][j]):
                            # not in selected and there is an edge
                            if minimum > G[i][j]:
                                minimum = G[i][j]
                                x = i
                                y = j
            #[weight,  node, to]
            resultList=resultList+[[G[x][y], x+1, y+1]]

            selected[y] = True
            no_edge += 1
        return resultList

    def adjacencyMatrix(self):
        '''
        Print function for adjacency Matrix.
        '''
        r = len(self.nodes)
        c =len(self.nodes)
        for i in range(r):
            for j in range(c):
                print(self.matrix[i][j], end=" ")
            print("")

    def PrimsAlgorithmAdj(self):
        #https://bradfieldcs.com/algos/graphs/prims-spanning-tree-algorithm/    ||MODIFIED THIS


        mst = []                                                            #result list
        visited = []                                                        #visited nodes
        curNode = 7                                                         #starting node
        possibleEdges = []                                                  #the possible edges left in any given iteration of while-loop
        for item in self.adjdict[curNode]:                                  # O(N)
            possibleEdges.append([item[1], curNode, item[0]])               #possible edges += [cost, node, to]
        heapq.heapify(possibleEdges)                                        #generates min-heap (binary tree) from given list of possible edges based on cost ||| O(log N)

        while possibleEdges and len(mst) < (len(self.nodes) -1):            #item[0] = to next, item[1] = cost
            cost,frm,to = heapq.heappop(possibleEdges)                      #pops the root of heap (smallest cost since min-heap)
            if to not in visited:                                           #not create cycle
                visited.extend([to, frm])                                   #both nodes of edges are put into visited list
                mst.append([cost, frm, to])                                 #add the connection to MST result list
                for item in self.adjdict[to]:                               # O(N-1), for each new possible connection for the new node:
                    if item[0] not in visited:
                        heapq.heappush(possibleEdges, [item[1], to, item[0]])   # The heappush() method pushes new possible edges into the
                                                                                # existing heap in such a way that the heap property is maintained.
        return mst

    def PrimsAlgorithmMatrix(self):
        #https://bradfieldcs.com/algos/graphs/prims-spanning-tree-algorithm/    ||MODIFIED THIS
        mst = []
        visited = []
        curNode = 7
        possibleEdges = []              #heap used for calculating MST
        r = len(self.nodes)
        c =len(self.nodes)
        for i in range(r):
            for j in range(c):                                              # O(n^2)
                if self.matrix[i][j] > 0 and j+1 == curNode:
                    possibleEdges.append([self.matrix[i][j], curNode, i+1])
        heapq.heapify(possibleEdges)                                        # O(log N)

        while possibleEdges and len(mst) < (len(self.nodes) -1):            #item[0] = to next, item[1] = cost        time: (n-1)
            #print(possibleEdges)   #display current heap for iteration
            cost,frm,to = heapq.heappop(possibleEdges)                      # O(log N) pop, O(log N) push
            if to not in visited:
                visited.extend([to, frm])
                mst.append([cost, frm, to])
                for item in self.adjdict[to]:                               # O(N * N-1) = O(N ^ 2)
                    if item[0] not in visited:
                        heapq.heappush(possibleEdges, [item[1], to, item[0]])   # The heappush() method pushes an element into an
                                                                                # existing heap in such a way that the heap property is maintained.
        return mst                      #returns the MST generated
'''
Time complexity:
O(N^2) since there are two nested for-loops to retrieve values for all edges+weights in 2d array

Total for outer statement: O(n^2) * O(log N) = O(n^2 * log N)
Total for while loop: O(n-1) * 2 * O(log n) * O(N) = O(n-1 * n * 2 * log n)
= O(n^2 * log n)
'''
def main():
    nodes = [1,2,3,4,5, 6, 7, 8, 9, 10]                             #Assign number of nodes, [0 to N]. USE INTEGERS > 0.
    graph = Graph(nodes)                                            #Create Graph object
    graph.addRandomEdge()
    graph.addEdge(4,2,5)
    graph.addEdge(5,1,2)
    graph.addEdge(2,1,1)
    graph.addEdge(4,3,6)
    graph.addEdge(1,3,9)

    print("Edges: (node, node connected to, weight)")
    for edges in graph.edges:
        print(edges)
    graph.calculateList()
    print("Adjacency List:")
    graph.adjacencyList()
    print("Matrix: ")
    graph.adjacencyMatrix()

    print("MST | AdjMatrix Prim's")
    print(graph.prim_Adj_matrix())
    print("MST | AdjList Prim's")
    print(graph.PrimAdjlist())
    print("MST | Prim's AdjList Heap")
    print(graph.PrimsAlgorithmAdj())
    print("MST | Prim's Matrix Heap")
    print(graph.PrimsAlgorithmMatrix())
main()
