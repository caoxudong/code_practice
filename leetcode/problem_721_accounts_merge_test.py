import unittest
import leetcode.problem_721_accounts_merge as problem


class UnitTestData:
    def __init__(
        self,
        accounts: list[list[str]] = [],
        expected: list[list[str]] = [],
    ):
        self.accounts = accounts
        self.expected = expected


unittest_data = [
    UnitTestData(
        accounts=[
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ],
        expected=[
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
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
        expected=[
            ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
            ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
            ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
            ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
            ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"],
        ],
    ),
    UnitTestData(
        accounts=[
            ["David", "David0@m.co", "David1@m.co"],
            ["David", "David3@m.co", "David4@m.co"],
            ["David", "David4@m.co", "David5@m.co"],
            ["David", "David2@m.co", "David3@m.co"],
            ["David", "David1@m.co", "David2@m.co"],
        ],
        expected=[
            [
                "David",
                "David0@m.co",
                "David1@m.co",
                "David2@m.co",
                "David3@m.co",
                "David4@m.co",
                "David5@m.co",
            ]
        ],
    ),
]


class TestSolution(unittest.TestCase):
    def test_accountsMerge(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.accountsMerge(item.accounts)
            self.assertListEqual(sorted(result), sorted(item.expected))
