def generate_combinations(n, k):
    def backtrack(start, current_combination):
        if len(current_combination) == k:
            print(' '.join(map(str, current_combination)))
            return
        for i in range(start, n + 1):
            current_combination.append(i)
            backtrack(i + 1, current_combination)
            current_combination.pop()

    backtrack(1, [])

n, k = map(int, input().split())
generate_combinations(n, k)
