def solve(s):
    t=s.split()
    for i in t:
        s=s.replace(i,i.capitalize())
    return s

print(solve('   rajeev    ranjan   123d'))