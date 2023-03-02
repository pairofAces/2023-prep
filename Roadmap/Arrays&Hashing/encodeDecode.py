class Solution:
    '''
    @params: strs: a list of strings
    @return: encodes a list of strings to a single string
    '''

    def encode(self, strs):
        # create a results variable, as an empty string
        result = ''

        # iterate over each string (s) in the list of strings (strs)
        for s in strs:

            # append the string along with other characters, example
            # str(len(s)) will provide a number, converted to a string, and append it
            # to the result string.
            # adding the "#" symbol into the string
            # then adding the actual string the current loop is in
            result += str(len(s)) + "#" + s
        return result

    '''
    @param: s: a string
    @return decodes a single string to a list of strings
    '''
    def decode(self, s):
        result, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return result

solution = Solution()

strs = ["leet","code","loves","you"]

test1 = solution.encode(strs)
print(test1)

s = "4#leet4#code5#loves3#you"

test2 = solution.decode(s)
print(test2)
