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

comm = MPI.COMM_WORLD
size = comm.Get_size()
#assert size > 1
if size < 2:
    print("WARNING: LESS THAN TWO NODES")
rank = comm.Get_rank()

if rank == 0:
    print(f"math.pi={math.pi}")

"""Calculate pi on each node
pi = 0
for i in range(1, N+1):
    pi += term(i, N)
pi *= 4

print(f"Hello world from {rank+1} of {size}: pi={pi}")
"""

MPI.COMM_WORLD.Barrier()
start_time = MPI.Wtime()

def batch_range(start, end, rank=rank, size=size):
    N = end - start
    batch_size = N // size
    batch_left_over = N - size * batch_size
    adjustment = batch_left_over if rank == size - 1 else 0
    left = start + rank * batch_size
    # if rank == 1:
    #     print(f"rank={rank}; batch_size={batch_size}; batch_left_over={batch_left_over}; left={left}; adjustment={adjustment}")
    return range(left, left + batch_size + adjustment)

def calc_pi(N):
    """Calculate pi on each node"""
#    batch_size = N // size
#    batch_left_over = N - size * batch_size
#    # if rank == 0:
#    #     print(f"batch_size={batch_size}; batch_left_over={batch_left_over}")

    pi_partial = 0
    # NB i = j + 1 + rank * batch_size
#    for j in range(0, batch_size + (batch_left_over if rank == size - 1 else 0)):
#       i = rank * batch_size + j + 1
    for i in batch_range(1, N+1):
        pi_partial += term(i, N)

    # except rank 0: send pi_partial to rank 0
    # rank 0: receive pi_partial from other ranks
    pi_partials = comm.gather(pi_partial, root=0)

    # rank 0: sum pi_partial, and multiply by 4, and print
    # other ranks: no actions
    if rank == 0:
        pi = 4 * sum(pi_partials)
        return pi
    else:
        return None

for k in range(5):
    pi = None
    for x in range(4):
        pi = calc_pi(N * 10**k)
    if rank == 0:
        print(f"     pi={pi}")
        lgerr = math.log2(abs(pi - math.pi))
        print(f"  log2(error)={lgerr} @ N={N * 10**k}")

MPI.COMM_WORLD.Barrier()
end_time = MPI.Wtime() - start_time
end_times = comm.gather(end_time, root=0)
if rank == 0:
    print(f"end_time={end_time}")
    print(f"end_times={end_times}")
