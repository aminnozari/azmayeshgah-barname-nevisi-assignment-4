
import random
import time
start = 0
end = 0
bazi = [["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]         
        ] 
def printbazi():
      for i in range(3):
            for j in range(3):
                print (bazi[i][j] , end=" ")   
            print()            
def print_natije(karbar):
       print(karbar ,"barande ast...")
       end = time.time()
       zaman = end - start
       print ("zaman tey shode dar bazi : " , zaman , "sanye")
def check_bazi(karbar):
    c = 0
    for i in range(3):
        for j in range(3):
         if   bazi[i][j] != "-" :
            c = c + 1;     
    if    (bazi[0][0] == "🔴" and bazi[0][1] == "🔴" and bazi[0][2] == "🔴" ) :
       print_natije("karbar1")
       return False   
    elif  (bazi[0][0] == "🔵" and bazi[0][1] == "🔵" and bazi[0][2] == "🔵" ) :  
       print_natije(karbar)
       return False   
    elif  (bazi[1][0] == "🔴" and bazi[1][1] == "🔴" and bazi[1][2] == "🔴" ) :
       print_natije("karbar1")
       return False   
    elif  (bazi[1][0] == "🔵" and bazi[1][1] == "🔵" and bazi[1][2] == "🔵" ) :  
       print_natije(karbar)
       return False   
    elif  (bazi[2][0] == "🔴" and bazi[2][1] == "🔴" and bazi[2][2] == "🔴" ) :
       print_natije("karbar1")
       return False      
    elif  (bazi[2][0] == "🔵" and bazi[2][1] == "🔵" and bazi[2][2] == "🔵" ) :  
       print_natije(karbar)
       return False    
    elif  (bazi[0][0] == "🔴" and bazi[1][0] == "🔴" and bazi[2][0] == "🔴" ) :
            print_natije("karbar1")
            return False    
    elif  (bazi[0][0] == "🔵" and bazi[1][0] == "🔵" and bazi[2][0] == "🔵" ) :  
       print_natije(karbar)
       return False   
    elif  (bazi[0][1] == "🔴" and bazi[1][1] == "🔴" and bazi[2][1] == "🔴" ) :
       print_natije("karbar1")
       return False   
    elif  (bazi[0][1] == "🔵" and bazi[1][1] == "🔵" and bazi[2][1] == "🔵" ) :  
       print_natije(karbar)
       return False   
    elif  (bazi[0][2] == "🔴" and bazi[1][2] == "🔴" and bazi[2][2] == "🔴" ) :
           print_natije("karbar1")           
           return False      
    elif  (bazi[0][2] == "🔵" and bazi[1][2] == "🔵" and bazi[2][2] == "🔵" ) :  
       print_natije(karbar)
       return False   
    elif  (bazi[0][2] == "🔴" and bazi[1][1] == "🔴" and bazi[2][0] == "🔴" ) :
            print_natije("karbar1") 
            return False     
    elif  (bazi[0][2] == "🔵" and bazi[1][1] == "🔵" and bazi[2][0] == "🔵" ) :  
       print_natije(karbar)
       return False    
    elif  (bazi[0][0] == "🔴" and bazi[1][1] == "🔴" and bazi[2][2] == "🔴" ) :
            print_natije("karbar1")           
            return False     
    elif  (bazi[0][0] == "🔵" and bazi[1][1] == "🔵" and bazi[2][2] == "🔵" ) :  
       print_natije(karbar)
       return False    
    elif c == 9 :
        return False   
    else :
        return True                                    
def init_pc_choose():
    while check_bazi("pc") :
     random_pc_row = random.randint(0,2)
     random_pc_col = random.randint(0,2)

     if bazi[random_pc_row][random_pc_col] == "-":
         bazi[random_pc_row][random_pc_col] = "🔵"
         break    
def playwithpc():
    while check_bazi("pc"):
        while True :
            print("shoma ba mohre 🔴 bazi mikonid . ")
            karbar_row = int(input ("satr mored nazar khod ra vared konid :"))
            karbar_col = int(input ("sotoon mored nazar khod ra vared konid :"))
            if bazi[karbar_row-1][karbar_col-1] == "-":
                bazi[karbar_row-1][karbar_col-1] = "🔴"
                init_pc_choose()
                printbazi()
                break
            else :
                print("khane digari ra entekhab konid in khane por ast !")
                printbazi()
def twoplayers():   
    while True:
        finish = 0
        while True :
            print("shoma ba mohre 🔴 bazi mikonid . ")
            karbar_row = int(input ("satr mored nazar khod ra vared konid :"))
            karbar_col = int(input ("sotoon mored nazar khod ra vared konid :"))
            if bazi[karbar_row-1][karbar_col-1] == "-":
                bazi[karbar_row-1][karbar_col-1] = "🔴"
                printbazi()
                if check_bazi("karbar2") == False :
                    finish = "finish"
                break
            else :
                print("khane digari ra entekhab konid in khane por ast !")
                printbazi()
        if finish == "finish":
             break    
        while True :   
            print("shoma ba mohre 🔵 bazi mikonid . ")
            karbar_row = int(input ("satr mored nazar khod ra vared konid :"))
            karbar_col = int(input ("sotoon mored nazar khod ra vared konid :"))
            if bazi[karbar_row-1][karbar_col-1] == "-":
                bazi[karbar_row-1][karbar_col-1] = "🔵"
                printbazi()
                if check_bazi("karbar2") == False :
                    finish = "finish"
                break
            else :
                print("khane digari ra entekhab konid in khane por ast !")
                printbazi()   
        if finish == "finish":
         break              
menu_gozine = {
    1: "user & pc",
    2: "user1 & user2",
    3: "Exit",
}
def print_menu():
    for key in menu_gozine.keys():
        print (key, ")", menu_gozine[key] )
if __name__=="__main__":
    while(True):
        print_menu()
        gozine = ""
        try:
            gozine = int(input("entekhab shoma chist ?"))
        except:
            print("✖")
        if gozine == 1:
           bazi = [["-","-","-"],
                    ["-","-","-"],
                    ["-","-","-"]         
                    ]
           start = time.time()
           playwithpc()
        elif gozine == 2:
            bazi = [["-","-","-"],
                    ["-","-","-"],
                    ["-","-","-"]         
                    ]
            twoplayers()
        elif gozine == 3:
            exit()
        else:
            print("✖")