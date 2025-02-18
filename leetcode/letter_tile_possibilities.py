class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seq = set()
        used = [False] * len(tiles)

        def generateSeq(current):
            seq.add(current)

            for i in range(len(tiles)):
                if not used[i]:
                    used[i] = True

                    generateSeq(current + tiles[i])

                    used[i] = False

        generateSeq('')

        return len(seq) - 1

sol=Solution()
print(sol.numTilePossibilities('AAB'))
print(sol.numTilePossibilities('AAABBC'))
print(sol.numTilePossibilities('A'))