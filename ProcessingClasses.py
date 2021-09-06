#------------------------------------------#
# Title: ProcessingClasses.py
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# MYokus, 2021-Sep-03, Modified the File to add tracks functionality
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.


        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to the inventory.
            table (list of CD Objects): 2D data structure (list of CD Objects) that holds the data during runtime.

        Returns:
            None.

        """

        cdId, title, artist = CDInfo
        try:
            cdId = int(cdId)
        except:
            raise Exception ('ID must be an Integer!')
        row = DC.CD(cdId, title, artist)
        table.append(row)

    @staticmethod
    def select_cd(table: list, cd_number: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_number

        Args:
            table (list): Inventory list of CD objects.
            cd_number (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_number

        """

        try:
            cd_number = int(cd_number)
        except ValueError as e:
            print('ID is not an Integer!')
            print(e.__doc__)
        for row in table:
            if row.cd_id == cd_number:
                return row
            else:
                raise Exception('This CD / Album index does not exist')

    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd


        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the tarck gets added to.

        Raises:
            Exception: Raised in case position is not an integer.

        Returns:
            None.

        """

        trkPos, trkTitle, trkLength = track_info
        try:
            trkPos = int(trkPos)
        except:
            raise Exception('Position must be an Integer')
        track = DC.Track(trkPos, trkTitle, trkLength)
        cd.add_track(track)
