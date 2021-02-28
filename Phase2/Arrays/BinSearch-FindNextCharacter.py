"""
744. Find Smallest Letter Greater Than Target
"""
def nextGreatestLetter(letters, target):
    left,right=0,len(letters)-1
    while left<right:
        mid = left+(right-left)//2
        if letters[mid]<=target:
            left=mid+1
        else:
            right=mid
    return letters[left%len(letters)]

letters = ["c", "f", "j"]
target = "c"
print(nextGreatestLetter(letters,target))