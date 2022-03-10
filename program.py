
class demon:
    def __init__(self, staminaConsumed, recoveryTurns, staminaRecovered, fragmentTurns, fragmentPoints):
        self.staminaConsumed = staminaConsumed
        self.staminaRecoveryTurns = recoveryTurns
        self.staminaRecovered=staminaRecovered
        self.fragmentTurns=fragmentTurns
        self.fragmentPointSequence = list()
        self.consumed=False
        for j in fragmentPoints:
            self.fragmentPointSequence.append(int(j))



class player:
    def __init__(self, stamina, max_stamina, turns, demons):
        self.stamina = stamina
        self.maxStamina = max_stamina
        self.turns = turns
        self.demonsCount = demons
        self.fragments = int()
        self.answersequence=list()
        self.pendingStamina=dict()
    def eligibleDemon(self, demonn):
        if(demonn.staminaConsumed <=self.stamina and demonn.consumed==False):
            return True
        else:
            return False

    
    def fightDemon(self, demonn):
        demonn.consumed=True
        self.stamina -= demonn.staminaConsumed
        # if(demonn.staminaRecoveryTurns==1):
        #     self.stamina+=demonn.staminaRecovered
        #     demonn.staminaRecoveryTurns=0
        #     print(self.stamina)
        # else:
        self.pendingStamina[demonn.staminaRecovered]= demonn.staminaRecoveryTurns

    def eligibleStamina(self):
        if(self.stamina<self.maxStamina):
            return True
        else:
            return False



with open("03-etheryum.txt", "r") as file:
    file_liness=file.readlines()
    file_lines=list()
    for i in file_liness:
        file_lines.append(i.split())
    print(file_lines)


player1 = player(int(file_lines[0][0]),int(file_lines[0][1]),int(file_lines[0][2]),int(file_lines[0][3]))

demonlist = list()
for i in range(1, int(file_lines[0][3])+1):
    demonSample = demon(int(file_lines[i][0]), int(file_lines[i][1]), int(file_lines[i][2]), int(file_lines[i][3]), file_lines[i][4:-1])
    demonlist.append(demonSample)


for k in range(player1.turns):
    print(player1.pendingStamina)
    pendstamina = player1.pendingStamina.keys()
    for s in pendstamina:
        if(player1.pendingStamina[s]>0):
            if(player1.pendingStamina[s]==1):
                if(player1.eligibleStamina()):
                    player1.stamina+=s
                    player1.pendingStamina[s]-=1
            player1.pendingStamina[s]-=1
    print(player1.stamina)
    demons_eligible = list()
    for d in demonlist:
        demons_eligible.append(player1.eligibleDemon(d))
    eligibledemoncount=0
    for d in demons_eligible:
        if(d==True):
            eligibledemoncount+=1

    if(eligibledemoncount>1):
        firstscores=dict()
        for d in range(len(demons_eligible)):
            if(demons_eligible[d]==True):
                #print(firstscores, "\n", demonlist[d].fragmentPointSequence, "\n" , demonlist[d].fragmentTurns)
                #demonlist[d].fragmentPointSequence = [1,2,3]
                if(demonlist[d].fragmentTurns>1):
                    firstscores[d]=demonlist[d].fragmentPointSequence[0]
        if(firstscores!={}):
            #print(firstscores,"\n",firstscores.get)
            demonindex= max(firstscores, key=firstscores.get)
            player1.fightDemon(demonlist[demonindex])
            demonlist[demonindex].consumed = True
            player1.answersequence.append(demonindex)
    elif(eligibledemoncount==1):
        for di in range(len(demons_eligible)):
            if(demons_eligible[di]==True):
                d_id=di
        player1.fightDemon(demonlist[d_id])
        player1.answersequence.append(d_id)
    else:
        pass

for t in range(len(demons_eligible)):
    if(demonlist[t].consumed==False and demons_eligible[t]==False):
        player1.answersequence.append(t)


with open("ans03.txt" , "w") as answerfile:
    for answer in player1.answersequence:
        answerfile.write(str(answer) + "\n")


