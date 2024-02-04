print("Doraemon:)")
print("Enter the characters of this cartoon to form a story")
character1 = input("Enter a character1: ")
character2 = input("Enter a character2: ")
character3 = input("Enter a character3: ")
character4 = input("Enter a character4: ")
place = input("Enter a place: ")
adjective1 = input("define character1's personality: ")
adjective2 = input("define character2's personality: ")
adjective3 = input("define character3's personality: ")
verb_past_tense = input("Enter a verb_past_tense: ")
verb3 = input("Enter a verb3: ")

#code
story = f"Once upon a time in {place}, there lived a {adjective1} boy named {character1}. One day, {character1} {verb_past_tense} for hours, avoiding his responsibilities and chores. Little did he know, his {adjective2} friend {character2} was worried about him."

story += f"\n\nMeanwhile, in the neighborhood, the {adjective3} {character3} was causing trouble. He had {verb3} a ball into {character4}'s garden, and {character4} was not happy about it. {character4}, known for being quite cunning, decided to seek revenge."

story += "\n\nAs the tension in the neighborhood escalated, Doraemon, the robotic cat from the future, appeared with his magical pocket filled with gadgets. Doraemon knew that the key to resolving the conflicts was communication and understanding."

story += f"\n\nDoraemon approached {character1} and encouraged him to open up to his friends. With a gadget that translated emotions into words, {character1} finally expressed his feelings of stress and pressure. {character2}, being {adjective2}, comforted {character1}, and together they came up with a plan to manage his responsibilities more effectively."

story += f"\n\nIn the end, {character1} learned the importance of facing challenges and seeking support from friends. The {adjective1} days were behind him, and with the help of his {adjective2} friends and the magical gadgets from Doraemon, he embraced a more balanced and fulfilling life in {place}."

print(story)
