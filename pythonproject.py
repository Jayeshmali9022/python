
""" menu = {
    'Pizza':60,
    'pasta':120,
    'shahi panir':150,
    'maggie':50,
    'coffee':60,
}
print ("Well come to JAYESH KA DHABA ")
print("pizza: 60\npasta: 120\nshahi panir: 150\nmaggie: 50\ncoffe: 60")  


order_total=0
item_1=input("Enter the name of item you want to order : ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f" Ordered item {item_1} is not avaiable yet")

num=int(input("How many item you want order : "))

another_order =input("Do you want to add another item? (yes/no) ")
for i in range(1,num+1):
    if another_order=="yes":
       item_2=input("Enter the name of second item : ")
       if item_2 in menu :
          order_total += menu[item_2]
          print(f"Item {item_2} has been added to order ")
       else:
          print("NHI HAI BHAI PHIR KABHI AANA")  
print(f"The total amount of items to pay is {order_total} ")       """ 




#for loop se order



menu = {
    'PIZZA':60,
    'PASTA':120,
    'SHAHIPANIR':150,
    'MAGGIE':50,
    'COFFE':60,
}
print ("Well come to JAYESH KA DHABA ")
print("PIZZA: 60\nPASTA: 120\nSHAHIPANIR: 150\nMAGGIE: 50\nCOFFE: 60")  

num=int(input("How many item you want order : "))
order_total=0
for i in range(num):
   item=input("Enter the name of item you want to order : ")
   if item in menu:
      order_total += menu[item]
      print(f"Your item {item} has been added to your order")
   else:
      print(f" Ordered item {item} is not avaiable yet")
print(f"The total amount of items to pay is {order_total} ")






'''num=int(input("How many item you want order : "))

another_order =input("Do you want to add another item? (yes/no) ")
for i in range(1,num+1):
    if another_order=="yes":
       item_2=input("Enter the name of second item : ")
       if item_2 in menu :
          order_total += menu[item_2]
          print(f"Item {item_2} has been added to order ")
       else:
          print("NHI HAI BHAI PHIR KABHI AANA")  
print(f"The total amount of items to pay is {order_total} ") '''






