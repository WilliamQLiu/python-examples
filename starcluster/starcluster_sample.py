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
    print "See notes about "
