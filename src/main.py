from environment import Environment

# Initial amount of women
women_amount = 500

# Initial amount of men
men_amount = 500

# Duration of simulation in months
duration = 50*12

if __name__ == "__main__":
    environment = Environment(women_amount, men_amount, duration)
    environment.simulate()

    # print results
    print()
    print('Final results:')
    print('Total habitants:', len(environment.poblation))

    deseases = 0
    for habitant in environment.poblation:
        if habitant.is_dead:
            deseases += 1

    print('Deseases:', deseases)
    print('Alive:', len(environment.poblation) - deseases)