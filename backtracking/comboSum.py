#!/usr/bin/python
"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.  
The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]
#39
REDDO: good question to redo. DP is actually slower. Also redo backtracking
"""
ml = []
def comboSum(t, d, r):
    """
    No idea why this beats 85.12% of python solution.
    """
    if t == 0:
        ml.append(r)

    for itm in d:
        if itm <= t and (not r or itm >= r[-1]):
            new_r = r[:]
            new_r.append(itm)
            comboSum(t-itm, d, new_r)

def comboSum_bt(t, cand):
    """
    Back tracking this is the slowest. 30% performance. Double check time-complex: O(n!)
    """
    rslt = []
    cand.sort() # must be in ascending order
    dfs(t, 0, [], cand, rslt)
    return rslt

def dfs(t, i, path, cand, rslt):
    if t < 0: return
    if t == 0:
        rslt.append(path)
        return

    for idx, itm in enumerate(cand[i:], start=i):
        dfs(t-itm, idx, path+[itm], cand, rslt)

def comboSum_r(sum, nums):
    res = []
    trace = []
    nums.sort() # need for ln 68 - 71
    dfs_r(nums, 0, trace, 0, sum, res)

    return res

def dfs_r(nums, i, trace, partial_sum, sum, res):
    if partial_sum >= sum:
        if partial_sum == sum: res.append(list(trace))
        return

    for n_i in range(i, len(nums)):
        trace.append(nums[n_i])
        partial_sum += nums[n_i]
        dfs_r(nums, n_i, trace, partial_sum, sum, res)

        # for this to work you need to sort the input array
        if partial_sum >= sum:
            trace.pop()
            break
        partial_sum -= nums[n_i]
        trace.pop()

def comboSum_dp(t, d):
    """
    dp sol, similar to knapsack
    """
    m = [[None]*(t+1)]*(len(d)+1)
    rslt = [x[:] for x in m]
    for d_idx in range(len(d)+1): rslt[d_idx][0] = [[]]
    for t_idx in range(t+1): rslt[0][t_idx] = []

    for d_idx, d_val in enumerate(d, start=1):
        for i in range(1, t+1):
            rslt[d_idx][i] = []
            for t_l in rslt[d_idx-1][i]:
                rslt[d_idx][i].append(t_l)

            rem = i-d_val
            if rem < 0 or not rslt[d_idx][rem]: continue
            for e_l in rslt[d_idx][rem]:
                new_l = list(e_l)
                new_l.append(d_val)
                rslt[d_idx][i].append(new_l)

    return rslt[len(d)][t]

def comboSum_dp2(t, d):
    """
    More concise, solution from lc. Understood and solved on my own.
    97.3% performance. has to sort first
    """
    rslt = []
    d.sort()
    for i in range(1,t+1):
        i_l = []
        for c_val in d:
            if c_val > i:
                break
            if c_val == i:
                i_l.append([c_val])
            else:
                prev_idx = i-c_val-1
                if prev_idx >= 0:
                    for l in rslt[prev_idx]:
                        if c_val >= l[-1]:
                            temp_l = l[:]
                            temp_l.append(c_val)
                            i_l.append(temp_l)
        rslt.append(i_l)

    return rslt[-1]


def test1():
    t = 7
    d = [2, 3, 6, 7]
    r = []
    #comboSum(t, d, r)
    #print(ml)
    print(comboSum_dp2(t, d))
    print(comboSum_bt(t, d))
    print(comboSum_r(t, d))
    print('----------------')

def test2():
    t = 10
    d = [2, 3, 6, 7]
    r = []
    #comboSum(t, d, r)
    #print(ml)
    print(comboSum_dp2(t, d))
    print(comboSum_bt(t, d))
    print(comboSum_r(t, d))
    print('----------------')

def test3():
    t = 1
    d = [1, 2]
    print(comboSum_dp2(t, d))
    print(comboSum_bt(t, d))
    print(comboSum_r(t, d))
    print('----------------')

def test4():
    t = 11
    d = [8, 4, 3, 7]
    print(comboSum_dp2(t, d))
    print(comboSum_bt(t, d))
    print(comboSum_r(t, d))
    print('----------------')

def test5():
    t = 10
    d = [8, 2]
    print(comboSum_dp2(t, d))
    print(comboSum_bt(t, d))
    print(comboSum_r(t, d))
    print('----------------')

def test6():
    t = 11
    d = [8, 7, 4, 3]
    print(comboSum_dp2(t, d))
    print(comboSum_bt(t, d))
    print(comboSum_r(t, d))
    print('----------------')

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
