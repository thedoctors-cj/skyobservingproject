#!/usr/bin/python

import os
import bottle
from bottle import route, request, static_file, run, template, auth_basic
from datetime import date, datetime, timedelta
import subprocess

# Global Variables
datetime_format = "%Y%m%d%H%M%S"
#current_directory="2020_Fall"
current_directory="2019_Spring-Python"
users = { "AAAA":"BBBB1234" , "CCCC":"DDDD1234" }

# Check Passwords
def check(user, pw):
    # Check user/pw here and return True/False
    if (user in  users) and (users[user] == pw):
        return True
    return False

# start off by finding out the directory of this file
bottle_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(bottle_dir)

# Then we will switch to where we are uploading files but we need to
# have access to out templates, so we have to add them to
# bottle.TEMPLATE_PATH
bottle.TEMPLATE_PATH.insert(0, ("%s/views" % bottle_dir))

save_path = "../{current_directory}".format(current_directory=current_directory)
save_path = os.path.realpath(save_path)
os.chdir(save_path)


@route('/')
@auth_basic(check)
def root():
    return template('basic_template', current_directory=current_directory)

@route('/static/<filename:path>')
@auth_basic(check)
def send_static(filename):
    print(filename)
    return static_file(filename, root=save_path)

@route('/upload', method='POST')
@auth_basic(check)
def do_upload():
    obs_num  = request.forms.get('obs_num')
    upload   = request.files.get('upload')
    os.chdir(save_path)

    try:
        value = int(obs_num)
    except ValueError:
        return "Observation number must be entered - go back and input a number from 1 to 8."

    # Work in a timestamped directory to avoid stomping things
    now = datetime.now().strftime(datetime_format)
    base_name = "Observation_{obs_num}".format(obs_num=obs_num)
    directory = base_name + ("-%s" % now)
    in_file   = base_name + ".xls"
    out_file  = base_name + "_all.tgz"

    file_path = "{path}/{directory}/{in_file}".format(path=save_path, directory=directory, in_file=in_file)

    if not os.path.exists(save_path):
        os.makedirs(save_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    os.chdir(directory)

    try:
        upload.save(file_path)
    except:
        return "No file selected - go back and select a file for upload - tried to upload to %s." % file_path
    out = "File successfully saved to '{0}'.\n<p>".format(file_path)

    out += "Starting processing...\n<p>"

    do_this = "../gradeAndTar.sh %s" % (obs_num)
    p = subprocess.Popen(do_this, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    out += do_this + "\n<p>"
    out += "Done processing.\n<p>"
    os.chdir(bottle_dir)
    out += "<a href=\"static/%s/%s\">%s</a>" % (directory, out_file, out_file)
    return out

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)
