import unittest
import problem_721_accounts_merge as problem


class UnitTestData:
    def __init__(
        self,
        accounts: list[list[str]] = [],
    ):
        self.accounts = accounts


unittest_data = [
    UnitTestData(
        accounts=[
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ],
    ),
    UnitTestData(
        accounts=[
            ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
            ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
            ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
            ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
            ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
        ],
    ),
]


class TestSolution(unittest.TestCase):
    def test_fourSumCount(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.accountsMerge(item.nums1, item.nums2, item.nums3, item.nums4)
            self.assertEqual(result, item.expected)
