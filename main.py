import databaseControl

if __name__ == '__main__':
    db = databaseControl.create_DB()
    playerFullName = ""
    while(True):
        playerFullName = input("Enter a player to search for or (quit) to exit: ")
        if(playerFullName == 'quit'):
            print("Program Quit! Have a nice day!")
            quit()
        else:
            playerArray = playerFullName.split(" ")
            player = databaseControl.search_player(playerArray[0], playerArray[1], db)
            print(player)
            print("\n")

