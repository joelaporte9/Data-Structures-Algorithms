
def makeChange():

    # Input amount you would like chnage back for
    change  = float(input("Enter amount: "))

    # All values of coins, penny, nickel, dime and quarter
    coins = [1, 5, 10, 25]
    n = len(coins)
      
    # Reluts list, i.e the change you will get in return.
    changeResults = []
  
    # Loop through the change
    i = n - 1
    while(i >= 0):
          
        # Loop to get the correct amount of chnage needed for number inputed
        while (change >= coins[i]):
            change -= coins[i]
            changeResults.append(coins[i])
  
        i -= 1
  
    # Print result
    for i in range(len(changeResults)):
        print(changeResults[i], end = " ")
    
makeChange()


                

