#!bash

set -e -x

exec mpiexec -n 10 python -m mpi4py calc_pi.py