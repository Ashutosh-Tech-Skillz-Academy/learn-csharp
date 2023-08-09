def perform_work(A, M, B):
    # Initialize a list to represent the schedule for each day
    schedule = [0] * (A + 1)

    # Sort the work descriptions based on the deadline day (B[i][1])
    sorted_work = sorted(B, key=lambda x: x[1])

    # Iterate through each work description
    for work in sorted_work:
        work_day, deadline_day, days_to_complete = work

        # Check if it's possible to complete the work before the deadline
        if work_day + days_to_complete - 1 > deadline_day:
            return [-1]

        # Find the earliest available day to start this work
        start_day = max(work_day, schedule.index(0, work_day, deadline_day + 1))

        # Update the schedule for the work days
        for day in range(start_day, start_day + days_to_complete):
            if day <= A:
                schedule[day] = sorted_work.index(work) + 1

        # Set the deadline day in the schedule
        if deadline_day <= A:
            schedule[deadline_day] = M + 1

    return [-1] if 0 in schedule[1:] else schedule[1:]

# Example usage:
A = 3
M = 1
B = [[1, 2, 2]]
result = perform_work(A, M, B)
print(result)
