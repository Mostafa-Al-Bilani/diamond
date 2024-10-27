row = int(input("choose number of rows:"))
#top half of the diamond
for column in range(1, row + 1): #loop through each row including the chosne number 
        print(" " * (row - column), end = "") #print spaces for the current row
        print("*" * (2 * column - 1))# print stars for the current row
#bottom half of the diamond
for column in range(row -1, 0, -1): #loop backwards 
        print(" " * (row - column), end = "") #print spaces for the current row
        print("*" * (2 * column - 1)) # print stars for the current row
    
   
    