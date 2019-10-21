from Battleground import *
import matplotlib.pyplot as plt


def plot_graf( x = None, y = None):
    """ x,y: lists
        plot commits polarity evolution"""
    if x and y:
        plt.xlabel("Player")
        plt.ylabel("no_of_rounds")
        plt.title("Battle evolution")
        plt.plot(x,y)
        plt.show()
        
def plot_hist(x,r):

    fig, ax = plt.subplots()
    ax.plot(x,r)
    plt.xlabel('round')
    plt.ylabel('Probability')
    plt.show()
    
if __name__ == "__main__":

    winner_list = []
    rounds_list = []
    
    for i in range(3):
        r = 0
        # create players
        hero = Hero("Orderus", health = randint(70,100), strength = randint(70,80), defence = randint(45,55), speed = randint(40,50), luck = randint(10,30))
        creature = Creature("Beast", health = randint(60,90), strength = randint(60,90), defence = randint(40,60), speed = randint(40,60), luck = randint(25,40))
    
    
        
        first_round = Battle(hero,creature)
        
        
        # check who attacks first
        first_round > first_round
    
        #battle as long as both obj have positive health
        while all(map(lambda x: x>0, [first_round.hero.get_health(), first_round.creature.get_health()])):
            Battle.print_stats(first_round.hero, first_round.creature, verbose=False)
            first_round.fight()

            r += 1
            #check if 20 turns where reached
            if first_round.fight.calls == 20:
                print("Number of max 20 turns has been reached")
                winner_list.append(first_round.check_winner())
                rounds_list.append(r)
                
                
                

        rounds_list.append(r)    
        winner_list.append(first_round.check_winner())

    hero_wins = list(map(lambda x: 1 if x == "Hero" else 0,winner_list))
    creature_wins = list(map(lambda x: 1 if x == "Creature" else 0,winner_list))

    plot_hist(hero_wins,rounds_list)
        
        
        
