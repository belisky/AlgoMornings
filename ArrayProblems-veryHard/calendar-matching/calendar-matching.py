def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    updatedCalendar1=updateCalendar(calendar1,dailyBounds1)
    updatedCalendar2=updateCalendar(calendar2,dailyBounds2)
    mergedCalendar=mergeCalendars(updatedCalendar1,updatedCalendar2)
    flattenedCalendar=flattenCalendar(mergedCalendar)
    return getAvail(flattenedCalendar,meetingDuration)
 
def getAvail(calendar,meetingDuration):
    matchingAvail=[]
    for i in range(1,len(calendar)):
        start=calendar[i-1][1]
        end=calendar[i][0]
        availabilityDur=end-start
        if availabilityDur>=meetingDuration:
            matchingAvail.append([start,end])
    return list(map(lambda m:[minToTime(m[0]),minToTime(m[1])],matchingAvail))
def minToTime(min):
    hrs=min//60
    mins=min%60
    hrsStr=str(hrs)
    minStr="0"+str(mins) if mins<10 else str(mins)
    return hrsStr+":"+minStr
def flattenCalendar(calendar):
    flattened=[calendar[0][:]]
    for i in range(1,len(calendar)):
        curMeeting=calendar[i]
        prevMeeting=flattened[-1]
        curStart,curEnd=curMeeting
        prevStart,prevEnd=prevMeeting
        if prevEnd>=curStart:
            newPrev=[prevStart,max(prevEnd,curEnd)]
            flattened[-1]=newPrev
        else:
            flattened.append(curMeeting[:])
    return flattened

def updateCalendar(calendar,dailyBounds):
    updatedCalendar=calendar[:]
    updatedCalendar.insert(0,["0:00",dailyBounds[0]])
    updatedCalendar.append([dailyBounds[1],"23:59"])
    return list(map(lambda m:[timeToMin(m[0]),timeToMin(m[1])],updatedCalendar))
def timeToMin(time):
    hrs,min=list(map(int,time.split(":")))
    return hrs*60+min
def mergeCalendars(calendar1,calendar2):
    merged=[]
    i,j=0,0
    while i<len(calendar1) and j<len(calendar2):
        meeting1,meeting2=calendar1[i],calendar2[j]
        if meeting1[0]<meeting2[0]:
            merged.append(meeting1)
            i+=1
        else:
            merged.append(meeting2)
            j+=1
    while i<len(calendar1):
        merged.append(calendar1[i])
        i+=1
    while j<len(calendar2):
        merged.append(calendar2[j])
        j+=1
    return merged
    
    # Write your code here.
    pass

# Much Simpler Solution2
# def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
#     earlyBound=max(timeToMinutes(dailyBounds1[0]),timeToMinutes(dailyBounds2[0]))
#     lateBound=min(timeToMinutes(dailyBounds1[1]),timeToMinutes(dailyBounds2[1]))
#     freeTimeCalendar1=getFreeTime(calendar1,earlyBound,lateBound)
#     freeTimeCalendar2=getFreeTime(calendar2,earlyBound,lateBound)
#     overlapFreeTime=getCalendarOverlap(freeTimeCalendar1,freeTimeCalendar2,meetingDuration)
#     return overlapFreeTime

# def getCalendarOverlap(freeTimeCalendar1,freeTimeCalendar2,meetingDuration):
#     timeOverlap=[]
#     for time1 in freeTimeCalendar1:
#         for time2 in freeTimeCalendar2:
#             if time1[0]<time2[1] and time1[1]>time2[0]:
#                 duration=min(time1[1],time2[1])-max(time1[0],time2[0])
#                 if duration>=meetingDuration:
#                     timeOverlap.append([minutesToTime(max(time1[0],time2[0])),minutesToTime(min(time1[1],time2[1]))])
#     return timeOverlap

# def getFreeTime(calendar,earlyBound,lateBound):
#     freetime=[]
#     if calendar==[]:
#         return [[earlyBound,lateBound]]
#     for idx in range(len(calendar)):
#         startTime=timeToMinutes(calendar[idx][0])
#         endTime=timeToMinutes(calendar[idx][1])
#         prevEndTime=timeToMinutes(calendar[idx-1][1])
#         if idx==0:
#             if startTime>earlyBound:
#                 freetime.append([earlyBound,startTime])
#         elif idx==len(calendar)-1:
#             if startTime>prevEndTime:
#                 freetime.append([prevEndTime,startTime])
#             if endTime<lateBound:
#                 freetime.append([endTime,lateBound])
#         else:
#             if startTime>prevEndTime:
#                 freetime.append([prevEndTime,startTime])
#     return freetime

# def timeToMinutes(time):
#     hours,minutes=list(map(int,time.split(":")))
#     return hours*60+minutes

# def minutesToTime(minutes):
#     hours=minutes//60
#     mins=minutes%60
#     hourStr=str(hours)
#     minStr=str(mins) if mins>0 else '00'
#     return hourStr+':'+minStr
#                     # Write your code here.
#     pass
