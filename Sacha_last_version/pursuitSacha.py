# COLL SACHA pursuit
import math
from tkinter import IntVar
import numpy as np
import matplotlib.pyplot as plt


# Vitesse de Target :
Vtarget = 0.1 # k

# Distance entre Target et Robot :
Dtrob = 1.0   # Lfc = 1.0

# Gain Vitesse pour régler rampe d'accélération
# Kp : https://ctms.engin.umich.edu/CTMS/index.php?example=Introduction&section=ControlPID
Krampe = 2.0 # Kp = 1.0

# Dt [s] ????
dt = 0.1 

# Empattement robot [m]
L = 2.9

list_detect = [] # Stabilisation des changements de vitesse


show_animation = True

class State:

    # Initialisation position
    def __init__(self, x=0.0, y=0.0, yaw=0.0, v=0.0):
        self.x = x          # Xrobot
        self.y = y          # Yrobot
        self.yaw = yaw      # Angle de rotation du Robot https://automaticaddison.com/yaw-pitch-and-roll-diagrams-using-2d-coordinate-systems/
                            #                            https://en.wikipedia.org/wiki/Yaw_(rotation)
        self.v = v          # Vitesse 
        self.dyaw = 0.0
        # self.vang = vang


    # Met à jour la position du robot (X;Y;Yaw;V)
def update(state, a, delta):
    global detect
    global tryagain
    global target_speed
    global cpt
    # Calcul de X et Y p.6 : https://homes.cs.washington.edu/~todorov/courses/cseP590/05_Kinematics.pdf
    state.x = state.x + state.v * math.cos(state.yaw) * dt      # Update Position X
    state.y = state.y + state.v * math.sin(state.yaw) * dt      # Update Position Y
    print(state.v / L * math.tan(delta) * dt)
    state.dyaw = state.v / L * math.tan(delta) * dt
    print(tryagain)
    print(cpt)
    """ if (detect<0 and detect - state.dyaw < 0) or (detect>0 and detect - state.dyaw > 0) : # Si changement de signe de vitesse angulaire
         #state.v = state.v - a * dt/2
         # and ((state.dyaw < -0.00) or (state.dyaw > 0.00))
        tryagain = True
        cpt += 1
    else: 
         #state.v = state.v + a * dt
        tryagain = False

    if tryagain and cpt<20:
        target_speed = 10.0/3.6
        cpt = 0
    else:
        target_speed = 3.0/3.6"""

    if ((detect<0 and detect - state.dyaw > 0) or (detect>0 and detect - state.dyaw < 0)) and (state.dyaw>0.01 or state.dyaw < -0.01) : # Si changement de signe de vitesse angulaire
                                        #<                                        #>
         #state.v = state.v - a * dt/2
         # and ((state.dyaw < -0.00) or (state.dyaw > 0.00))
        #tryagain = True
        cpt += 1
        if cpt<20: # cpt<30 60 100
            tryagain = True
        else:
            exit
    else: 
         #state.v = state.v + a * dt
        tryagain = False
        cpt = 0

    if tryagain:
        target_speed = 1.0/3.6
        #cpt = 0
    else:
        target_speed = 13.0/3.6
    state.yaw = state.yaw + state.v / L * math.tan(delta) * dt  # Update Angle Rotation Yaw
    state.v = state.v + a * dt                                  # Update Vitesse
    #state.vang = state.vang + newvang
    detect = state.v / L * math.tan(delta) * dt
    return state

    # Variation du rapport cyclique du moteur
def PIDControl(target, current):         # Proportional Integral Derivative => Vcurrent est mesurée et comparée avec vitesse voulue
    a = Krampe * (target - current)      # Explication de cette formule : https://www.sciencedirect.com/topics/computer-science/proportional-controller

    return a

    # Calcul Point de passage le plus proche du véhicule => Trouve l'indicateur du point
def calc_target_index(state, cx, cy): # Calcul l'indicateur

    # Recherche de l'index du point le plus proche
    dx = [state.x - icx for icx in cx]      # dx = Xrobot - Xchemin
    dy = [state.y - icy for icy in cy]      # dy = Yrobot - Ychemin
    d = [abs(math.sqrt(idx ** 2 + idy ** 2)) for (idx, idy) in zip(dx, dy)]     # Distance Robot(x;y)-> FuturTarget(x;y)
    ind = d.index(min(d))       # Récupère index de la distance la plus petite
    L = 0.0                     # Init de L

    Lf = Vtarget * state.v + Dtrob

    # search look ahead target point index
    while Lf > L and (ind + 1) < len(cx):
        dx = cx[ind + 1] - cx[ind]
        dy = cy[ind + 1] - cy[ind]
        L += math.sqrt(dx ** 2 + dy ** 2) # L = L + ds
        ind += 1
