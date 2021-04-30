import unittest 
from matrix import *
from copy import deepcopy


class test_matrix(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('\nteardownClass')

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_multiply_vec_by_scalar(self):
        v = multiply_vec_by_scalar([1,1,1],2)
        self.assertEqual(v, [2,2,2])
        self.assertIsInstance(v, list)

    def test_mat_multiply(self):
        A = [
            [1,0],
            [0,1]
        ]

        B = [
            [2,0],
            [0,2]
        ]

        badB = deepcopy(B)
        self.assertIsNot(badB,B)
        badB.append([1,1])
        self.assertRaises(Exception, mat_multiply, A, badB)
        self.assertEqual(mat_multiply(A,B),B)

        
        
        



if __name__ == '__main__':
    # A = [
    #     [1,0],
    #     [0,1]
    # ]

    # B = [
    #     [2,0],
    #     [0,2]
    # ]

    # badB = deepcopy(B)
    # badB.append([1,1])
    # mat_multiply(A, badB)
    unittest.main()