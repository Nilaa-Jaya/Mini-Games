print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You are in a cross road. Where do you want to go? Type "left" or "right"  ')
if choice1 == "right":
    print("There was a big pit, you fell. GAME OVER!!!")

elif choice1 == "left":
    print(
        'You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim"to swim across.')
    choice2 = input()
    if choice2 == "swim":
        print("You get attacked by an angry shark. Game over!!!")
        print('''       
                                 ,-
                               ,'::|
                              /::::|
                            ,'::::o|                                      _..
         ____........-------,..::?88b                                  ,-' /
 _.--"""".^. . .      .   .  .  .  ""`-._                           ,-' .;'
<. - :::::O......  ...   . . .. . .  .  .""--._                  ,-'. .;'
 `-._  ` `":`:`:`::||||:::::::::::::::::.:. .  ""--._ ,'|     ,-'.  .;'
     """_=--       //'doo.. ````:`:`::::::::::.:.:.:. .`-`._-'.   .;'
         ""--.__     P(                       ` ``:`:``:::: .   .;'
                "| ""--.:-.     `.                             .:/
                  |. /    `-._   `.""-----.,-..::(--""./ ""`.  `:
                   `P         `-._ /          `-:/          `. `:
                                   ""            "            `-._) 
    ''')

    elif choice2 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. "
              "Which colour do you choose?  ")
        choice3 = input()
        if choice3 == "red":
            print("Its a room full of fire. GAME OVER!!!")
            print('''
               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^''')

        elif choice3 == "blue":
            print("You enter a room full of beasts. GAME OVER!!!")
            print('''  
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \ \    ( '        )(    )
      \   \ \   \.  _.__ ____( .  |
       \  /\ \  .(   .'  /\  '.  )
        \(  \ \.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\ \ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
                 _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"

''')


        elif choice3 == "yellow":
            print("You found the treasure!!! YOU WON!!! CONGRATULATIONS ")
            print('''     

                               .--------.
                             .: : :  :___`.
                           .'!!:::::  \ \_\`.
                      : . /%O!!::::::::\ \_\_\.
                     [""]/%%O!!:::::::::::::  \.
                     |  |%%OO!!::::::::::: : . |
                     |  |%%OO!!:::::::::::::  :|
                     |  |%%OO!!!::::::::::::: :|
            :       .'--`.%%OO!!!:::::::::::: :|
          : .:     /`.__.' %%OO!!!::::::::::::/
         :    .   /         %OO!!!!::::::::::/
        ,-'``'-. ;          ;%%OO!!!!!!:::::'
        |`-..-'| |   ,--.   |`%%%OO!!!!!!:'
        | .   :| |_.','`.`._|  `%%%OO!%%'
        | . :  | |--'    `--|    `%%%%'
        |`-..-'| ||   | | | |     |__|`-.
        |::::::/ ||)|/|)|)|/|           /
---------`::::'--|._ ~**~ _.|----------( -----------------------
           )(    |  `-..-'  |           |    ______
           )(    |          |,--.       ____/ /  /| | ,-._.-'
        ,-')('-. |          ||`;|   .-()___  :  |`.!,-'`'/`-._
       (  '  `  )`-._    _.-'|;,|    `-,    |_|__|`,-'>-.,-._
        `-....-'     ````    `--'      `-._       (`- `-._`-.   
''')
