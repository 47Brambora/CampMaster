import os
import sys


DATA_DIR = "data"
logo = r'''
  ______                                     __       __                        __                         
 /      \                                   |  \     /  \                      |  \                        
|  ######\  ______   ______ ____    ______  | ##\   /  ##  ______    _______  _| ##_     ______    ______  
| ##   \## |      \ |      \    \  /      \ | ###\ /  ### |      \  /       \|   ## \   /      \  /      \ 
| ##        \######\| ######\####\|  ######\| ####\  ####  \######\|  ####### \######  |  ######\|  ######\
| ##   __  /      ##| ## | ## | ##| ##  | ##| ##\## ## ## /      ## \##    \   | ## __ | ##    ##| ##   \##
| ##__/  \|  #######| ## | ## | ##| ##__/ ##| ## \###| ##|  ####### _\######\  | ##|  \| ########| ##      
 \##    ## \##    ##| ## | ## | ##| ##    ##| ##  \# | ## \##    ##|       ##   \##  ## \##     \| ##      
  \######   \####### \##  \##  \##| #######  \##      \##  \####### \#######     \####   \####### \##      
                                  | ##                                                                     
                                  | ##                                                                     
                                   \##  
'''


def get_available_camps():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        return []
    
    return [f for f in os.listdir(DATA_DIR) if f.endswith(".db")]

def main_page():
    print(logo)

    camps = get_available_camps()
    if not camps:
        print("In directory data we didn't found any camp database. Please create one.")
        # TODO: Creating new database and opening that.
    else:
        print(f"We found these years: {camps}")
        # TODO: Open existing database (throu number 1,2,... or name camp_3027 or year 3027)


def main():
    main_page()


if __name__ == "__main__":
    main()
