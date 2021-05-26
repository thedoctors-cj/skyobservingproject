# Questions:
# Where to make sure we are using utf8
# &Date_Init("setdate=now,GMT")

import os

##############################################################
# Configuration VARIABLES 
##############################################################
myGlobals = {}

myGlobals["verbose"] = 1
myGlobals["printDaylightSavingsCheck"] = 0
myGlobals["messages_for_students_basename"] = "Observation_"
myGlobals["previous_observation_dates_basename"] = myGlobals["messages_for_students_basename"] + "SavedDates_"
myGlobals["path"] = os.path.dirname(os.path.abspath(__file__))
myGlobals["sunrise_sunset_dir"] = myGlobals["path"] + "/SunriseSunset"
myGlobals["alt_azm_dir"] = myGlobals["path"] + "/AltAzm"
myGlobals["sun_degree_slop"] = {}
myGlobals["sun_degree_slop"][1] = 30
myGlobals["sun_degree_slop"][2] = 30

for ii in range(3,20):
    myGlobals["sun_degree_slop"][ii] = 21

myGlobals["moon_phase_slop"] = .1
myGlobals["moon_location_cutoff"] = .3
myGlobals["moon_location_slop"] = .1

# after a rethink, we say that the moon altitude must be at
# least 5 degrees in order to be visible - generally corresponds
# to 30-40 minutes after moonrise
myGlobals["moon_altitude_min"] = 10

# In the case where the moon is a tiny bit illuminated (this implies
# it will be close to the horizon at sunset), some people could see it
# and be right, while others may not see it and we still want to allow
# for this.  Note also that we are not doing this for a nearly full
# moon - they should see that.  We are doing this for 15%
myGlobals["moon_visible_slop"] = 15

# This flag indicates whether a directory should be create and
# messages for each student should be created
myGlobals["create_Student_Messages"] = 1

myGlobals["namePhase"] = {}
myGlobals["namePhase"]["waxing crescent"] = 1
myGlobals["namePhase"]["1st quarter"] = 2
myGlobals["namePhase"]["waxing gibbous"] = 3
myGlobals["namePhase"]["full"] = 4
myGlobals["namePhase"]["waning gibbous"] = 5
myGlobals["namePhase"]["3rd quarter"] = 6
myGlobals["namePhase"]["waning crescent"] = 7
myGlobals["namePhase"]["no moon"] = 8
# Invert the dict 
myGlobals["reverseNamePhase"] = {v: k for k, v in myGlobals["namePhase"].items()}
myGlobals["skyLocation"] = {}
myGlobals["skyLocation"]["close to the eastern horizon"] = 1
myGlobals["skyLocation"]["in the eastern sky, between the horizon and overhead (the meridian)"] = 2
myGlobals["skyLocation"]["overhead (on the meridian), or close to overhead (the meridian)"] = 3
myGlobals["skyLocation"]["in the western sky, between the horizon and overhead (the meridian)"] = 4
myGlobals["skyLocation"]["close to the western horizon"] = 5
myGlobals["skyLocation"]["no moon"] = 6
# Invert the dict 
myGlobals["reverseSkyLocation"] = {v: k for k, v in myGlobals["skyLocation"].items()}


myGlobals["questions"] = ["date", "time", 
    	 "sun_set_north_tf", "degrees_north", 
    	 "moon_visible_tf", "moon_phase", 
    	 "moon_phase_name", "moon_location"]
myGlobals["questionsText"] = ["Observation Date", 
    	     "Observation Time", 
    	     "Sun Set North of West (T/F)", 
    	     "Number of Degrees from West", 
    	     "Moon Was Visible (T/F)", 
    	     "Moon Phase", 
    	     "Moon Phase Name", 
    	     "Moon Location"]
myGlobals["questionsPoints"] = [1,1,1,1,1,2,1,1]
myGlobals["daylight_savings_start"] = {}
myGlobals["daylight_savings_end"] = {}
myGlobals["daylight_savings_check"] = {}

