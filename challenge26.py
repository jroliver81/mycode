print("Which character do you want to know about? (Starlord, Mystique, Hulk) ") 
char_name = input()

print("What statistic do you want to know about? (real name, powers, archenemy)")
char_stat = input()

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

result = marvelchars.get(char_name).get(char_stat)
print(f"{char_name}'s {char_stat} is: {result}")



