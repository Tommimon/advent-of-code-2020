with open('input.txt', 'r') as file:
    seats = file.read().split('\n')
    seats.remove('')
    for i in range(len(seats)):
        seats[i] = seats[i].replace('F', 'L').replace('L', '0')
        seats[i] = seats[i].replace('B', 'R').replace('R', '1')
        seats[i] = int(seats[i], 2)
    print(max(seats))
    seats.sort()
    for i in range(len(seats)-1):
        if(seats[i+1]-seats[i] == 2):
            print(seats[i]+1)
