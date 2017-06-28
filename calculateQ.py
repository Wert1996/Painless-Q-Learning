# Implementation of the room finding task 
# as given in the "Painless Q = Learning
# tutorial".
import numpy as np

rewards = np.tile(-1, (6,6))
rewards[0,4] = 0
rewards[1,3] = 0
rewards[1,5] = 100
rewards[2,3] = 0
rewards[3,1] = 0
rewards[3,2] = 0
rewards[3,4] = 0
rewards[4,0] = 0
rewards[4,3] = 0
rewards[4,5] = 100
rewards[5,1] = 0
rewards[5,4] = 0
rewards[5,5] = 100


def calQ():
    n_episodes = 100
    Q = np.zeros((6,6))

    gamma = 0.8
    for episode in range(n_episodes):
        current = np.random.choice(6,1)[0]
        while(True):
        # print("Current is ", current)
            nextChoice = np.random.choice([num for num in range(6) 
                                       if rewards[current, num] != -1], 1)[0]
        # print("Possible actions are ", [num for num in range(6) if rewards[current, num] != -1])
        # print("Chosen next choice is ", nextChoice)
            Q[current, nextChoice] = rewards[current, nextChoice] + gamma*np.max(Q[nextChoice, :])
        # print("Maximum Q for nextchoice is ", np.max(Q[nextChoice, :]))
        # print ("Q value updated is ", Q[current, nextChoice])
            if current == 5:
                break
            current = nextChoice
    Q = np.array([round(num/5) for li in Q for num in li])
    Q = Q.reshape((6,6))
    return Q

if __name__=="__main__":
    print(calQ())
