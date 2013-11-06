import random
import copy
class Algorithme:
    """Classe mère des algorithmes."""

    def __init__(self, nbCoupsMax, listBras, numAlgo):
        self.gain=0
        self.nbCoupsJoue=0
        self.nbCoupsMax = nbCoupsMax
        
        self.listBras = copy.deepcopy(listBras)

        self.numAlgo = numAlgo
                  
    def actionnerBras(self, numeroBras):
        """ Cette fonction actionne le bras demandé. Sauf dans le cas du gain espéré où le gain est ajouté directement."""
        self.nbCoupsJoue += 1
        
        # Le gain est calculé différemment si il s'agit de l'algo utilisé pour connaître le gain espéré. En effet, nous voulons alors connaître la VERITABLE ESPERANCE.
        if (self.numAlgo == -1):
            self.gain += self.esperanceVeritable(numeroBras)
        else:        
            self.gain += self.listBras[numeroBras].actionner()
          

    def esperanceCalculee(self, numeroBras):
        """ Cette fonction retourne l'espérance calculée."""
        return self.listBras[numeroBras].esperanceCalculee()        

    def esperanceVeritable(self, numeroBras):
        """ Cette fonction retourn l'espérance véritable."""
        return self.listBras[numeroBras].esperanceVeritable()        

        
    
    def lancerAlgo(self):
        """Cette fonction est appelée pour lancer l'algorithme, et actionner le bras ensuite."""
       
        if self.numAlgo == -1:
            res = self.algoGainEspere()
        if self.numAlgo == 1:
            res = self.algoHasard()
        if self.numAlgo == 2:
            res = self.algoGlouton()
        self.actionnerBras(res)

    def lancerAlgoEntierement(self):
        """Cette fonction est appelée pour lancer l'algorithme autant de fois que nbCoupsMax."""
        
        for i in range(0,self.nbCoupsMax):
            self.lancerAlgo()


    def algoGainEspere(self):
        
        numeroMeilleurBras=-1
        gainMeilleurBras=-1

        # Pour chaque bras, je vais regarder la VERITABLE espérance et essayer de trouver le meilleur bras.
        for i in range(0,len(self.listBras)):
            if self.esperanceVeritable(i) > gainMeilleurBras:
                numeroMeilleurBras = i
                gainMeilleurBras = self.esperanceVeritable(i)

        return numeroMeilleurBras


    def algoHasard(self):
        return random.randint(0,len(self.listBras)-1)

    def algoGlouton(self):
        jeuApprentissage = 0.5 # 50% du nombre de coups max sera utilisé pour connaitre le meilleur bras.  
        if self.nbCoupsJoue < jeuApprentissage*self.nbCoupsMax :
            res = self.nbCoupsJoue % len(self.listBras)
        else:
            numeroMeilleurBras=-1
            gainMeilleurBras=-1

            # Pour chaque bras, je vais regarder l'espérance et essayer de trouver le meilleur bras.
            for i in range(0,len(self.listBras)):
                if self.listBras[i].esperanceCalculee() > gainMeilleurBras:
                    numeroMeilleurBras = i
                    gainMeilleurBras = self.listBras[i].esperanceCalculee()

            res = numeroMeilleurBras
        return res



