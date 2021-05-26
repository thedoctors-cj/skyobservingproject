# skyobservingproject

When you start a new semester:

1. Create a directory where you want your results and put gradeAndTar.sh in that directory.

2. Modify the SEMESTER_START_DATE variable in gradeAndTar.sh to account for
the first day of the semester.  This is the Saturday, 3 weeks before the
first observations are due.

3. Change the web site directory to the one you just created in
WebInterface/web_page.py

4. Restart the web server by killing the cron spawned process web_page.py
and restarting it.

5. Go to localhost:8080 and upload the file

