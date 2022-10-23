#!python3
"""Calculate a value for pi in parallel

This based on exercise 2 in [Henty2017].

[Henty2017] "Exercises: Message-Passing Programming", David Henty
    https://www.archer.ac.uk/training/course-material/2017/09/mpi-york/exercises/MPP-exercises.pdf
"""

import math
from mpi4py import MPI

# divisible by 2, 3, 4, 5, 6, 7 and 8!
N = 840

# \frac{\pi}{4} == \frac{1}{N} \sum_{i=1}^N term(i, N)
# term(i, N) = \frac{1}{1 + ((i-0.5)/N)^2}
def term(i, N):
    return (1 / N) * 1 / (1 + ((i - 0.5)/N)**2)

size = MPI.COMM_WORLD.Get_size()
assert size > 1
rank = MPI.COMM_WORLD.Get_rank()

pi = 0
for i in range(1, N+1):
    pi += term(i, N)
pi *= 4

if rank == 0:
    print(f"math.pi={math.pi}")

print(f"Hello world from {rank+1} of {size}: pi={pi}")