# Start is the first day (a Sunday), end is the first day of
# non-daylight savings (Note, this is a bit goofy, but otherwise we
# could have the last day of daylight savings be in October 
myGlobals["daylight_savings_start"][2007] = 11
myGlobals["daylight_savings_start"][2008] = 9
myGlobals["daylight_savings_start"][2009] = 8
myGlobals["daylight_savings_start"][2010] = 14
myGlobals["daylight_savings_start"][2011] = 13
myGlobals["daylight_savings_start"][2012] = 11
myGlobals["daylight_savings_start"][2013] = 10
myGlobals["daylight_savings_start"][2014] = 9
myGlobals["daylight_savings_start"][2015] = 8
myGlobals["daylight_savings_end"][2007] = 4
myGlobals["daylight_savings_end"][2008] = 2
myGlobals["daylight_savings_end"][2009] = 1
myGlobals["daylight_savings_end"][2010] = 7
myGlobals["daylight_savings_end"][2011] = 6
myGlobals["daylight_savings_end"][2012] = 4
myGlobals["daylight_savings_end"][2013] = 3
myGlobals["daylight_savings_end"][2014] = 2
myGlobals["daylight_savings_end"][2015] = 1

myGlobals["daylight_savings_start"][2016] = 13
myGlobals["daylight_savings_start"][2017] = 12
myGlobals["daylight_savings_start"][2018] = 11
myGlobals["daylight_savings_start"][2019] = 10
myGlobals["daylight_savings_start"][2020] = 8
myGlobals["daylight_savings_start"][2021] = 14
myGlobals["daylight_savings_start"][2022] = 13
myGlobals["daylight_savings_start"][2023] = 12
myGlobals["daylight_savings_start"][2024] = 10
myGlobals["daylight_savings_start"][2025] = 9
myGlobals["daylight_savings_start"][2026] = 8
myGlobals["daylight_savings_start"][2027] = 14
myGlobals["daylight_savings_start"][2028] = 12
myGlobals["daylight_savings_start"][2029] = 11
myGlobals["daylight_savings_start"][2030] = 10
myGlobals["daylight_savings_start"][2031] = 9
myGlobals["daylight_savings_start"][2032] = 14
myGlobals["daylight_savings_start"][2033] = 13
myGlobals["daylight_savings_start"][2034] = 12
myGlobals["daylight_savings_start"][2035] = 11
myGlobals["daylight_savings_start"][2036] = 9
myGlobals["daylight_savings_start"][2037] = 8
myGlobals["daylight_savings_start"][2038] = 14
myGlobals["daylight_savings_start"][2039] = 13
myGlobals["daylight_savings_start"][2040] = 11
myGlobals["daylight_savings_start"][2041] = 10
myGlobals["daylight_savings_start"][2042] = 9
myGlobals["daylight_savings_start"][2043] = 8
myGlobals["daylight_savings_start"][2044] = 13
myGlobals["daylight_savings_start"][2045] = 12
myGlobals["daylight_savings_start"][2046] = 11
myGlobals["daylight_savings_start"][2047] = 10
myGlobals["daylight_savings_start"][2048] = 8
myGlobals["daylight_savings_start"][2049] = 14
myGlobals["daylight_savings_end"][2016] = 6
myGlobals["daylight_savings_end"][2017] = 5
myGlobals["daylight_savings_end"][2018] = 4
myGlobals["daylight_savings_end"][2019] = 3
myGlobals["daylight_savings_end"][2020] = 1
myGlobals["daylight_savings_end"][2021] = 7
myGlobals["daylight_savings_end"][2022] = 6
myGlobals["daylight_savings_end"][2023] = 5
myGlobals["daylight_savings_end"][2024] = 3
myGlobals["daylight_savings_end"][2025] = 2
myGlobals["daylight_savings_end"][2026] = 1
myGlobals["daylight_savings_end"][2027] = 7
myGlobals["daylight_savings_end"][2028] = 5
myGlobals["daylight_savings_end"][2029] = 4
myGlobals["daylight_savings_end"][2030] = 3
myGlobals["daylight_savings_end"][2031] = 2
myGlobals["daylight_savings_end"][2032] = 7
myGlobals["daylight_savings_end"][2033] = 6
myGlobals["daylight_savings_end"][2034] = 5
myGlobals["daylight_savings_end"][2035] = 4
myGlobals["daylight_savings_end"][2036] = 2
myGlobals["daylight_savings_end"][2037] = 1
myGlobals["daylight_savings_end"][2038] = 7
myGlobals["daylight_savings_end"][2039] = 6
myGlobals["daylight_savings_end"][2040] = 4
myGlobals["daylight_savings_end"][2041] = 3
myGlobals["daylight_savings_end"][2042] = 2
myGlobals["daylight_savings_end"][2043] = 1
myGlobals["daylight_savings_end"][2044] = 6
myGlobals["daylight_savings_end"][2045] = 5
myGlobals["daylight_savings_end"][2046] = 4
myGlobals["daylight_savings_end"][2047] = 3
myGlobals["daylight_savings_end"][2048] = 1
myGlobals["daylight_savings_end"][2049] = 7


