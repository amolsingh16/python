#Table

# n=int(input("enter number: "))
# i=1
# while i<=10:
#     print(n*i , end=" ")
#     i=i+1

#print 1 to 100

# i=1
# while i<=100:
#     print(i)
#     i=i+1

#check prime nummber

# n=int(input("enter a number: "))
# if(n%2==0):
#     print(n,"is prime")
# else:
#     print("not prime")

#factorial

# n=int(input("entere a number"))
# fact=1
# i=1
# while i<n+1:
#     fact=fact*i
#     i=i+1
# print(f"factorial of {n} is {fact}")

#fibonacci

# n=int(input("enter a number"))
# sum=0
# first = 0
# second = 1
# if n==0:
#     print("0")
# elif n==1:
#     print("1")
# else:
#     for i in range(n):
       
#         sum = first+second
#         first=second
#         second = sum
#     print(sum)

#reverse number

# n=1234
# r=0
# while n!=0:
#     a=n%10
#     r=r*10+a
#     n=n//10
# print("reverse number :",r)


#Count number

# n=1234
# count=0
# while n!=0:
#     n=n//10
#     count=count+1
# print("total",count)

# Create List

# my_list = [1,2,3]
# print(my_list)
# print(type(my_list))

# my_list2=[1,'amol','singh',True,3.14]
# print(my_list2)
# print(type(my_list2))


# my_list3=[1,2,[3,4],5]
# print(my_list3)
# print(type(my_list3))


#Access list - indexing

# list1=[10,20,30,40,50]
# print(list1[0])
# print(list1[-1])

#list slicing

#list_name[start:stop:step]

# list1=[10,20,30,40,50,60,70,80]

# #first three element
# print(list1[0:3])

# #second to fifth
# print(list1[1:6])

# #last three
# print(list1[-3:])

# #alternative
# print(list1[::2])

# #reverse
# print(list1[::-1])

#list modify

list=['apple','mango','grapes']
list[1]='banana'
print(list)
list.append('mango')
print(list)
list.remove('apple')
print(list)