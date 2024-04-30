list= [4,2,7,9,12,3]
find_num = int(input())
found_num = False 
for each_num in list:
    if(each_num == find_num):
        found_num = True 
        break
    
if(found_num == True):
        print ("number in found ")
else:
    print("number in not found")

    