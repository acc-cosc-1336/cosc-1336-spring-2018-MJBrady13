def non_contiguous_motif(str1, dna_list):

    index = -1
    num = 0
    list1 = []

    for i in str1:
        go = True
        while index < len(dna_list) and go:

            index+= 1
            if i == dna_list[index]:
                list1.append(index+1)
                go = False

    return list1[0], list1[1], list1[2]
