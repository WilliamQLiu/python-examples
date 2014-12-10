""" Run to deploy to our internal Ubuntu server for data entry
    Run on server like so:
    $fab -H localhost,linuxbox host_type

 """

from fabric.api import run


### On Local Server
def update_requirements():
    """ Update requirements.txt on local computer """
    run('cd /Users/williamliu/GitHub/MHADjango')
    run('pip freeze > requirements.txt')

### Server Stuff Below
def aptget_update():
    """ Get the latest updates to the server"""
    run('sudo apt-get update')


def aptget_upgrade():
    """ Upgrade the latest upgrades """
    run('sudo apt-get upgrade')


def restart_server():
    """ Restart the entire server """
    reboot(wait=30)  # wait in seconds


def start_nginx():
    """ start nginx """
    run('sudo service nginx start')


def activate_virtualenv():
    """ Activate virtualenv """
    with cd('/home/dsadmin'):  # Go to directory
        run('source /opt/mha_env/bin/activate')


def start_gunicorn():
    """ Start gunnicorn with 6 workers """
    activate_virtualenv()
    run('cd /home/dsadmin/MHADjango/datasite')
    run('gunicorn dataentry.wsgi:application --bind 10.1.1.7:8000 -w 6')


def see_gunicorn_processes():
    """ See all gunicorn processes """
    run('ps ax|grep gunicorn')


def kill_gunicorn_processes():
    """ Kill all gunicorn processes """
    run('pkill gunicorn')


### Django Stuff Below

def install_project_requirements():
    """ Make sure requirements are installed """
    run('cd /home/dsadmin/MHADjango')
    activate_virtualenv()
    run('pip install -r requirements.txt')


def git_fetch_code():
    """ Get latest code from git """
    run('git fetch --all')
    # Will be prompted username and password
    run('git reset --hard origin/master')


def syncdb():
    """ Sync the database in case models changed """
    run('cd /home/dsadmin/MHADjango/datasite')
    run('python manage.py syncdb')


### MySQL Stuff Below
def check_mysql_status():
    """ Check mysql status """
    run('sudo netstat -tap | grep mysql')  # Is MySQL running?
    run('mysqladmin -u root -p status')  # Check status of MySQL


def restart_mysql():
    run('sudo service mysql restart')


def login_mysql():
    """ Log in as root """
    run('mysql -u root -p')
    # Useful commands for MySQL
    # mysql> show databases;
    # mysql> use mydb;  # Use a db
    # mysql> show tables;


if __name__ == '__main__':

    update_requirements()
    aptget_update()
    aptget_upgrade()
    restart_server()

    # Change settings.py DEBUG=False, TEMPLATE_DEBUG=False
    # Change settings.py DATABASE

    activate_virtualenv()
    git_fetch_code()  # Get latest GitHub code
    install_project_requirements()
    syncdb()
    start_nginx()
    start_gunicorn()
