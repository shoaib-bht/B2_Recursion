from functools import cmp_to_key
"""
Assignment_D: recursion
"""

class Recursion:

    numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]    #[4, 12, 3, 8, 17, 12, 1, 3, 8, 7]


    def sum(self, _numbers) -> int:
        """
        Return sum of numbers using recursion.
        Follow steps:
            1. Return 0 for an empty list of numbers.
            2. Split the problem by removing the first number `n1` from the list leaving `r` as remaining list (sub-problem).
            3. Invoke `sum(r)` recursively on the remaining list.
            4. Combine the result for the sub-problem with the first number `n1`: `return n1 + sum(r)`.
        """
        # your code
        if len(_numbers) == 0:
            return 0
        
        n1 = _numbers[0]
        r = _numbers[1:]
        return n1 + self.sum(r)

    def fib(self, _n, memo=None) -> int:
        """
        Return value of n-th Fibonacci number.
        - input: n=8
        - output: 21
        """
        # your code
        if memo is None:
            memo = {}
        if _n in memo:
            return memo[_n]
        if _n == 0:
            return 0
        if _n == 1:
            return 1
        result = self.fib(_n - 1, memo) + self.fib(_n - 2, memo)
        memo[_n] = result
        return result
    
    def fib_gen(self, _n):
        """
        Return a generator object that yields two lists, one with n and the
        other with corresponding fib(n).
        - input: n=16
        - output: generator object that produces:
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
             [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987])
        """
        # your code
        n_values = []
        fib_values = []
        if _n > 0:
            for i in range(_n+1):
                n_values.append(i)
                fib_values.append(self.fib(i))
            yield (n_values, fib_values)
        else:
            yield ([], [])


    def perm(self, _numbers) -> list:
        """
        Return permutation (all possible arrangements) for a given input list.
        - input: [1, 2, 3]
        - output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        """
        # your code
        if _numbers == []:
            return [[]]
        else:
            perms = []
            for i in range(len(_numbers)):
                n = _numbers[i]
                r = _numbers[:i] + _numbers[i+1:]
                for p in self.perm(r):
                    perms.append([n] + p)
            return perms


    def pset(self, _numbers) -> list:
        """
        Return powerset (set of all subsets) for a given input list.
        - input: [1, 2, 3]
        - output: powerset, [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        """
        # your code
        if not _numbers:
            return [[]]
        
        n1 = _numbers[0]
        r = _numbers[1:]
        sub_pset = self.pset(r)
        res = list(sub_pset) 
        for subset in sub_pset:
            res.append([n1] + subset)

        return res


    def find(self, _numbers, match_func) -> list:
        """
        Return list of elements n for which match_func(n) evaluates True.
        """
        # your code
        result = []
        for n in _numbers:
            if match_func(n):
                result.append(n)
        return result


    def find_adjacent(self, pair, _numbers, _i=0) -> list:
        """
        Return list of indexes of adjacent numbers in _numbers.
        """
        # your code
        n = len(_numbers)
        if _i >= n - 1:
            return []
    
        res = []
        if _numbers[_i] == pair[0] and _numbers[_i + 1] == pair[1]:
            res.append(_i)
        
        recursive_results = self.find_adjacent(pair, _numbers, _i + 1)
        res.extend(recursive_results)
        return res


    def find_pairs(self, n: int, _numbers: list) -> list:
        """
        Return list of unique pairs from _numbers that add to n,
        using recursion by slicing the input list.
        
        :param n: The target sum.
        :param _numbers: The list of numbers to search within.
        :return: A list of unique pairs [a, b] where a + b == n.
        """
        if len(_numbers) < 2:
            return []

        pairs = self.find_pairs(n, _numbers[1:])
        current_num = _numbers[0]
        complement = n - current_num

        if complement in _numbers[1:]:
            new_pair = sorted([current_num, complement])
            if new_pair not in pairs:
                pairs.append(new_pair)

        return pairs

    def find_all_sums(self, n: int, _numbers: list) -> list:
        """
        Return all combinations of numbers in _numbers that add to n,
        (any pair, any order, no duplicates).
        """
        nums = sorted(list(set(_numbers)))        
        results = []

        def backtrack(target, start_index, path):
            """
            Return all combinations of numbers in _numbers that add to n,
            (any pair, any order, no duplicates).
            """            
            if target == 0:
                results.append(path[:])
                return
            if target < 0:
                return

            for i in range(start_index, len(nums)):
                current_num = nums[i]
                if current_num > target:
                    break

                path.append(current_num)
                backtrack(target - current_num, i + 1, path)                
                path.pop()

        backtrack(n, 0, [])        
        return results

    def __init__(self, _numbers=numbers):
        """
        Constructor to initialize member variables.
        """
        self.numbers = _numbers

    run_choices = [
        1,      # Challenge 1, Simple recursion: sum numbers
        2,      # Challenge 2, Fibonacci numbers
        21,     # Challenge 2.1, fig_gen()
        22,     # Challenge 2.2, memoization, fib(60), fib(90)
        3,      # Challenge 3, Permutation
        4,      # Challenge 4, Powerset
        5,      # Challenge 5, Finding matches, find()
        51,     # Challenge 5.1, find_adjacent() pairs
        52,     # Challenge 5.2, find_pairs() that add to n
        6,      # Challenge 6, Find all combinations that add to n
        61,     # Challenge 6.1, Find all in medium set
        7       # Challenge 7, Hard problem finding numbers (extra points)
    ]


