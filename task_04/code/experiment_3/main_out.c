#include "../types.h"
#include <stdio.h>
#include <time.h>

void selection_sort(int *p, size_t length);
void init(array_t arr, size_t length);
unsigned long long calc_elapsed_time(const struct timespec *beg, const struct timespec *end);

int main(void)
{
    struct timespec t_beg, t_end;

    array_t array;
    size_t n_array = N;
    init(array, n_array);

    int *p = array;

    clock_gettime(CLOCK_MONOTONIC_RAW, &t_beg);
    selection_sort(p, n_array);
    clock_gettime(CLOCK_MONOTONIC_RAW, &t_end);

    long long time = (long long) calc_elapsed_time(&t_beg, &t_end);
    printf("%d %lld\n", N, time);

    return 0;
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

void selection_sort(int *p, size_t length)
{
    size_t min_element;

    for (size_t i = 0; i < length; i++)
    {
        min_element = i;
        for (size_t j = i + 1; j < length; j++)
            if (*(p + j) < *(p + min_element))
                min_element = j;

        int temp = *(p + i);
        *(p + i) = *(p + min_element);
        *(p + min_element) = temp;
    }
}
