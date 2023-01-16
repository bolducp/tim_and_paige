def climbStairs(n: int) -> int:
#if there's 1 step: there's just 1 option: 1
#2 steps: two option: 1,1 or 2
#3 steps: three options: 1,1,1 or 2,1 or 1,2
#4 steps: five options: 2,2; 1,1,1,1; 1,2,1; 1,1,2; 2,1,1
#5 steps: eight options: 1,1,1,1,1; 1,1,1,2; 1,1,2,1; 1,2,1,1; 2,1,1,1,; 2,2,1; 2,1,2; 1,2,2
#6 steps: thirteen options: 1,1,1,1,1,1;
#1,1,1,1,2; 2,1,1,1,1; 1,2,1,1,1; 1,1,2,1,1; 1,1,1,2,1;
#2,2,2;
#2,2,1,1; 2,1,2,1; 2,1,1,2; 1,1,2,2; 1,2,2,1, 1,2,1,2
    if n == 0:
        return 0
    if n == 1:
        return 1


    step_options = [1, 1]
    for step in range(2, n+1):
        previous_step = step_options[-1]
        previous_previous_step = step_options[-2]
        step_options.append(previous_step + previous_previous_step)

    return step_options[-1]
