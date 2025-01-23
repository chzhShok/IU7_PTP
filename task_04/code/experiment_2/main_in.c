#include "../types.h"
#include <stdio.h>
#include <time.h>

void selection_sort(array_t arr, size_t length);
void init(array_t arr, size_t length);
unsigned long long calc_elapsed_time(const struct timespec *beg, const struct timespec *end);
void print(times_t arr, size_t n, int n_array, double rse, int count);

times_t times;
size_t n_times = 0;

int main(void)
{
    struct timespec t_beg, t_end;
    double rse_metric = 100.0;
    int count = 0;

    while (rse_metric > 1.0)
    {
        count += N_REPS;
        for (int i = 0; i < N_REPS; i++)
        {
            array_t array;
            size_t n_array = N;
            init(array, n_array);

            clock_gettime(CLOCK_MONOTONIC_RAW, &t_beg);
            selection_sort(array, n_array);
            clock_gettime(CLOCK_MONOTONIC_RAW, &t_end);

            long long time = (long long) calc_elapsed_time(&t_beg, &t_end);

            times[n_times++] = time;
        }

        rse_metric = rse(times, n_times);
    }

    print(times, n_times, N, rse_metric, count);

    return 0;
}

void print(times_t arr, size_t n, int n_array, double rse, int count)
{
    for (size_t i = 0; i < n; i++)
        printf("%d %lld %lf %d\n", n_array, arr[i], rse, count);
}

unsigned long long calc_elapsed_time(const struct timespec *beg, const struct timespec *end)
{
    return ((unsigned long long) (end->tv_sec - beg->tv_sec) * 1000 * 1000 * 1000 +
            (end->tv_nsec - beg->tv_nsec)) /
           1000;
}

void init(array_t arr, size_t length)
{
    for (size_t i = 0; i < length; i++)
        arr[i] = length - i;
}

void selection_sort(array_t arr, size_t length)
{
    size_t min_element;

    for (size_t i = 0; i < length; i++)
    {
        min_element = i;
        for (size_t j = i + 1; j < length; j++)
            if (*(arr + j) < *(arr + min_element))
                min_element = j;

        int temp;
        temp = *(arr + i);
        *(arr + i) = *(arr + min_element);
        *(arr + min_element) = temp;
    }
}