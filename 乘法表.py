# print('\n'.join([
#     ' '.join(['%s*%s=%-2s' % (j, i, i * j) for j in range(1, i + 1)])
#     for i in range(1, 10)
# ]))
print('\n'.join([
    " ".join(["%s*%s=%2s" % (i, j, j * i) for i in range(1, j+1)])
    for j in range(1, 10)
]
)
)
