import numpy as np
import generalUtils

class tree:
    #the goal of procedural generation is to conserve computer resources and generate the tree only as required.
    #due to the unique constraints of the situation, that being the user is not able to perform backwards manipulation
    #preceding portions of the tree can be "forgotten" and future paths are generated as-needed

    #this allows for the loading of extremely high-dimension matrices with unknown projected memory sizes to be
    #represented with a predetermined amount of memory space using lower-dimension local representations
    #specifically, the parts of the larger matrix loaded composes of a "present" buffer and a "look-ahead buffer"

    seed = [0, 0, 0]
    currentDepth = 1
    presentBuffer = 0
    lookAheadBuffer = 0
    
    

    def generateRandomSeed(self, depth:list, branchPopulation:list, divergence:list) -> None:
        #depth: list of length 2 containing bounding ranges for random depth generation
        #branchPopulation: list of length 2 containing bounding ranges for random branch population
        #divergence: list of length 2 containing bounding ranges for branch count

        self.seed[0] = np.random.randint(depth[0], depth[1])
        self.seed[1] = np.random.randint(branchPopulation[0], branchPopulation[1])
        self.seed[2] = np.random.randint(divergence[0], divergence[1])
        self.presentBuffer = [0] * self.seed[1]
        self.lookAheadBuffer = np.zeros(self.seed[2], self.seed[1])


    def setSeed(self, depth: int, branchPopulation:int, divergence:int) -> None:
        self.seed[0] = depth
        self.seed[1] = branchPopulation
        self.seed[2] = divergence
        self.presentBuffer = [0] * self.seed[1]
        self.lookAheadBuffer = np.zeros(self.seed[2], self.seed[1])

    
        

    

            
        

