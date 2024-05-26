def generate_permutations(n):
    def backtrack(current_permutation, used):
        # Nếu độ dài của current_permutation bằng n, ta đã có một hoán vị hoàn chỉnh
        if len(current_permutation) == n:
            print(' '.join(map(str, current_permutation)))
            return
        # Thử tất cả các số từ n đến 1
        for i in range(n, 0, -1):
            if not used[i]:
                # Đánh dấu số i là đã sử dụng
                used[i] = True
                # Thêm i vào hoán vị hiện tại
                current_permutation.append(i)
                # Gọi đệ quy để tiếp tục xây dựng hoán vị
                backtrack(current_permutation, used)
                # Loại bỏ i khỏi hoán vị hiện tại và đánh dấu nó là chưa sử dụng
                current_permutation.pop()
                used[i] = False

    # Khởi tạo danh sách trạng thái sử dụng cho các số từ 1 đến n
    used = [False] * (n + 1)
    # Bắt đầu quay lui với hoán vị rỗng
    backtrack([], used)


n = int(input())
generate_permutations(n)
