#include "types.h"
#include <math.h>

double average(times_t times, size_t n)
{
    int sum = 0;
    for (size_t i = 0; i < n; i++)
        sum += (int) times[i];
    return (double) sum / (int) n;
}

double variance(times_t times, size_t n, double average)
{
    double s_2 = 0.0;
    for (size_t i = 0; i < n; i++)
        s_2 += ((double) times[i] - average) * ((double) times[i] - average);
    return s_2 / (int) (n - 1);
}

double std_deviation(double variance)
{
    return sqrt(variance);
}

double std_error(double std_deviation, size_t n)
{
    return std_deviation / sqrt((double) n);
}

double rse(times_t times, size_t n)
{
    double t_avg = average(times, n);

    double s_2 = variance(times, n, t_avg);

    double s = std_deviation(s_2);

    double std_err = std_error(s, n);

    return std_err / t_avg * 100;
}