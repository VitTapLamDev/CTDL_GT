def generate_combinations(n, k):
    def backtrack(current_combination, used):
        if len(current_combination) == k:
            print(' '.join(map(str, current_combination)))
            return
        for i in range(1, n + 1):
            if not used[i]:
                used[i] = True
                current_combination.append(i)
                backtrack(current_combination, used)
                current_combination.pop()
                used[i] = False

    used = [False] * (n + 1)
    backtrack([], used)

n, k = map(int, input().split())
generate_combinations(n, k)
