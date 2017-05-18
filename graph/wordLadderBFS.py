def ladderLeng(beg, end, wordList):
    begSet = set()
    endSet = set()
    leng, strLen = 1, len(beg)
    visited = set()
    begSet.add(beg)
    endSet.add(end)

    while begSet and endSet:
        if len(begSet) > len(endSet):
            begSet, endSet = endSet, begSet

        temp = set()
        for word in begSet:
            chs = list(word)
            for i in range(len(chs)):
                # a to z generate
                for c in [chr(i+ord('a')) for i in range(26)]:
                    old = chs[i]
                    chs[i] = c
                    target = ''.join(chs)

                    if endSet.contains(target): return leng+1
                    if target not in visited and target in wordList:
                        temp.add(target)
                        visited.add(target)
                    chs[i] = old
        begSet = temp
        leng += 1

    return 0
