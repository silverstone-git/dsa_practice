def total_rain_water_capacity(pillars: list[int]):

    water = 0

    forward_trap = 0
    forward_trap_start = 0
    forward = True
    i = 1

    backward_trap = 0
    backward_trap_start = len(pillars) - 1
    j = len(pillars) - 2

    while j > -1 and i < len(pillars):

        # TBD: we have to find a way to not double counting the traps in forward and backward
        # find a way to get the last forward trap high pillar

        # the forward pointer
        if forward and pillars[i] < pillars[forward_trap_start]:
            # underwater case, forward_trap_start counting the water till it hits
            print("going down: ", forward_trap)
            forward_trap += pillars[forward_trap_start] - pillars[i]
            i += 1
            if i > backward_trap_start:
                print("flushing current forward, backward counting again")
                forward_trap = 0
                forward = not forward
                i -= 1

        elif forward:
            # new partition time
            print("forward trapped: ", forward_trap, " at index", i)
            water += forward_trap
            forward_trap_start = i
            forward_trap = 0
            
            i += 1
            if i >= backward_trap_start:
                # this was post-flush corrected trap count, no need to go further
                break

        # the backward pointer
        elif pillars[j] < pillars[backward_trap_start]:
            print("backing up: ", backward_trap)
            backward_trap += pillars[backward_trap_start] - pillars[j]
            j -= 1

            if j < forward_trap_start:
                # while back-counting, we hit the forward pillar
                print("flushing current backward, forward counting again")
                backward_trap = 0
                forward = not forward
                j += 1
        else:
            print("backward_traped: ", backward_trap)
            water += backward_trap
            backward_trap_start = j
            backward_trap = 0

            j -= 1
            if j <= forward_trap_start:
                # this was post-flush corrected trap count, no need to go further
                break
            
        
    return water


if __name__ == "__main__":
    pillars_testcases = [
        # [0,1,0,2,1,0,1,3,2,1,2,1],
        # [4,2,0,3,2,5],
        # [5, 4, 1, 2],
        [2, 4, 1, 5]
    ]
    for pillars in pillars_testcases:
        print(total_rain_water_capacity(pillars))