# Ignore this code that loads solution from file, if exists.
# The solution is not distributed.
try:
    _from, _import = 'recursion_sol', 'Recursion'
    Recursion = getattr(__import__(_from, fromlist=[_import]), _import)
#
except ImportError:
    pass


if __name__ == '__main__':
    """
    Main driver that runs when this file is executed by Python interpreter.
    """
    run_choices = Recursion.run_choices

    numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
    n1 = Recursion(numbers)
    print(f'n1.numbers: {n1.numbers}')

    # Challenge 1, Simple recursion: sum numbers
    if 1 in run_choices:
        s = n1.sum(n1.numbers)
        print(f'sum(n1.numbers): {s}')


    # Challenge 2, Fibonacci numbers
    if 2 in run_choices:
        n = 30
        print(f'\nfib({n}): {n1.fib(n)}')

    # Challenge 2.1, fig_gen()
    if 21 in run_choices:
        gen = n1.fib_gen(20)    # yield generator object
        n, fib = next(gen)      # trigger generator
        print(f'n:      {n}')
        print(f'fib(n): {fib}')

    # Challenge 2.2, memoization, fib(60), fib(90)
    if 22 in run_choices:
        n = 60
        print(f'fib({n}): {n1.fib(n)}')     # ??
        n = 90
        print(f'fib({n}): {n1.fib(n)}')     # ??


    # Challenge 3, Permutation
    if 3 in run_choices:
        lst = [1, 2, 3]
        perm = n1.perm(lst)
        print(f'\nperm({lst}) -> {perm}')


    # Challenge 4, Powerset
    if 4 in run_choices:
        lst = [1, 2, 3]
        pset = n1.pset(lst)
        print(f'\npset({lst}) -> {pset}')


    lst = n1.numbers
    #
    # Challenge 5, Finding matches, find()
    if 5 in run_choices:
        div3 = n1.find(lst, match_func=lambda n : n % 3 == 0)
        print(f'\nfind numbers divisible by 3: {div3}')

    # Challenge 5.1, find_adjacent() pairs
    if 51 in run_choices:
        pair = [4, 8]
        adj = n1.find_adjacent(pair, lst)
        print(f'find_adjacent({pair}, list): {adj}')

    # Challenge 5.2, find_pairs() that add to n
    if 52 in run_choices:
        n = 12
        pairs = n1.find_pairs(n, lst)
        print(f'find_pairs({n}, list) -> {pairs}')


    lst = [8, 10, 2, 14, 4]     # input list
    #
    # Challenge 6, Find all combinations that add to n
    if 6 in run_choices:
        print(f'\nlist: {lst}\n\\\\')
        n = 14
        all = n1.find_all_sums(n, lst)
        print(f'find_all_sums({n}, lst) -> {all}')
        #
        n = 20
        all = n1.find_all_sums(n, lst)
        print(f' - find_all_sums({n}, lst) -> {all}')
        #
        n = 32
        all = n1.find_all_sums(n, lst)
        print(f' - find_all_sums({n}, lst) -> {all}')


    lst = [     # input list
        260, 720, 225, 179, 101, 767, 167, 200, 157, 289,
        318, 303, 153, 290, 201, 594, 457, 607, 592, 246,
    ]
    #
    # Challenge 6.1, Find all in medium set
    if 61 in run_choices:
        print(f'\nlist({len(lst)}): {lst}\n\\\\')
        n = 101 + 201 + 167     # 469 -> [[179, 290], [101, 167, 201]]
        all = n1.find_all_sums(n, lst)
        for i, s in enumerate(all):
            print(f' {i+1:2}: find_all_sums({sum(s)}) -> {s}')


    lst = [     # input list
        260, 720, 225, 179, 101, 767, 167, 200, 157, 289,
        318, 303, 153, 290, 201, 594, 457, 607, 592, 246,
        132, 135, 584, 432, 591, 204, 417, 405, 362, 658,
        136, 751, 583, 536, 293, 493, 431, 780, 563, 703,
        400, 618, 397, 320, 513, 708, 319, 317, 685, 347,
        758, 439, 145, 378, 158, 384, 551, 110, 408, 648,
        847, 498,  50,  19,     # 64 numbers
    ]
    # Challenge 7, Hard problem finding numbers (extra points)
    if 7 in run_choices:
        print(f'\nlist({len(lst)}) with {len(lst)} numbers.\n\\\\')
        n = 101 + 201 + 167     # 469
        all = n1.find_all_sums(n, lst)
        #
        sort_cpm = lambda x, y: -1 if len(x) < len(y) else 1 if len(x) > len(y) else \
            -1 if x <= y else 1 if x > y else 0
        all.sort(key=cmp_to_key(sort_cpm))  # sort by len(solution)
        #
        for i, s in enumerate(all):
            print(f' {i+1:2}: find_all_sums({sum(s)}) -> {s}')
        print()


# #
# n = 899 # 720 + 179, [[720, 179], [260, 179, 157, 303], [167, 289, 153, 290], [289, 153, 457]]
# n = 6240