#list comprehensions
##even=[i*2 for i in range(10)]
##print(even)
##
##movies = [
##    "Star Wars",
##    "Gandhi",
##    "Casablanca",
##    "Shawshank Redemption",
##    "Toy Story",
##    "Ghostbusters",
##    "To Kill A Mockingbird",
##    "Good Will Hunting",
##    "2001: A Space Odyssey",
##    "Raiders of the Lost Ark",
##    "Groundhog Day",
##    "Close Encounters of the Third Kind"
##]
##smovies=[sms for sms in movies if sms.startswith("S")]
##print(smovies)
##gmovies=[gm for gm in movies if gm.startswith("G")]
##print(gmovies)
##a = [
##    "Beyond", 
##    "the", 
##    "mountains", 
##    "the", 
##    "sun", 
##    "sets", 
##    "quietly", 
##    "casting", 
##    "golden", 
##    "hues", 
##    "across", 
##    "the", 
##    "tranquil", 
##    "river", 
##    "reflecting", 
##    "endless", 
##    "dreams"
##]
##_4words=[words for words in a if len(words)<=4 and words.startwith("t")]
##print(_4words)

##x = int(input())
##y = int(input())
##z = int(input())
##n = int(input())
##coordinates=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
##print(coordinates)


##n=int(input("Enter the number of participants:"))
##scores=list(map(int,input().split()))
##max_score=max(scores)
##altered_code=[score for score in scores if score !=max_score]
##runner=max(altered_code)
##print("the runner is "+str(runner))
##num_inputs = int(input("How many values do you want to enter? "))
##
### Collect user inputs and create a list using list comprehension
##user_inputs = [int(input(f"Enter value {i+1}: ")) for i in range(num_inputs)]
##
##print(user_inputs)
##NoOfElements=int(input("Enter how much elements you need to enter?"))
##Elements=[int(input()) for _ in range(NoOfElements)]
##print("Entered elements\n",Elements)
##EvenElements=[i for i in Elements if i%2==0]
##print("Even elements\n",EvenElements
##e=int(input("how much elements"))
##list1=[int(input()) for _ in range(e)]
##print(list1)
##list2=[i**2 for i in list1]
##print(list2)

##student=[]
##for _ in range(int(input())):
##    name=input()
##    score=float(input())
##    student.append([name,score])
##print(student)
L1=[[1,2],[3,4],[5,6]]
l2=[i for i in L1 ]
print(L1)
print(l2)




















































