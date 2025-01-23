import glob
import os
from math import floor, ceil

data_path = 'data'
preproc_path = 'preproc_data'

txt_files = glob.glob(os.path.join(data_path, '*.txt'))


def calc_values(array: list[float]) -> tuple[float, float, float, float, float, float]:
    array.sort()
    count: int = len(array)
    avg: float = sum(array) / count
    median: float = array[count // 2 + 1] if count % 2 == 1 else (array[count // 2] + array[count // 2 + 1]) / 2
    maxi: float = max(array)
    mini: float = min(array)
    q1: float = array[int(0.25 * (count + 1))] if floor(0.25 * (count + 1)) == ceil(0.25 * (count + 1)) \
        else (array[floor(0.25 * (count + 1))] + array[ceil(0.25 * (count + 1))]) / 2
    q3: float = array[int(0.75 * (count + 1))] if floor(0.75 * (count + 1)) == ceil(0.75 * (count + 1)) \
        else (array[floor(0.75 * (count + 1))] + array[ceil(0.75 * (count + 1))]) / 2

    return avg, median, maxi, mini, q1, q3


for file in txt_files:
    experiment_ind = (file.split('/')[1].split('_')[1])
    file_ind = (file.split('/')[1].split('_')[2].split('.')[0])
    out_file_path: str = os.path.join(preproc_path, f'preproc_data_{experiment_ind}_{file_ind}.txt')

    with (open(file, 'r') as f_in, open(out_file_path, 'w') as f_out):
        f_out.write('N AVG MEDIAN MAXI MINI Q1 Q3 RSE REPS\n')

        times: list[tuple[int, float, float, int]] = []
        for line in f_in.readlines():
            n: int = int(line.split()[0])
            time: float = float(line.split()[1]) / 1000
            rse: float = float(line.split()[2])
            reps: int = int(line.split()[3])
            times.append((n, time, rse, reps))

        times.sort()

        n_now: int = times[0][0]
        rse_now: float = times[0][2]
        reps_now: int = times[0][3]
        values: list[float] = [times[0][1]]
        for i in range(1, len(times)):
            cur = times[i]
            if cur[0] == n_now:
                values.append(times[i][1])
            else:
                avg, median, maxi, mini, q1, q3 = calc_values(values)

                f_out.write(f'{n_now} {avg:.2f} {median} {maxi} {mini} {q1} {q3} {rse_now} {reps_now}\n')

                n_now = times[i][0]
                values = [times[i][1]]

        if len(values) != 0:
            avg, median, maxi, mini, q1, q3 = calc_values(values)

            f_out.write(f'{n_now} {avg:.2f} {median} {maxi} {mini} {q1} {q3} {rse_now} {reps_now}\n')
