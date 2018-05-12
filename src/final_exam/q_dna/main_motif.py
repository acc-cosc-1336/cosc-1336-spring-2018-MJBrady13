def non_contiguous_motif(str1, dna_list):

    index = -1
    num = 0

    for i in str1:
        for j in dna_list:
            index+= 1
            if i == j:
                num = index
                return num
