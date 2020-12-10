def restoreIpAddresses(s):
    res = []
    segments = []

    def isValid(digits):
        if len(digits) > 1 and digits[0] == "0":
            return False
        if int(digits) < 0 or int(digits) > 255:
            return False
        return True

    def backtrack(lastPoint, remainingPoints):
        if remainingPoints == 0:
            if lastPoint == len(s):
                res.append(".".join(segments))
            return
        for currPoint in range(lastPoint + 1, lastPoint + 4):
            if currPoint > len(s):
                break
            if isValid(s[lastPoint:currPoint]):
                segments.append(s[lastPoint:currPoint])
                backtrack(currPoint, remainingPoints - 1)
                segments.pop()

    backtrack(0, 4)
    return res


s = "25525511135"
print(restoreIpAddresses(s))
