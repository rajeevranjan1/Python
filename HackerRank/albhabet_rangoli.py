n=3
chars=[i for i in map(chr,range(ord('a'),(ord('z')+1)))]
l = []
for i in range(n):
    s = "-".join(chars[i:n])
    l.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(l[:0:-1]+l))

# # s='-'.join(chars[0:3])
# # print(s[::-1])
print(l[:0:-1]+l)
print(chars[n-1].center(9,'-'))