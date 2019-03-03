class Solution:
    @staticmethod
    def search_matrix(matrix, target):
        return Solution.upper_right_solution(matrix, target)
        pass

    @staticmethod
    def simple_solution(matrix, target):
        for row in matrix:
            for item in row:
                if item == target:
                    return True
        return False

    @staticmethod
    def upper_right_solution(matrix, target):
        """
        右上角元素为这一行最大，这一列最小，判断其与target大小
        等于则返回，大于则删除此列，小于则删除此行
        """
        row_index = 0
        row_num = len(matrix)
        if row_num == 0:
            return False
        column_index = len(matrix[0]) - 1
        while row_index < row_num and column_index >= 0:
            if matrix[row_index][column_index] == target:
                return True
            elif matrix[row_index][column_index] > target:
                column_index -= 1
            else:
                row_index += 1
        return False


if __name__ == '__main__':
    m = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    t = 5
    print(Solution.search_matrix(m, t))
