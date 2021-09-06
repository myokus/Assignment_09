#------------------------------------------#
# Title: CDInventory.py
# Desc: Main module for CD Inventory
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# MYokus, 2021-Sep-03, Modified the File to add tracks functionality
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['CDInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory reloaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be cancelled.')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue # start loop back at top.
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Select the CD / Album index: ')
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        while True:
            IO.ScreenIO.print_CD_menu()
            strChoice2 = IO.ScreenIO.menu_CD_choice()
            if strChoice2 == 'x':
                break
            if strChoice2 == 'a':
                tplTrkInfo = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(tplTrkInfo, cd)
            elif strChoice2 == 'd':
                IO.ScreenIO.show_tracks(cd)
            elif strChoice2 == 'r':
                IO.ScreenIO.show_tracks(cd)
                trk_idx = int(input('Select the Track Index: '))
                cd.rmv_track(trk_idx)
            else:
                print('General Error')
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames  , lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue # start loop back at top.
    else:
        print('General Error')
