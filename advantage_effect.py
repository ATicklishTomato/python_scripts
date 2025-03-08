import random
import matplotlib.pyplot as plt

def dice_roll():
    return random.randint(1, 20)

def advantage_roll():
    return max(dice_roll(), dice_roll())

def disadvantage_roll():
    return min(dice_roll(), dice_roll())

def main():
    num_trials = 1000000
    regular_results = [dice_roll() for _ in range(num_trials)]
    advantage_results = [advantage_roll() for _ in range(num_trials)]
    disadvantage_results = [disadvantage_roll() for _ in range(num_trials)]

    regular_results = [regular_results.count(i) / num_trials for i in range(1, 21)]
    advantage_results = [advantage_results.count(i) / num_trials for i in range(1, 21)]
    disadvantage_results = [disadvantage_results.count(i) / num_trials for i in range(1, 21)]

    plt.plot(range(1, 21), regular_results, label='Regular Roll')
    plt.plot(range(1, 21), advantage_results, label='Advantage Roll')
    plt.plot(range(1, 21), disadvantage_results, label='Disadvantage Roll')
    plt.xlabel('Roll Value')
    plt.ylabel('Probability')
    plt.title('Advantage/Disadvantage Effect on D&D Rolls')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()