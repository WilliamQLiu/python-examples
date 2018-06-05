"""
ABOUT
Fabric is used for streamlining the use of SSH for
automation of a wide range of tasks varying from
application deployment (build a server) to systems
administration tasks (maintenance and monitoring)

INSTALLATION
Install fabric with: $sudo apt-get install fabric

'fabfiles' contain functions, then executes them via
the fab command-line tool

RUNNING
Run on server like so:
    $fab -H localhost,linuxbox host_type

"""

#import logging # debug output Paramiko prints
from fabric.api import run, cd

#For debugging, prints Paramiko's debug statements to
#standard error stream
#logging.basicConfig(level=logging.DEBUG)


def hello(who="world"):
    """Run with $fab hello:who=Fab"""
    print "Hello {who}!".format(who=who)


### run (fabric.operations.run)
# Run operation

def host_type():
    """ Display host type """
    run("uname -s")

def create_dir():
    """ Make directory """
    run("mkdir /tmp/trunk/")

def uptime():
    """ Returns uptime """
    run("uptime")

def hostname():
    """ Returns host name"""
    run("hostname")

def output_ls():
    """ Captures the output of 'ls' command """
    result = run("ls -l /var/www")
    print result
    # result.failed shows if command failed


### sudo (fabric.operations.sudo)
# Run operation as root/sudo or specified user

def sudo_create_dir():
    """ Create a directory as sudo """
    sudo("mkdir /var/www")

def sudo_create_dir_user():
    """ Create a directory as another user """
    sudo("mkdir /var/www/web-app-one", user="web-admin")



### local (fabric.operations.local)
# perform actions on the local machine
def local_remove_file():
    """ Remove a local file """
    local("rm /tmp/trunk/app.tar.gz")



### get (fabric.operations.get)
# Downloads/pulls file(s) from the remote system to the computer
# where Fabric is being used - good for backups, logging data
# Can specify the remote path with 'remote_path' argument
# Can specify the local path with 'local_path' argument

def get_logs():
    """ Get some logs from a remote system to local """
    get(remote_path="/tmp/log_extracts.tar.gz",
        local_path="/logs/new_log.tar.gz")

def get_db_backup():
    """ Download a database back-up """
    get("/backup/db.gz", "./db.gz")


### put (fabric.operations.put)
# Upload files; can get results with '.failed' and '.succeeded'
# Can specify the remote path with 'remote_path'
# Can specify the local path with 'local_path'
# Can set the file mode (flags) with 'mode'
# Can set the file flags automatically by reading local file's
#  mode with 'mirror_local'
# Can set as sudo with 'use_sudo'

def put_file_with_mode():
    """ Upload a file and set the exact mode desired """
    upload = put("requirements.txt", "requirements.txt", mode= 664)
    # 'upload.succeeded' to verify the upload


### prompt (fabric.operations.prompt)
# Asks the user (person running the script) to input data

def prompt_port():
    """ Prompt the user with port number to use """
    port_number = prompt("Which port would you like to use?")

def prompt_port_defaults():
    """ Prompt the user with port number to use with defaults """
    port_number = prompt("Which port?", default=42, validate=int)


### Reboots the remote system
# Default wait time is 120 seconds
def reboot_system():
    """ Reboot the system using default 2 min wait """
    reboot()

def reboot_system_quick():
    """ Reboot the system after 30 seconds wait """
    reboot(wait=30)


### cd (fabric.context_managers.cd)
# Context Managers keeps the directory state (i.e. where the
#    following block of code is executed)
def using_single_cd():
    """ Using a single context manager to manage path """
    with cd("/tmp/trunk"):
        items = sudo("ls -l")

def using_chain_cd():
    """ Chain context managers, i.e. goes to '/tmp/trunk' """
    with cd("/tmp"):
        with cd("/trunk"):
            run("ls")


