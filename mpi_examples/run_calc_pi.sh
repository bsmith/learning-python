#!bash

set -e -x

NPROCS=${NPROCS:-10}

exec mpiexec -n $NPROCS python -m mpi4py calc_pi.py