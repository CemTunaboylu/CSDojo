# Given 2 lists of integers, find the closest sum to target of two integers one each from a list.

def near_sum(a, b, target):
        a.sort() # O(a log a )
        b.sort() # O(b log b )
        i,j = 0, len(b)-1
        closest = a[0] + b[-1] 
        pair = (a[0] , b[-1])
        while i < len(a) and j>=0:
                s = a[i] + b[j]
                if s == target:
                        return s, (a[i], b[j])
                dif_clo = abs(target-closest)
                dif_s = abs(target-s)
                if dif_s < dif_clo:
                        closest = s
                        pair = ( a[i], b[j] )
                if s < target:
                        i += 1
                else:
                        j -= 1
                        
        return closest, pair

def test(a = [-1, 3, 8, 2, 9, 5], b = [4, 1, 2, 10, 5, 20], t=24, r = [23,25]):
        c,p = near_sum(a,b,t)
        print(f"Closest sum to {t} is {c} w/ pair {p}")
        if isinstance(r, list): assert (c in r)
        else: (c == r)

def test_long():
        from random import randint, seed
        seed(0)
        r = 100_000
        L = 1_000_000
        a = [ randint(-L, L) for _ in range(r)  ]
        b = [ randint(-L, L) for _ in range(r*2)  ]
        t = 204
        c,p = near_sum(a,b,t)
        print(f"Closest sum to {t} is {c} w/ pair {p}")
        assert c == t




test()
test([7, 4, 1, 10], [4, 5, 8, 7], 13, [12,14])
test( [6, 8, -1, -8, -3], [4, -6, 2, 9, -3], 3, 3)
test( [19, 14, 6, 11, -16, 14, -16, -9, 16, 13], [13, 9, -15, -2, -18, 16, 17, 2, -11, -7], -15, [-14, -16])
test_long()

