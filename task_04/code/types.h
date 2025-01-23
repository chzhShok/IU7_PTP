#ifndef TYPES_H
#define TYPES_H

#include <stdlib.h>

#ifndef N
#error Define N
#endif

#ifndef N_REPS
#define N_REPS 20
#endif

typedef int array_t[N];
typedef long long times_t[N];

double rse(times_t times, size_t n);
double average(times_t times, size_t n);

#endif // TYPES_H
