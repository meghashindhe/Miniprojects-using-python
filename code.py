noun_plural1 = input("Noun (plural): ")
noun_plural2 = input("Noun (plural): ")
# input for variables adj1, body_part, verb, adj2, adj3, adj4, and noun
adj1 = input("Adjective: ")
body_part = input("Body part: ")
verb = input("Verb: ")
verb1 = input("another Verb: ")
adj2 = input("Another adjective: ")
adj3 = input("One more adjective: ")
adj4 = input("Yet another adjective: ")
adj5 = input("Last adjective: ")
noun = input("Noun: ")

# rest of the code remains the same


madlib = f" I love Biology because it's {adj1}! The journey to becoming a " + \
f"good scientist starts with intrest in your subject and a dream in your {body_part}. Through blood, sweat, and tears, you will learn to be a {noun_plural1} and a {adj2}. Yes, once you learn to {verb}, it becomes " + \
f"a part of your daily routine and become your {adj3} power. Knowledge of concepts " + \
f"Lets control your grip on diagrams and explanations of {noun_plural2}, anything " + \
f"maybe even recreate Charles Darwin and make him extra {adj4}. I hope you all start your {adj5} journey by learning to {verb} and {verb1}."+ \
f"coding with {noun} :)".format(
        adj1=adj1, body_part=body_part, noun_plural1=noun_plural1, verb=verb, adj2=adj2, adj3=adj3, adj4=adj4, noun_plural2=noun_plural2, noun=noun, verb1=verb1
)
"coding with me :)"

print(madlib)
