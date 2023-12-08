def vote_menu():
    print(f'--------------------')
    print(f'VOTE MENU')
    print(f'--------------------')
    print(f'v: Vote')
    print(f'x: Exit')
    option = str(input('Option: ').lower().strip())
    while option != 'v' and option != 'x':
        option = str(input('Invalid (v/x): ').lower().strip())

    return option


def candidate_menu():
    print(f'--------------------')
    print(f'CANDIDATE MENU')
    print(f'--------------------')
    print(f'1: John')
    print(f'2: Jane')
    president = int(input('Candidate: '))
    while president != 1 and president != 2:
        president = int(input('Invalid (1/2): '))
    return president


def main():
    Jane = 0
    John = 0
    Total = 0
    option = vote_menu()
    while option != 'x':
        if option == 'v':
            president = candidate_menu()
            if president == 1:
                John += 1
                Total += 1
                print(f'Voted John')
            elif president == 2:
                Jane += 1
                Total += 1
                print(f'Voted Jane')
            option = vote_menu()
    print(f'--------------------')
    print(f'John - {John}, Jane - {Jane}, Total - {Total}')
    print(f'--------------------')


main()
