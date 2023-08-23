#!/usr/bin/python3
# Conversion Notes
# XXX starts a note about a change I made
# DOME note something I need to come back to 

import argparse
import sys
import datetime
import os
import collections

# The config file in this directory has the global variables needed
# for this project
import config
import gradingSubroutines


##############################################################
# GLOBAL VARIABLES 
##############################################################
infile = ""
config.myGlobals["observation_number"] = -1
semester_start_date = ""
start_date = ""
end_date = ""
nested_dict = lambda: collections.defaultdict(nested_dict)
scores = nested_dict()
config.myGlobals["summary_all"] = nested_dict()
zeroed_score = {}
moon_visible = {}
flagged = {}
previous_observation_dates = {}
current_observation_dates = {}
sunset_times = {}
student_message_dir = ""
current_observation_dates_file = ""
previous_observation_dates_file = ""
days_to_first_observation = 0



##############################################################
# Parse Arguments and get things set up
##############################################################
parser = argparse.ArgumentParser(description="Example: ./gradeObservations.py --date \"February 5, 2011\" --obs 1 --infile data1")
parser.add_argument('--date', required=True, dest='semester_start_date', metavar='\"DATE\"', help='DATE is the start date for the semester observations in quotes, probably something like the first Saturday of the semseter, like \"February 5, 2011\"')
parser.add_argument('--obs', required=True, dest='observation_number', metavar='NUM', help='NUM is the number of the observation - starts at 1')
parser.add_argument('--infile', required=True, dest='infile', metavar='FILE', help='FILE is the tab delimited file from blackboard')

# Note: leavng --messages on all the time so commenting this out
# parser.add_argument('--messages', dest='create_Student_Messages', action='store_true', help="If this is given, a directory called \"" + config.messages_for_students_basename + "\" is created and a file for each student is created.")
args = parser.parse_args()

# Output the collected arguments
# print(args.semester_start_date)
# print(args.observation_number)
# print(args.infile)

# Fill in semester_start_date with the datetime object for that day
semester_start_date = datetime.datetime.strptime(args.semester_start_date, '%B %d, %Y')
config.myGlobals["observation_number"] = int(args.observation_number)
infile = args.infile
student_message_dir = config.myGlobals["messages_for_students_basename"] + str(config.myGlobals["observation_number"])
current_observation_dates_file = "../" + config.myGlobals["previous_observation_dates_basename"] + str(config.myGlobals["observation_number"])
previous_observation_dates_file = "../" + config.myGlobals["previous_observation_dates_basename"] + str(config.myGlobals["observation_number"]-1)

# validate myGlobals["observation_number"]
if (config.myGlobals["observation_number"] < 1) or (config.myGlobals["observation_number"]>8):
    sys.exit(f"EXITING: Observation Number given as {config.myGlobals['observation_number']} - must be an integer from 1 to 8")

# First observation period is 3 weeks
days_to_first_observation = 14*(config.myGlobals["observation_number"]-1)+7
if (config.myGlobals["observation_number"] == 1):
    days_to_first_observation = 0 

# Note: We added a day for one time April 23, 2015 and used the
# following line:
# my $days_to_last_observation = 14*($observation_number)+7;
# Added 2 days in Winter 2018 using the following
# my $days_to_last_observation = 14*($observation_number)+8;
days_to_last_observation = 14*config.myGlobals["observation_number"] + 6;

# DOME - decide if I want to move this to the config file and change
# the if statement to remove 2 entries if this isn't the first
# observation
if (config.myGlobals["observation_number"] == 1):
    config.myGlobals["questions"] = ["howDetermineDirection", "whereObservation"] + config.myGlobals["questions"]
    config.myGlobals["questionsText"] = ["How Direction was Determined", "Where was the observation made"] + config.myGlobals["questionsText"]
    config.myGlobals["questionsPoints"] = [1,1] + config.myGlobals["questionsPoints"]


##############################################################
# Initialization
##############################################################
config.myGlobals["start_date"] = semester_start_date + datetime.timedelta(days=days_to_first_observation)
config.myGlobals["end_date"] = semester_start_date + datetime.timedelta(days=days_to_last_observation)
config.myGlobals["year"] = semester_start_date.year

print(semester_start_date)
print(config.myGlobals["start_date"])
print(config.myGlobals["end_date"])
print(config.myGlobals["year"])

config.myGlobals["spring_semester"] = True
if config.myGlobals["start_date"].month > 6:
    config.myGlobals["spring_semester"] = False

if config.myGlobals["verbose"]:
    (y, m, d) = (semester_start_date.year, semester_start_date.month, semester_start_date.day)
    sys.stderr.write(f"Input Date: {m}/{d}/{y}\n")
    (y, m, d) = (config.myGlobals["start_date"].year, config.myGlobals["start_date"].month, config.myGlobals["start_date"].day)
    sys.stderr.write(f"Start Date: {m}/{d}/{y}\n")
    (y, m, d) = (config.myGlobals["end_date"].year, config.myGlobals["end_date"].month, config.myGlobals["end_date"].day)
    sys.stderr.write(f"End Date: {m}/{d}/{y}\n")

