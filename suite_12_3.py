from tests_for_suite import RunnerTest, TournamentTest
import unittest


ttr_1 = unittest.TextTestRunner(verbosity=2)
runner_suite = unittest.TestSuite()
runner_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
runner_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

ttr_1.run(runner_suite)
