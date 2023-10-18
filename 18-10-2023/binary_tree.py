class Solution:
    def is_binary_tree_true(self, current, child_left, child_right, visited):
        if child_left[current] != -1:
            if visited[child_left[current]]:
                return False
            visited[child_left[current]] = True
            if not self.is_binary_tree_true(child_left[current], child_left, child_right, visited):
                return False

        if child_right[current] != -1:
            if visited[child_right[current]]:
                return False
            visited[child_right[current]] = True
            if not self.is_binary_tree_true(child_right[current], child_left, child_right, visited):
                return False

        return True

    def validateBinaryTreeNodes(self, n, left_child, child_right):
        child_count = [False] * n

        for child in left_child:
            if child != -1:
                child_count[child] = True

        for child in child_right:
            if child != -1:
                if child_count[child]:
                    return False
                child_count[child] = True

        root = -1
        for i in range(n):
            if not child_count[i]:
                if root == -1:
                    root = i
                else:
                    return False

        if root == -1:
            return False

        visited = [False] * n
        visited[root] = True
        if not self.is_binary_tree_true(root, left_child, child_right, visited):
            return False

        for visit in visited:
            if not visit:
                return False

        return True
