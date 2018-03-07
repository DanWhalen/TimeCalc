#OPENING
print("Welcome to TimeCalc")
print("Copyright Dan Whalen, 2014")
print("")

state = 1
while state == 1:
    try:
        #USER INPUT
        print("")
        print("")
        info = raw_input('In time, Out time, Mins for lunch: ')
        info_list = str(info).split()
        intime = info_list[0]
        inmeridian = info_list[1]
        outtime = info_list[2]
        outmeridian = info_list[3]
        lunch_mins = info_list[4]
            
        #GET IN TIME
        #multi-digit intime
        if len(intime)%2 == 1:
            in_hour = intime[0]
        elif len(intime)%2 == 0:
            in_hour = intime[0] + intime[1]
        #single-digit intime (on the hour)
        if len(intime) == 1 or len(intime) == 2:
            in_minute = 0
        else:
            in_minute = intime[-2] + intime[-1]

        #GET OUT TIME
        #multi-digit intime
        if len(outtime) == 1 or len(outtime) == 3:
            out_hour = outtime[0]
        elif len(outtime) == 2 or len(outtime) == 4:
            out_hour = outtime[0] + outtime[1]
        #single-digit intime (on the hour)
        if len(outtime) == 1 or len(outtime) == 2:
            out_minute = 0
        else:
            out_minute = outtime[-2] + outtime[-1]

        #MAKE EVERYTHING INT
        out_hour = int(out_hour)
        out_minute = int(out_minute)
        in_hour = int(in_hour)
        in_minute = int(in_minute)
        lunch_mins = int(lunch_mins)

        #CALCULATE
        #IF ON SAME SIDE OF MERIDIAN
        if inmeridian == outmeridian:
            #change '12' to '0' -NB: 12am is midnight, 12pm is noon-
            if in_hour == 12 and out_hour == 12:
                in_hour = 0
                out_hour = 0
            elif in_hour == 12 and out_hour != 12:
                in_hour = 0
            else:
                pass
            #count hours and mins
            mins_to_next_hour = 60 - in_minute
            in_hour = in_hour+1
            hours_worked = out_hour-in_hour
            mins_worked = mins_to_next_hour + out_minute
            #summing
            total_mins = float(hours_worked*60) + mins_worked - lunch_mins
            total = float(total_mins/60)

        #IF ON DIFFERENT SIDE OF MERIDIAN
        if inmeridian != outmeridian:
            if in_hour == 12:
                in_hour = 0
            if out_hour == 12:
                out_hour = 0
            #count hours and mins
            mins_to_next_hour = 60 - in_minute
            in_hour = in_hour+1
            hours_to_meridian = 12-in_hour
            hours_worked = hours_to_meridian + out_hour
            mins_worked = mins_to_next_hour + out_minute
            #summing
            total_mins = float(hours_worked*60) + mins_worked - lunch_mins
            total = float(total_mins/60)

        #PRINT OUT RESULTS
        if total >= 0:
            print("   -Time worked: " + str(round(total,2)) + " hours-")
        else:
            print("   -Time worked: " + str(round(total,2)) + " hours-")
            print("   (Neg. answer since 'out time' occurs before 'in time')")
            
    #SKIP ERRORS, AND OFFER INTSTRUCTIONS
    except NameError:
        print("Error: time entered incorrectly.")
        instructions = raw_input('Review TimeCalc instructions? (y/n) -> ')
        if instructions == 'n' or instructions == 'N':
            pass
        elif instructions == 'y' or instructions == 'Y':
            print('')
            print('')
            print('------------BEGIN TIMECALC INSTRUCTIONS------------')
            print('')
            print('1) WHAT IS TIMECALC?')
            print('Give TimeCalc your in time, out time, and time for lunch (in minutes).')
            print('TimeCalc will return the total number of hours you worked in decimal form.')
            print('')
            print('')
            print('2) EXAMPLES')
            print('For a 8:45 am to 5:15 pm shift, with a full hour for lunch:')
            print('   Enter  -> 845 a 515 p 60')
            print('   Output -> 7.5 hours')
            print('')
            print('For a 8:00 pm to 11:00 pm shift, with a half hour lunch:')
            print('   Enter  -> 8 pm 11 pm 30')
            print('   Output -> 2.5  hours')
            print('')
            print('For a 9:22 am to 4:47 pm shift, with 36 minutes for lunch:')
            print('   Enter  -> 922 am 447 pm 36')
            print('   Output -> 6.82 hours')
            print('')
            print('')
            print('3) ENTERING TIME CORRECTLY')
            print('Input requires five items, with a space separating each:')
            print('')
            print('[TIME-IN] [space] [TIME-IN AM OR PM] [space] [TIME-OUT] [space] [TIME-OUT AM OR PM] [space] [LUNCH TIME IN MINS]')
            print('')
            print('')
            print('4) NOTES')
            print('The "m" in "am" and "pm" is not necessary.')
            print('(e.g. Use either "a" or "am" to signify morning.  Use either "p" or "pm" to signify afternoon/evening.)')
            print('')
            print('If you did not have a lunch break, enter "0" for your lunch time.')
            print('(e.g. Correct: "11 am 515 pm 0".  Incorrect: "11 am 515 pm")')
            print('')
            print('Do not use colons.')
            print('(e.g. Correct: "735".  Incorrect: "7:35")')
            print('')
            print('Include a space after each inputted item.')
            print('(e.g. Correct: "645 pm".  Incorrect: "645pm")')
            print('')
            print('For times on the hour, entering "00" minutes is not necessary.')
            print('(e.g. "1:00 pm" can be entered as either "1 pm" or "100 pm")')
            print('')
            print('-----------------END OF INSTRUCTIONS---------------')
            print('')

    except IndexError:
        print("Error: time entered incorrectly.")
        instructions = raw_input('Review TimeCalc instructions? (y/n) -> ')
        if instructions == 'n' or instructions == 'N':
            pass
        elif instructions == 'y' or instructions == 'Y':
            print('')
            print('')
            print('------------BEGIN TIMECALC INSTRUCTIONS------------')
            print('')
            print('1) WHAT IS TIMECALC?')
            print('Give TimeCalc your in time, out time, and time for lunch (in minutes).')
            print('TimeCalc will return the total number of hours you worked in decimal form.')
            print('')
            print('')
            print('2) EXAMPLES')
            print('For a 8:45 am to 5:15 pm shift, with a full hour for lunch:')
            print('   Enter  -> 845 a 515 p 60')
            print('   Output -> 7.5 hours')
            print('')
            print('For a 8:00 pm to 11:00 pm shift, with a half hour lunch:')
            print('   Enter  -> 8 pm 11 pm 30')
            print('   Output -> 2.5  hours')
            print('')
            print('For a 9:22 am to 4:47 pm shift, with 36 minutes for lunch:')
            print('   Enter  -> 922 am 447 pm 36')
            print('   Output -> 6.82 hours')
            print('')
            print('')
            print('3) ENTERING TIME CORRECTLY')
            print('Input requires five items, with a space separating each:')
            print('')
            print('[TIME-IN] [space] [TIME-IN AM OR PM] [space] [TIME-OUT] [space] [TIME-OUT AM OR PM] [space] [LUNCH TIME IN MINS]')
            print('')
            print('')
            print('4) NOTES')
            print('The "m" in "am" and "pm" is not necessary.')
            print('(e.g. Use either "a" or "am" to signify morning.  Use either "p" or "pm" to signify afternoon/evening.)')
            print('')
            print('If you did not have a lunch break, enter "0" for your lunch time.')
            print('(e.g. Correct: "11 am 515 pm 0".  Incorrect: "11 am 515 pm")')
            print('')
            print('Do not use colons.')
            print('(e.g. Correct: "735".  Incorrect: "7:35")')
            print('')
            print('Include a space after each inputted item.')
            print('(e.g. Correct: "645 pm".  Incorrect: "645pm")')
            print('')
            print('For times on the hour, entering "00" minutes is not necessary.')
            print('(e.g. "1:00 pm" can be entered as either "1 pm" or "100 pm")')
            print('')
            print('-----------------END OF INSTRUCTIONS---------------')
            print('')
