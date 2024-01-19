def print_job_schedule(arr, t):
    arr.sort(key=lambda x: x[2], reverse=True)
    job = ['-1'] * t

    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if job[j] == '-1':
                job[j] = arr[i][0]
                break

    print("Maximum profit sequence of jobs:")
    print(job)

jobs = [
    ['a', 7, 202],
    ['b', 5, 29],
    ['c', 6, 84],
    ['d', 1, 75],
    ['e', 2, 43]
]

print_job_schedule(jobs, 3)