############ RAJOUTER MODIF DE LA VITESSE  + MODIF Vangulaire
    return ind

def pure_pursuit_control(state, cx, cy, pind):

    ind = calc_target_index(state, cx, cy) # Récupère l'index du prochain point

    if pind >= ind:                        # Si indicateur position robot >= indicateur prochain point
        ind = pind                         # On met à jour l'indicateur du prochain point

    if ind < len(cx):                      # Si il reste des points du chemin
        tx = cx[ind]                       #Target(x = Xcheminprochainpoint ; y = Ycheminprochainpoint)
        ty = cy[ind]
    else:
        tx = cx[-1]                        # Sinon Target(x = Xcheminprochainpoint-1 ; y = Ycheminprochainpoint-1)
        ty = cy[-1]                        ############################ A modifier si on veut arriver à l'arrivée
        ind = len(cx) - 1                  # Met à jour l'indicateur du prochain point

    alpha = math.atan2(ty - state.y, tx - state.x) - state.yaw

    if state.v < 0:  # back
        alpha = math.pi - alpha

    Lf = Vtarget * state.v + Dtrob

    delta = math.atan2(2.0 * L * math.sin(alpha) / Lf, 1.0)

    return delta, ind

target_speed = 0
cpt = 0
def main():
    # Chemin Généré par A*
    cx = np.arange(0, 60, 0.1) # (Xdebut, Xarrivée, Step)
    cy = [math.sin(ix / 5.0) * ix / 2.0 for ix in cx]

    # RÉGLER VITESSE
    #target_speed = 10.0 / 3.6  # [m/s]

    # TEMPS MAX SIMULATION
    T = 100.0 

    # INITIALISATION DU ROBOT ( POSITION INITIALE )
    state = State(x=-0.0, y=-3.0, yaw=0.0, v=0.0)

    # Dernier Index = Index du Dernier Point - 1
    lastIndex = len(cx) - 1
    time = 0.0

    # Récupère Infos du Robot
    x = [state.x] 
    y = [state.y]
    yaw = [state.yaw]
    v = [state.v]
    t = [0.0]
    dyaw = [0.0]

    # Index de la Cible 
    target_ind = calc_target_index(state, cx, cy)

    # Tant que Tsimu>0 ou Point d'Arrivée Pas Passé
    while T >= time and lastIndex > target_ind:
        ai = PIDControl(target_speed, state.v)                           # Récupère le coef d'accélération ( PID )
        di, target_ind = pure_pursuit_control(state, cx, cy, target_ind) # Récupère Delta et l'Indicateur à jour
        state = update(state, ai, di)                                    # Met à jour infos robot

        time = time + dt                                                 # Met à jour temps

        # Init des Listes des infos du robot
        x.append(state.x)
        y.append(state.y)
        yaw.append(state.yaw)
        v.append(state.v)
        t.append(time)
        dyaw.append(state.dyaw)

        if show_animation:
            plt.cla()
            plt.plot(cx, cy, ".r", label="course")                        # CHEMIN GÉNÉRÉ PAR A*
            plt.plot(x, y, "-b", label="trajectory")                      # TRAJECTOIRE EMPRUNTÉ PAR ROBOT
            plt.plot(cx[target_ind], cy[target_ind], "xg", label="target")
            plt.axis("equal")
            plt.grid(True)
            plt.title("Speed[km/h]:" + str(state.v * 3.6)[:4])            # Affichage vitesse en [km/h]
            plt.pause(0.001)







################################### RESTANT ###################################
    assert lastIndex >= target_ind, "Cannot goal"

    if show_animation:
        plt.plot(cx, cy, ".r", label="course") # CHEMIN GÉNÉRÉ PAR A*
        plt.plot(x, y, "-b", label="trajectory") # TRAJECTOIRE EMPRUNTÉ PAR ROBOT
        plt.legend()
        plt.xlabel("x[m]")
        plt.ylabel("y[m]")
        plt.axis("equal")
        plt.grid(True)

        flg, ax = plt.subplots(1)
        #plt.plot(t, [iv * 3.6 for iv in v], "-r")
        plt.plot(t, [iv for iv in dyaw], "-r")
        plt.xlabel("Time[s]")
        plt.ylabel("Speed[km/h]")
        plt.grid(True)
        plt.show()


tryagain = False
detect = 0

if __name__ == '__main__':
    print("Pure pursuit path tracking simulation start")
    main()
