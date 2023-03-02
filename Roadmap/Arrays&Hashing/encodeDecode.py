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

    def decode(self, s):
