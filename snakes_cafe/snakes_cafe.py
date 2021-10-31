
def snakes_cafe():
    print("""
        **************************************
        **    Welcome to the Snakes Cafe!   **
        **    Please see our menu below.    **
        **
        ** To quit at any time, type "quit" **
        **************************************
        Appetizers
        ----------
        Wings
        Cookies
        Spring Rolls

        Entrees
        -------
        Salmon
        Steak
        Meat Tornado
        A Literal Garden

        Desserts
        --------
        Ice Cream
        Cake
        Pie

        Drinks
        ------
        Coffee
        Tea
        Unicorn Tears
        ***********************************
        ** What would you like to order? **
        ***********************************
    """)

    # options= {
    #     "Appetizers":[ "Wings","Cookies","Spring Rolls"],
    #     "Entrees":["Salmon","Steak","Meat Tornado","A Literal Garden"],
    #     "Desserts":["Ice Cream","Cake","Pie"],
    #     "Drinks":["Coffee","Tea","Unicorn Tears"]
    # }
    # answer= input("> ")
    # count= 1
    # # print(options)

    # while answer != "quit":
        
        # for x in options :
        #     # print(options[x])
        #     for y in range(0,len(options[x])):
        #         # print(y)
        #         if answer == options[x][y]:
        #             # print(options[x][y])
        #             # count=1
        #             count +=1
        #             print(f"{count} order of {answer} have been added to your meal ") 
                    
        # answer= input("> ")

           
    options= {
       "Wings":0,
       "Cookies":0,
       "Spring Rolls":0,
       "Salmon":0,
       "Steak":0,
       "Meat Tornado":0,
       "A Literal Garden":0,
       "Ice Cream":0,
       "Cake":0,
       "Pie":0,
        "Coffee":0,
        "Tea":0,
        "Unicorn Tears":0
    }
    answer= input("> ")
  

    while answer != "quit":
        if answer in options:
                options[answer] +=1
        else:
            print("please choose from menu")
        for x, y in options.items():
          
            if answer == x:
   
                print(f"{y} order of {answer} have been added to your meal ")

           
        answer= input("> ")

snakes_cafe()  
