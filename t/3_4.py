#  Implement Greedy search algorithm for Job Scheduling Problem

# Job structure: (id, deadline, profit)

def job_scheduling(jobs):
    # Sort jobs by profit (descending)
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find maximum deadline
    max_deadline = max(job[1] for job in jobs)

    # Initialize time slots
    slots = [None] * max_deadline

    total_profit = 0

    # Iterate through jobs
    for job in jobs:
        job_id, deadline, profit = job

        # Find a free slot (latest possible)
        for i in range(min(deadline, max_deadline) - 1, -1, -1):
            if slots[i] is None:
                slots[i] = job_id
                total_profit += profit
                break

    return slots, total_profit


# ---------------- Main ----------------
jobs = [
    ('J1', 2, 100),
    ('J2', 1, 19),
    ('J3', 2, 27),
    ('J4', 1, 25),
    ('J5', 3, 15)
]

schedule, profit = job_scheduling(jobs)

print("Job Schedule:", schedule)
print("Total Profit:", profit)


## output
# Job Schedule: ['J3', 'J1', 'J5']
# Total Profit: 142