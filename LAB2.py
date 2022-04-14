import sys
def Incremental(arr):
	#O(n)
	#Om listan är mindre än 3 så är den för kort.
	if (len(arr) < 3):
		print("Listan är för kort!")
		return
	third = first = second = sys.maxsize #Värderna som sedan retuneras får högsta möjliga värde i början.
	#Denna kollar för varje element i listan:
	for i in range(0, len(arr)):
		#Om elementet är mindre än first så är den det minsta elementet:
		if (arr[i] < first):
			#då sätts tredje minsta till den andra minsta
			third = second
			#andra till första
			second = first 
			#och första till elemtet som var mindre.
			first = arr[i] 
		#samma princip gäller om det elementet är mindre än det andra eller det tredje.
		elif (arr[i] < second): 
			third = second 
			second = arr[i] 
		
		elif (arr[i] < third): 
			third = arr[i] 
	#Retunerar en trippel med ordningen (minst, näst minst, störst)
	return (first,second,third)


def divideAndConquer(lst, svararr):
	#O(n)
	#Om längden på listan är 1 så är den för kort.(Den är för kort om den är < 3 men de förstör våran algo)
	if len(lst) <= 1:
		print("Listan är för kort!")
		return
	else:
		#Typ base case.
		#Om listan är 3 eller 2 så kör kollar den alla element mot dom 3 i svararr och om en är mindre byt ut.
		#Följer samma princip som Incremental algo.
		if len(lst) <= 3:
			for i in range(0, len(lst)):
				if (lst[i] < svararr[0]):
					svararr[2] = svararr[1] 
					svararr[1] = svararr[0]
					svararr[0] = lst[i] 

				elif (lst[i] < svararr[1]): 

					svararr[2] = svararr[1]
					svararr[1] = lst[i] 

				elif (lst[i] < svararr[2]): 
					svararr[2] = lst[i] 
			
			return (svararr)
		#Annars så delar den upp listan i 2 sedan kallar rekusivt på denna funktion med dessa sub problems
		else:
			mid = len(lst) // 2 #Hittar mitten
			R = lst[mid:] #Höger sida av listan (sub problem 1)
			L = lst[:mid] #vänster sida av listan (sub problem 2)
			divideAndConquer(L,svararr)
			divideAndConquer(R,svararr)
		#Retunerar en tripple med ordningen (minst, nästminst, störst)
		return(svararr[0],svararr[1],svararr[2])
	

def divideAndConquer2(lst):
	# O(n*logn)
	if len(lst)==2: #Base case for even number of inputs
		return(lst[1] / lst[0])

	mid = len(lst)//2
	lPos = divideAndConquer2(lst[:mid])         #Each recursive step divides the given list into two steps, left and right side
	rPos = divideAndConquer2(lst[mid:])

	leftMin = min(lst[:mid])
	rightMax = max(lst[mid:])           #We want to find the highest value of the right side (nominator) divided by the left side (denominator) recursively.
	Maxkvot = max(lPos, rPos, rightMax / leftMin)
	return Maxkvot                      #continue until the base case is met ( 3 >= len(lst) >= 2 )

def divideAndConquer3(lst):
	#O(n)
	#Base cases för sub problems och orginal listan.
	if len(lst)==2:
		#returnerar kvoten, max talet, min talet
		return (lst[1] / lst[0], max(lst[0],lst[1]) , min(lst[0],lst[1]))


	#delar upp listan i sub problems
	middle = len(lst)//2
	#rekursivt kallar på funktionen med sub problems
	(lKvot,lMax, lMin) = divideAndConquer3(lst[:middle])
	(rKvot,rMax, rMin) = divideAndConquer3(lst[middle:])
	#Hittar den största kvoten

	maxKvot = max(rMax / lMin, lKvot, rKvot)
	Maximum = max(lMax, rMax)
	Minimum = min(lMin, rMin)
	return (maxKvot, Maximum , Minimum)

lst = [6,100,3,4,78,2,30,16,1]
lstPart2 = [6,100,3,4,78,2,30,16]
third = first = second = sys.maxsize
svararr = [first,second,third]
print(Incremental(lst))
print(divideAndConquer(lst,svararr))
print(divideAndConquer2(lstPart2))
print(divideAndConquer3(lstPart2)[0])
