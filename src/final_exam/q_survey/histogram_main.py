from histogram import display_histogram

file = open('survey.dat', 'r')

for line in file:
    list1 = line.split()
    display_histogram(list1)
    print('\n')

file.close()
