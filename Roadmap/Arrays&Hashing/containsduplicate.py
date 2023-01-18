# function takes List as a parameter -> nums List
def containsDuplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False