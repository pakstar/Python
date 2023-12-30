my_list = ['ivan,','parvan','gosho','georg'] 

#list_len=len(my_list) 
#print(list_len)


my_list.append('jivko') #dobavq neshto kum lista
my_list.insert(0,'penka') #dobavq na opredeleno mqstp
print(my_list)



first_element=my_list[0]
 #vzemam nqkoi element
last_element = my_list[len(my_list) -1]


my_list[2] = 'svetlio'
print(my_list)






guest_list =  ['Ani','Niki','Pepi']
print("Guest list", guest_list)
print(guest_list[0],"I would like to invite you")
print(guest_list[1],"I would like to invite you")
print(guest_list[2],"I would like to invite you")


for x in guest_list:
    print( x + " I would like to invite you" )
    print( f"{x} +  I would like to invite you" )

for i in range(len(guest_list)):
    if(i % 2 == 0):
        print(f"{i+1}{guest_list[i]}, +  I would like to invite you 19" )
    else:
         print(f"{i+1}{guest_list[i]}, +  I would like to invite you 20" )



    