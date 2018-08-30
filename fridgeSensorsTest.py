import unittest
from statistics import mean, median

import fridgeSensors


class Test(unittest.TestCase):
    testDictionary = {'a': [3.53, 3.63, 4.63, 3.53, 3.66, 3.67], 'c': [3.96, 3.96, 3.95, 3.36, 3.36],
                      'b': [4.13, 4.15, 4.15, 3.88]}

    def testAverages(self):
        """
        Tests if the averages calculated by the calculateAverages function is equal to the imported mean method.
        :return: 
        """
        averages = fridgeSensors.calculateAverages(self.testDictionary)
        for id in averages:
            if id == "a":
                self.assertEqual(averages[id], round(mean(self.testDictionary[id]), 2))
            elif id == "b":
                self.assertEqual(averages[id], round(mean(self.testDictionary[id]), 2))
            elif id == "c":
                self.assertEqual(averages[id], round(mean(self.testDictionary[id]), 2))

    def testMedians(self):
        """
        Tests if the averages calculated by the calculateAverages function is equal to the imported median method.
        :return: 
        """
        medians = fridgeSensors.calculateMedians(self.testDictionary)
        for id in medians:
            if id == "a":
                self.assertEqual(medians[id], round(median(self.testDictionary[id]), 2))
            elif id == "b":
                self.assertEqual(medians[id], round(median(self.testDictionary[id]), 2))
            elif id == "c":
                self.assertEqual(medians[id], round(median(self.testDictionary[id]), 2))

    def testModes(self):
        """
        Tests if the averages calculated by the calculateAverages function is equal to manually entered expected results.
        :return: 
        """
        modes = fridgeSensors.calculateModes(self.testDictionary)
        for id in modes:
            if id == "a":
                self.assertEqual(modes[id], [3.53])
            elif id == "b":
                self.assertEqual(modes[id], [4.15])
            elif id == "c":
                self.assertEqual(modes[id], [3.96, 3.36])


if __name__ == '__main__':
    unittest.main()