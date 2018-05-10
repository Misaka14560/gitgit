print('\n'.join([
    '\t'.join(['%d * %d = %d' % (y, x, x * y) for y in range(1, x + 1)])
    for x in range(1, 10)
]))
print(list(range(10)))
print("\n".join([
    "\t".join(["%d *%d = %d " % (a, a, a * a) for a in range(1, x + 1)])
    for x in range(1, 10)
]))
