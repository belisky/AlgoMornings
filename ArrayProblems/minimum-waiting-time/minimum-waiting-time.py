def minimumWaitingTime(queries):
    sum_total = 0
    sums = []
    queries = sorted(queries)

    for i in range(len(queries) - 1):
        sum_total += queries[i]         
        sums.append(sum_total)

    return sum(sums)