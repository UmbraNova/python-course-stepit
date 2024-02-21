# import unittest


# class TestMate(unittest.TestCase):

#     def test_adunare(self):
#         self.assertEqual(2+2, 4)
 

# if __name__ == "__main__":
#     unittest.main()

import unittest
import random
import mate


x, y = 5, 19
m, n = 88, 92
q, f = False, True

class Test_mate(unittest.TestCase):
    def test_adunare(self):
        self.assertEqual(2+2, 4)
        self.assertEqual(20+10, 30)

    def test_scadere(self):
        self.assertEqual(10-6, 4)

    def test_false(self):
        self.assertFalse(x == y)  # interesant

    def test_true(self):
        self.assertTrue(2 < 7)

    def test_fail_unless(self):
        self.failUnless(f)
        self.failUnless(m)
    
    def test_not_equal(self):
        self.assertNotEqual(1299+1, 1301)
        self.assertNotEqual(m, n)
        self.assertNotEqual(q, f)


class Test_other(unittest.TestCase):
    def test_equal_cycle(self):
        self.assertEqual([i for i in range(2)][1]+3, 4)

    def test_random_cycle(self):
        self.assertTrue([i for i in range(random.randint(0,3))][random.randint(0,2)]+3, 5)
        
    def test_random_cycle(self):
        self.assertIsNot(this_var, this_var_2)


class Test_mate_py(unittest.TestCase):
    def test_some_func(self):
        # mate.inmultire(4, 6)
        # result = mate.inmultire(4, 6)
        # self.assertEqual(result, 24)
        self.assertEqual(mate.inmultire(4, 6), 24)

this_var = Test_mate()
this_var_2 = Test_mate()

class Test_sound(unittest.TestCase):
    def some_f(self):
        import winsound

        winsound.PlaySound("button-press.mp3", 0)
        winsound.PlaySound("sounds/button-press.mp3", 0)
        winsound.PlaySound("../sounds/button-press.mp3", 0)
        winsound.PlaySound("students-shuffle/sounds/button-press.mp3", 0)
        winsound.PlaySound("../students-shuffle/sounds/button-press.mp3", 0)