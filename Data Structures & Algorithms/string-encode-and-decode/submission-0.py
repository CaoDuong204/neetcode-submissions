class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for word in strs:
            encoded = encoded + str(len(word)) + "#" + word

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            length = ''

            while s[i] != '#':
                length = length + s[i]
                i += 1

            i += 1
            length = int(length)
            word = s[i:i + length]
            result.append(word)
            i += length

        return result