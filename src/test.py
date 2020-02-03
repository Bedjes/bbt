from utils.graphes import *

#On crée 4 sommets
n = [
    Node(1, 0, 0, "Début"),  #0
    Node(1, 0, 0, "Fin"),   #1
    Node(1, 0, 0, "A"),  #2
    Node(1, 0, 0, "B"), #3
    Node(1, 0, 0, "C"), #4
    Node(1, 0, 0, "D"), #5
    Node(1, 0, 0, "E"), #6
    Node(1, 0, 0, "F"), #7
    Node(1, 0, 0, "G"), #8
    Node(1, 0, 0, "H"), #9
    Node(1, 0, 0, "I"), #10
    Node(1, 0, 0, "J"), #11
    Node(1, 0, 0, "K"), #12
    Node(1, 0, 0, "L"), #13
    Node(1, 0, 0, "M"), #14
    Node(1, 0, 0, "N"), #15
    Node(1, 0, 0, "O"), #16
    Node(1, 0, 0, "P"), #17
    Node(1, 0, 0, "Q"), #18
    Node(1, 0, 0, "R"), #19
    Node(1, 0, 0, "S"), #20
    Node(1, 0, 0, "T"), #21
    Node(1, 0, 0, "U"), #22
    Node(1, 0, 0, "V"), #23
    Node(1, 0, 0, "W"), #24
    Node(1, 0, 0, "X"), #25
    Node(1, 0, 0, "Y") #26
]

#Attention: il faut que tous les voisins de chaque sommet soit renseigné sinon ca plante le markage des arettes
#On construit un graphe avec ces sommets
g = Graph({
    n[0]: [(n[2], 50), (n[3], 500), (n[4], 15) ],
    n[1]: [(n[26], 200), (n[23], 830), (n[22], 1300), (n[16], 750), (n[15], 50)],
    n[2]: [(n[0], 50)],
    n[3]: [(n[0], 500), (n[25], 500), (n[19], 200)],
    n[4]: [(n[0], 15), (n[6], 100)],
    n[5]: [(n[6], 300), (n[8], 100)],
    n[6]: [(n[4], 100), (n[19], 400), (n[17], 750), (n[7], 150), (n[5], 300)],
    n[7]: [(n[6], 150), (n[9], 250), (n[16], 10000)],
    n[8]: [(n[5], 100), (n[9], 50), (n[10], 200)],
    n[9]: [(n[7], 250), (n[14], 300), (n[8], 50)],
    n[10]: [(n[8], 200), (n[14], 10), (n[11], 450)],
    n[11]: [(n[10], 450), (n[12], 50)],
    n[12]: [(n[11], 50), (n[15], 50)],
    n[13]: [(n[14], 10)],
    n[14]: [(n[10], 10), (n[13], 10), (n[16], 1000)],
    n[15]: [(n[1], 50, (n[12], 50))], 
    n[16]: [(n[14], 1000), (n[7], 10000), (n[17], 300), (n[22], 200), (n[1], 750)],
    n[17]: [(n[16], 300), (n[6], 750), (n[22], 150)], 
    n[18]: [(n[19], 20)],
    n[19]: [(n[18], 20), (n[6], 400), (n[3], 200), (n[20], 300), (n[21], 800)],
    n[20]: [(n[19], 300), (n[21], 300)], 
    n[21]: [(n[19], 800), (n[20], 300), (n[22], 200)], 
    n[22]: [(n[1], 1300), (n[16], 200), (n[17], 150), (n[21], 200), (n[24], 300), (n[23], 250)],
    n[23]: [(n[1], 830), (n[22], 250), (n[24], 100)],
    n[24]: [(n[25], 2000), (n[22], 300), (n[23], 100), (n[26], 350)],
    n[25]: [(n[3], 500), (n[24], 2000)],
    n[26]: [(n[24], 350), (n[1], 200)]
}, "Test")

#On dessine le graphe
g.draw()