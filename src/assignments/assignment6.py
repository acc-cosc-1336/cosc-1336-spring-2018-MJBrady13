def get_count_A_C_G_and_T_in_string(dna_string):
    '''
    Create a function named get_count_A_C_G_and_T_in_string with a parameter named dna_string.

    :param dna_string: a DNA string
    :return: the count of As, Cs, Gs, and Ts in the dna_string
    '''
    dna_string = dna_string.upper()

    As = 0
    Cs = 0
    Gs = 0
    Ts = 0

    for ch in dna_string:
        if ch == 'A':
            As += 1
        elif ch == 'C':
            Cs += 1
        elif ch == 'G':
            Gs += 1
        else:
            Ts += 1
    return As,Cs,Gs,Ts

