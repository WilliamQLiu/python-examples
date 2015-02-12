"""
    StarCluster is a cluster-computing toolkit for Amazon's EC2
    Designed to automate and simplify the process of building,
    configuring, and managing clusters of virtual machines

    Sets up a computing environment in the cloud suited for
    distributed and parallel computing applications and systems

    Quickstart: http://star.mit.edu/cluster/docs/latest/quickstart.html
    Found: http://zonca.github.io/machine-learning-at-scale-with-python/

    StarCluster does the following:
    * Configures a new security group for each cluster (e.g. @sc-mycluster)
        Allows control of all network access using cluster's security group
    * Simple naming convention for all of the nodes in the cluster
        Each worker node is then labeled 'node001' (instead of random ec2-123)
        $starcluster listclusters
    * Configure a non-root user account to use for non-admin tasks
        $starcluster sshmaster -u sgeadmin mycluster
    * Password-less SSH
        Can simply login to the master node of a cluster (because its configured
        so that ssh can connect to any node in the cluster without a password
        $starcluster sshmaster mycluster
        $ssh node001
    * NFS Shares
        By default, /home on the master node is NFS-shared across the cluster
        Any EBS volumes specified in a cluster's config is also NFS-shared
    * EBS volumes
        Allows you to attach and NFS-share EBS volumes across the cluster for
        persistent storage with these lines in the config:
          [volume mydata]
          volume_id = vol-9999999
          mount_path = /mydata

          [cluster mycluster]
          volumes - mydata
    * StarCluster configures the Oracle Grid Engine queueing system for
      distributing tasks/jobs across the cluster
    * Easy to copy data to and from a cluster
        $starcluster put mycluster /local/file/or/dir /remote/path
        $starcluster get mycluster /remote/path /local/file/or/dir

"""


#from ConfigParser import ConfigParserN

if __name__ == '__main__':

    ### Starcluster Config File is here, holds AWS keys
    print "Setup config file (AWS info, cluster setup)"
    print "$subl ~/.starcluster/config"
    print "\n"

    ### Start a cluster that we named in config
    print "Start a cluster that we named in config (e.g. smallcluster)"
    print "$starcluster start smallcluster"
    print "\n"

    ### SSH into cluster
    print "SSH into cluster"
    print "$starcluster sshmaster smallcluster"
    print "\n"

    ### Put local file or dir to server
    print "Put file or dir from local computer to server"
    print "$starcluster put smallcluster /path/to/local/file/or/dir /remote/path/"
    print "\n"

    ### Get get file or dir from server to local computer
    print "Get file or dir from server to local computer"
    print "$starcluster get smallcluster /path/to/remote/file/or/dir /local/path/"
    print "\n"

    ### Terminate server (IMPORTANT - or else it'll cost a lot)
    print "Terminate server"
    print "$starcluster teminate smallcluster"
    print "\n"

    ### help
    print "Get additional help"
    print "$starcluster --help"
    print "\n"