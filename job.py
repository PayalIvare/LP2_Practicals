def job_scheduling(jobs, n):
    jobs.sort(key=lambda x: x[1], reverse=True)
    result = [False] * n
    job_sequence = ['-1'] * n

    for job in jobs:
        for j in range(min(n-1, job[2]-1), -1, -1):
            if not result[j]:
                result[j] = True
                job_sequence[j] = job[0]
                break

    return job_sequence

jobs = [('a', 100, 2), ('b', 19, 1), ('c', 27, 2), ('d', 25, 1), ('e', 15, 3)]
print("Job sequence:", job_scheduling(jobs, 3))


"""
def job_scheduling(jobs, n):
    # Sort jobs by profit in decreasing order
    jobs.sort(key=lambda x: x[1], reverse=True)

    # Initialize the result array (time slots) and job sequence
    result = [False] * n
    job_sequence = ['-1'] * n

    # Iterate through each job
    for job in jobs:
        # Check available time slots from job's last possible time slot to the first
        for j in range(min(n-1, job[2]-1), -1, -1):
            if not result[j]:
                result[j] = True  # Mark the slot as filled
                job_sequence[j] = job[0]  # Assign the job to that time slot
                break

    return job_sequence

def dynamic_job_scheduling():
    try:
        # Get number of time slots
        n = int(input("Enter the number of time slots: "))
        
        # Get the number of jobs
        m = int(input("Enter the number of jobs: "))
        
        jobs = []
        
        # Get job details (job name, profit, and deadline)
        for i in range(m):
            job_details = input(f"Enter details for job {i+1} (name profit deadline): ").split()
            job_name = job_details[0]
            profit = int(job_details[1])
            deadline = int(job_details[2])
            jobs.append((job_name, profit, deadline))

        # Get the job schedule
        job_sequence = job_scheduling(jobs, n)
        
        # Print the job sequence
        print("Job sequence:", job_sequence)
        
    except ValueError:
        print("Invalid input. Please enter valid integers for profit and deadline.")

# Call the dynamic job scheduling function
dynamic_job_scheduling()


Enter the number of time slots: 3
Enter the number of jobs: 5
Enter details for job 1 (name profit deadline): a 100 2
Enter details for job 2 (name profit deadline): b 19 1
Enter details for job 3 (name profit deadline): c 27 2
Enter details for job 4 (name profit deadline): d 25 1
Enter details for job 5 (name profit deadline): e 15 3


"""