myGlobals["summary_degrees_slop"] = 10
myGlobals["summaryNamePhase"] = {}
myGlobals["summaryNamePhase"]["waxing crescent"] = 1
myGlobals["summaryNamePhase"]["1st quarter"] = 2
myGlobals["summaryNamePhase"]["waxing gibbous"] = 3
myGlobals["summaryNamePhase"]["full"] = 4
myGlobals["summaryNamePhase"]["waning gibbous"] = 5
myGlobals["summaryNamePhase"]["3rd quarter"] = 6
myGlobals["summaryNamePhase"]["waning crescent"] = 7
myGlobals["summaryNamePhase"]["new"] = 8

myGlobals["summaryReverseNamePhase"] = {v: k for k, v in myGlobals["summaryNamePhase"].items()}

myGlobals["summaryQuestions"] = range(1,20)
myGlobals["summaryQuestionsText"] = ["1. Over the course of the semester the position of the sunset (2 points)",
"2. True or false: The sunset position crossed the position of due West at some point during the semester. (2 points)",
"3. The date on which the event in the previous question occurred is (choose all that apply). (2 points)",
"4. Enter the month of your last observation (1-12). (1 point)",
"5. Enter the date of your last observation (1-31). (1 point)",
"6. True or false: In 6 months from your last observation, the sunset will be North of due West. (2 points)",
"7. Enter the number of degrees the sunset position will be in 6 months in the direction you gave for the previous question. (2 points)",
"8. True or false: In one year from your last observation, the sunset will be North of due West. (2 points)",
"9. Enter the number of degrees the sunset position will be in one year in the direction you gave for the previous question. (2 points)",
"10. What will the Moon's phase be in two weeks from your last observation? (2 points)",
"11. What will the Moon-Sun angular distance (or separation) in the sky be two weeks from your last observation? (2 points)",
"12. What will the Moon's phase be in one month from your last observation? (2 points)",
"13. What will the Moon-Sun angular distance (or separation) in the sky be one month from your last observation? (2 points)",
"14. Choose one of your observation dates you did NOT see the Moon and give the month here (1-12) * (1 point)",
"15. Choose one of your observation dates you did NOT see the Moon (the same one you used in the previous question) and give the date here (1-31)* (1 point)",
"16. What was the Moon's phase on the date you entered above? (2 points)",
"17. What was the Moon-Sun angular distance (or separation) on the date you entered above? (2 points)",
"18. What Moon phases are never visible at sunset? (Choose all that apply.) (2 points)",
"19. Explain your answer(s) to the previous question. (3 points)"]
myGlobals["summaryPoints"] = [2,2,2,1,1,2,2,2,2,2,2,2,2,1,1,2,2,2,3]

myGlobals["summary_questions_01"] = ["did not change.",
"started South of due West and gradually moved North.",
"started North of due West and gradually moved South.",
"completed part of its 360 degree path around the horizon.",
"Both b) and d).",
"Both c) and d). "]

myGlobals["summary_questions_03"] = ["The event did not occur.",
"around September 22",
"around March 20",
"around June 21",
"around December 21",
"the summer solstice",
"the vernal equinox",
"the autumnal equinox",
"the winter solstice"]

myGlobals["summary_questions_10"] = ["new",
"waxing crescent",
"1st quarter",
"waxing gibbous",
"full",
"waning gibbous",
"3rd quarter",
"waning crescent"]

myGlobals["summary_questions_11"] = ["about 0 degrees",
"between 0 and 90 degrees",
"about 90 degrees",
"between 90 and 180 degrees",
"about 180 degrees"]

myGlobals["summary_questions_12"] = ["new",
"waxing crescent",
"1st quarter",
"waxing gibbous",
"full",
"waning gibbous",
"3rd quarter",
"waning crescent"]

myGlobals["summary_questions_13"] = ["about 0 degrees",
"between 0 and 90 degrees",
"about 90 degrees",
"between 90 and 180 degrees",
"about 180 degrees"]

myGlobals["summary_questions_16"] = ["new",
"waxing crescent",
"1st quarter",
"waxing gibbous",
"full",
"waning gibbous",
"3rd quarter",
"waning crescent"]

myGlobals["summary_questions_17"] = ["about 0 degrees",
"between 0 and 90 degrees",
"about 90 degrees",
"between 90 and 180 degrees",
"about 180 degrees"]

myGlobals["summary_questions_18"] = ["new",
"waxing crescent",
"1st quarter",
"waxing gibbous",
"full",
"waning gibbous",
"3rd quarter",
"waning crescent",
"None. All phases are in principle visible at sunset."]

