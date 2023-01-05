class Solution:
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        rows = [[1], [1, 1]]

        for x in range(numRows - 2):
            next_row = [1]
            for index in range(1, x + 2):
                previous_row = rows[-1]
                next_value = previous_row[index - 1] + previous_row[index]
                next_row.append(next_value)

            next_row.append(1)
            rows.append(next_row)


        return rows















if __name__ == "__main__":
   solution = Solution()
   print(solution.generate(5))
