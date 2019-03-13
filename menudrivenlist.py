L=[]
even=[]
odd=[]
mergedlist=[]
n=int(input("Enter the no of elements you want in the list:\n"))
for i in range(n):
	a=int(input("Enter the element into the list:"))
	L.append(a)
choice=0
while(choice!=6):
	choice=int(input("\nMENU:\n1.Put Even and odd elements in two different lists\n2.Merge and sort the two lists\n3.Update the first element with any new value and delete the middle element of the list of both lists\n4.Find max and min elements from both lists\n5.Add n numbers in the list and check if 'python' is present\n6.EXIT\nEnter your choice:"))
	if(choice==1):
		for i in L:	
			if(i%2==0):
				even.append(i)
			else:
				odd.append(i)
		print("even=",even)
		print("odd=",odd)
	
	elif(choice==2):
		mergedlist=even+odd
		mergedlist.sort()
		print(mergedlist)

	elif(choice==3):
		even[0]=int(input("\nEnter a new value for 1st position of 1st list:\n"))
		odd[0]=int(input("\nEnter a new value for 1st position of 2nd list:\n"))
		even.pop(len(even)//2)
		odd.pop(len(odd)//2)
		print("even=",even)
		print("odd=",odd)
		
	elif(choice==4):
		print("The max value from list 'even' is: ",max(even))
		print("The min value from list 'even' is: ",min(even))
		print("The max value from list 'odd' is: ",max(odd))
		print("The min value from list 'odd' is: ",min(odd))
		
	elif(choice==5):
		no=int(input("\nEnter the no of names you want to enter in the original list:\n"))
		for i in range(no):
			name=input("Enter the name to insert in the list:")
			L.append(name)
		if 'python' in L:
			print("\nThe name 'python' is present in the list\n")
		else:	
			print("\nThe name 'python' is not present in the list\n")