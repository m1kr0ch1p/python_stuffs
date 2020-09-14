import re
alphabet = {'a':'Alpha','b':'Betha','c':'Charlie','d':'Deltha','e':'Echo','f':'Fox trot', \
    'g':'Golf','h':'Hotel','i':'india','j':'Julliet','k':'Kilo','l':'Lima','m':'Mike','n':'November', \
    'o':'Oscar','p':'Papa','q':'Quebec','r':'Romeo','s':'Sierra','t':'Tango','u':'Uniform', \
    'v':'Victor','w':'Wisky','x':'X-ray','y':'Yankee','z':'Zulu'}
#print(alphabet)
       
word = input('Give me a word and I will spell it for you, SIR! ')
  
if word.isalpha():  
    letter = list(word.lower())
    for char in letter:
        print(str(alphabet[char])+'!')
    #print(" ")
    print("         .---.")
    print("    ___ /_____\\")
    print("   /\.-`( '.' )")
    print("  / /    \_-_/_")
    print("  \ `-.-\"`'V'//-.")
    print("   `.__,   |// , \\")
    print("       |Ll //Ll|\ \\")

else:
    print('I needed a SPELLABLE word!\nPermission to be dismissed, SIR!\n')
    print('       \\ /////')
    print('       |      |')
    print('      (| _  _ |)')
    print("       |` |  '|")
    print('       |  __  |')
    print(' >>>___/\_^__/\___<<<')
    print("/               |||  \\")