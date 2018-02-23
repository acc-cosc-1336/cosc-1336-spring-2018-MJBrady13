import unittest
#write the import for function get_count_A_C_G_and_T_in_string
from src.assignments.assignment6 import get_count_A_C_G_and_T_in_string


class Test_Assign6(unittest.TestCase):

    def test_countACGT_w_string_ATGCTTCAGAAAGGTCTTACG(self):
        '''
        Create a test case to test the count of As, Cs, Gs, and Ts in string ATGCTTCAGAAAGGTCTTACG
        '''
        A_count, C_count, G_count, T_count = get_count_A_C_G_and_T_in_string('ATGCTTCAGAAAGGTCTTACG')
        self.assertEqual(6, A_count)
        self.assertEqual(4, C_count)
        self.assertEqual(5, G_count)
        self.assertEqual(6, T_count)


    def test_count_ACGT_w_stringAGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC(self):
        '''
        Create a test case to test the count of As, Cs, Gs, and Ts in string
        AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
        '''
        A_count, C_count, G_count, T_count = get_count_A_C_G_and_T_in_string('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
        self.assertEqual(20, A_count)
        self.assertEqual(12, C_count)
        self.assertEqual(17, G_count)
        self.assertEqual(21, T_count)
