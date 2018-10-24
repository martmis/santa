import pandas as pd
import numpy as np
import sqlite3


#def get_list():

cnx = sqlite3.connect('database.db')
cursor = cnx.execute("SELECT name FROM santas")
i=0
santas = []
rows = cursor.fetchall();
for row in rows:
    santas.append(row[0])
    print(row[0])
    i = i + 1
print(santas)

to_pickup = np.array([santas.index(name) for name in santas])  # Int paired with each participant
print(str(len(to_pickup)) + ' santas')

# Initialisation tirage au sort
pickedup = np.array([])
results = ""

np.random.seed(3690)
r = np.random.choice(to_pickup)
print("picked-up first: " + santas[r] + '(' + str(r) + ')' + '\n')
to_pickup = np.delete(to_pickup, np.where(to_pickup == r))
pickedup = np.append(pickedup, r)

# Who offers to who
for person in to_pickup:  # N-1 tirages au sort pour N santas
    r = np.random.choice(to_pickup)
    pickedup = np.append(pickedup, r)
    to_pickup = np.delete(to_pickup, np.where(to_pickup == r))
    results = results + santas[int(pickedup.item(-2))] + ' offers to ' + santas[r] + '\n'

# Final - results + last picked up offers to first picked-up
results = results + 'And ' + santas[int(pickedup.item(-1))] + ' offers to ' + santas[int(pickedup.item(0))] + '\n'
print(results)
cnx.close()

