class Solutions:
    def encode(self, strs: List[str]) -> str:
        encoded_word = "" 

        for word in strs:
           encoded_word += (str(len(word)) + "#" + word) 

        return encoded_word

    def decode(self, s: str) -> List[str]:
        i = 0
        res = list()

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            res.append(s[(j+1) : (j+1+length)])
            i = j + 1 + length


        return res
