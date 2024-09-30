def format_duration(seconds):
    if seconds == 0: return "now"

    conversion = {"years": 31536000, "days": 86400, "hours": 3600,"minutes": 60}
    final = {"years": 0, "days": 0, "hours": 0,"minutes": 0, "seconds":0}
    while seconds > 60:
        to_divide = seconds
        for x in conversion:
            if seconds >= conversion[x]:
                seconds = seconds%conversion[x]
                final[x] = round((to_divide-seconds)/conversion[x])
                break
    final["seconds"] = seconds
    final_str = ""
    for y in final:
        if final[y]==1:
            final_str += str(final[y]) + " " + y[:-1] + ", "
        if final[y]>1:
            final_str += str(final[y])+ " " + y + ", "
    adding_and = final_str[:-2].split(",")
    
    
    if len(adding_and) == 1: return adding_and[0]
    return ",".join(adding_and[:-1]) + " and" + adding_and[-1]