if (config.myGlobals["year"] < 2007) or (config.myGlobals["year"] > 2049):
      raise SystemExit(f"No daylight savings time for the year {config.myGlobals['year']}")

# load all the previous observation dates when we are on the summary case
if config.myGlobals["observation_number"] == 8:
    gradingSubroutines.load_all_previous_observation_dates(config.myGlobals)
elif (config.myGlobals["observation_number"] > 1):
    gradingSubroutines.load_previous_observation_dates(previous_observation_dates_file, previous_observation_dates) 
gradingSubroutines.load_sunset_times(sunset_times, config.myGlobals)
if config.myGlobals["create_Student_Messages"]:
    if not os.path.isdir(student_message_dir):
        os.mkdir(student_message_dir)

# this first part splits mac file (which use \r as newline) or windows (\r\n) or unix files (\n)
my_file = ''
try:
    with open(infile,"r") as IN:
        my_file = IN.read()
except IOError as e:
    sys.exit(f"EXITING: {infile} can't be opened")
lines = my_file.splitlines()
total_lines = len(lines)
if config.myGlobals["verbose"]:
    print(f"Parsing {total_lines} lines.\n", file=sys.stderr)


# We assume that the first row is the column headers
cols = lines[0].split("\t")
if config.myGlobals["verbose"]:
    print("Just grabbed the column headers from the first line\n", file=sys.stderr)

# If we find the first entry is empty, then we have a missing student
# name.  We use NoName followed by a counter for these entries without
# names, and the counter is $no_name:
no_name = 1

# Track if a student submitted multiple times
number_of_submissions = {}


# We currently assume that each line consists of a student's name
# followed by their answers
for row in lines[1:]:
    # clean blackboard junk
    row = gradingSubroutines.strip_tags(row)
    row = row.replace(u'\xa0', u' ')
    row = row.replace('\\n', '')

    # store the answers in the @answers array
    answers = row.split("\t")
    # strip off any weird whitespace left over from removing the html tags
    answers = [gradingSubroutines.dequote(x) for x in answers]
    answers = [x.strip() for x in answers]

    
    # if the student name is missing, give a warning and carry on
    if len(answers[0]) == 0:
        print(f"WARNING: Error extracting student name at line {row} -", file=sys.stderr)
        print(f" using NoName{no_name}\n", file=sys.stderr)
        answers[0] = "NoName" + no_name
        no_name += 1

    if answers[0] in number_of_submissions:
        number_of_submissions[answers[0]] += 1
        flagged[answers[0]] = f"This student submitted {number_of_submissions[answers[0]]} times - only scored first one"
        continue
    else:
        number_of_submissions[answers[0]] = 1

    just_answers = gradingSubroutines.isolateAnswers(answers)
    if config.myGlobals["verbose"]:
        print("\n", file=sys.stderr)

    if config.myGlobals["observation_number"] == 8:
        gradingSubroutines.gradeSummary(just_answers, scores, flagged, previous_observation_dates, sunset_times, moon_visible, zeroed_score, config.myGlobals)
    else:
        gradingSubroutines.gradeObservations(just_answers, scores, flagged, previous_observation_dates, sunset_times, moon_visible, zeroed_score, config.myGlobals)
        
## Do a little cleanup:
# If we bailed, we may not have filled in the moon_visible entry for
# every student, in that case, we fill in with -1
for name in scores.keys():
    if not name in moon_visible:
        moon_visible[name] = -1

# create a list of student userIDs sorted by lastname and then
# firstname - we include the userId at the end in order to make sure
# the names a fully unique 
userid_lastname_dict = {}
for name in scores.keys():
    userid_lastname_dict[scores[name]["lastName"] + scores[name]["firstName"] + name] = name
print(userid_lastname_dict)
config.myGlobals["sorted_userids"] = []
for full_name in sorted(userid_lastname_dict.keys()):
    config.myGlobals["sorted_userids"].append(userid_lastname_dict[full_name])


gradingSubroutines.save_current_observation_dates(current_observation_dates_file, scores, zeroed_score, moon_visible)
if config.myGlobals["create_Student_Messages"]:
    gradingSubroutines.createStudentMessages(scores, student_message_dir, config.myGlobals) 
gradingSubroutines.createTeacherSummary(                 scores, flagged, student_message_dir, config.myGlobals)
gradingSubroutines.createTeacherSummaryNoTeacherComments(scores, flagged, student_message_dir, config.myGlobals)
gradingSubroutines.printGrades(scores, student_message_dir, config.myGlobals)
gradingSubroutines.printSpreadsheet(scores, student_message_dir, config.myGlobals)
    
if config.myGlobals["create_Student_Messages"]:
    os.system(f"tar -zcvf {student_message_dir}.tgz {student_message_dir}")



