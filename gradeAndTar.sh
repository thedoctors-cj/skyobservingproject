#!/bin/bash

# The following date is the Saturday, 3 weeks before the first observations are due.
SEMESTER_START_DATE='January 26, 2019'

# The rest you shouldn't have to mess with 
NUM=$1
YEAR=${SEMESTER_START_DATE:(-4)}
NOW=$(date +"%Y%m%d%H%M%S")
BASENAME=Observation_${YEAR}_
cp ${BASENAME}${NUM}.xls ${BASENAME}${NUM}.backup-${NOW}.xls
dos2unix ${BASENAME}${NUM}.xls
pwd
../../gradeObservations.py --date "${SEMESTER_START_DATE}" --obs ${NUM} --infile ${BASENAME}${NUM}.xls > ${BASENAME}${NUM}.output.txt 2>&1
tar -zcvf ${BASENAME}${NUM}_all.tgz ${BASENAME}${NUM}.*
