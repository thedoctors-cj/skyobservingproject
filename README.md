# skyobservingproject

Sky Observing Project Scoring Script

This scoring script is intended to be run using a web interface (included).
It can also be run at the command line with some path adjustments.

Instructions are given for the web interface below, under "Runnig the script".

The script is designed to use as input a spreadsheet of student responses to a Blackboard
form for each observation throughout a semester/year.

An instructor guide for the full project is available here: http://wp.towson.edu/jescott/observingprojectguide/

An export file of the Blackboard observation forms is available by request: jescott@towson.edu



Instructions: short version
==================================================================

When you start a new semester:

1. Create a directory where you want your results and put gradeAndTar.sh in that directory.

2. Modify the SEMESTER_START_DATE variable in gradeAndTar.sh to account for the first day of the semester. This is the Saturday, 3 weeks before the first
observations are due.

3. Change the web site directory to the one you just created in WebInterface/web_page.py

4. Restart the web server by killing the cron spawned process web_page.py and restarting it.

5. Go to localhost:8080 and upload the file




Instructions: detailed version
==================================================================


-------------------------------------------------------------------
Set up
-------------------------------------------------------------------

Initial set-up (one time)
-------------------------------------------------------------------
1. Check that you have the bottle python web framework installed:
python -c "import bottle"

If no reponse, it's there, you may proceed.

ModuleNotFoundError indicates you need to install it:
https://bottlepy.org/docs/dev/tutorial.html#installation

2. Modify the user(s) in the script WebInterface/web_page.py (usernames and
passwords can be independent of any users on localhost)



Beginning-of-semester set up (for each new semester)
-------------------------------------------------------------------
1. Make a subdirectory for your new semester, e.g. 2021_Spring

2. bash script
a. Copy gradeAndTar.sh into your new semester subdirectory.

b. In gradeAndTar.sh modify the SEMESTER_START_DATE variable to account for
the first day of the semester.  This is the Saturday 3 weeks before the first
observations are due.

3. In the script WebInterface/web_page.py
a. change the current_directory variable to the semester subdirectory you just created in step 1 above

b. start the web server:
./web_page.py


4. USNO data (if outside Baltimore area)
----------------------------------------
This repository contains USNO data through 2045 for the Baltimore area.
If you are using this tool outside this area, you will need to use data tables appropriate for your location.
Sun and Moon position data and Moon phase data can be downloaded at the USNO Data Services website:
https://www.usno.navy.mil/USNO/astronomical-applications/data-services/data-services
(Note: This site is down as of 2019-2021. It is scheduled to return to service in June 2021.)


-------------------------------------------------------------------
Running the script from a web form
-------------------------------------------------------------------
After students enter their observation data and the deadline has passed, download their responses from Blackboard
by choosing "Download Responses" from the menu on that observation's Grade Center column.

It is recommended to keep this item "hidden" from students until *after* you have run the grading script and uploaded scores & feedback it generates.
This is because Blackboard's default grading is insufficient and inaccurate and can't be turned off!

Go to localhost:8080 in your web browser

Select the observation number and upload the .xls file from Blackboard (Summary questions = Observation #8)

You will then be prompted to download a tgz file with all the output files created by the grading script (See * above)

All of the files downloaded through this form are also written to localhost in a subdirectory within your semester subdirectory


Observations 1-7
----------------
It is advisable to spot-check responses to ensure that this is working as you'd like it to.

The web interface will:
1- make a backup of the input .xls file and then modify the original to make it compatible with python
2- generate a variety of output files*
Observation_year_observationnumber/                         :directory containing individual files of each student's feedback
Observation_year_observationnumber.backup-dateandtime.xls   :backup .xls input file
Observation_year_observationnumber.grades.txt               :text file of scores only for all students
Observation_year_observationnumber.grades.xls               :.xls file of scores & feedback for all students (for copy/pasting, uploading back to Bb Grade Center)
Observation_year_observationnumber.output.txt               :details on how each students' entries were scored
Observation_year_observationnumber.summary.noComments.txt**   :text file of student input and feedback as given to student (same as in grades.xls file)
Observation_year_observationnumber.summary.withComments.txt** :text file of student input and feedback "(Teacher Only)" gives lines that don't go into student feedback
Observation_year_observationnumber.tgz                      :tarred, zipped contents of Observation_year_observationnumber/ subdirectory
Observation_year_observationnumber.xls                      :input .xls file modified for compatibilty with python
Observation_year_observationnumber_all.tgz                  :tarred, zipped contents of this directory, including Observation_year_observationnumber.tgz

**Check one of these files each time for flagged issues that require follow-up with students, e.g. students who:
-reported observation times or dates outside the correct windows (may be a typo by the student)
-claimed to see the Moon on a night it should have been below the horizon (fabricated data, or Moon observation made later in the night)
You may also want to check if the student uploaded any photograph to Blackboard, to determine the course of action

Default penalties:
--observation time or date outside the correct window: score=0
--reported Moon observation when Moon was not visible: score=0
 (I also institute a stronger penalty for the whole project for this, since it is a fabrication of data,
  a violation of the Code of Academic Integrity - and a no-no in science!)
--missed seeing the Moon when it was out: -3  (honest mistake)


Finally, each time you run the script, it generates
Observation_<year>_SavedDates_<ObservationNumber>
This is a record of each students' observation dates only.
It is not included in the tarred, zipped archives of output files but is retained on localhost for grading the end of semester summary questions.


Observation 8/Summary Questions
-------------------------------
The 8th observation asks the students to reflect on their observations and
has more questions than the first 7 observsations.

The python script will generate output files as above for the student responses to the summary questions, with observationnumber=8.

The instructor will need to score the final question (Q19) by hand. It is advisable to check the scoring of Q18 for proper tolerance as well.
