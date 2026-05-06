def job_scheduling(jobs, t):
    # Step 1: Sort jobs by profit (descending)
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Step 2: Initialize result slots
    slots = [False] * t   # track free/occupied slots
    result = ['-1'] * t   # store job IDs

    total_profit = 0

    # Step 3: Assign jobs greedily
    for job in jobs:
        job_id, deadline, profit = job

        # Find a free slot before deadline
        for j in range(min(t - 1, deadline - 1), -1, -1):
            if not slots[j]:
                slots[j] = True
                result[j] = job_id
                total_profit += profit
                break

    print("Scheduled Jobs:", result)
    print("Total Profit:", total_profit)


# Example input
jobs = [
    ['a', 2, 100],
    ['b', 1, 19],
    ['c', 2, 27],
    ['d', 1, 25],
    ['e', 3, 15]
]

job_scheduling(jobs, 3)