"""
    Boto provides a Python interface to nearly all of the Amazon
    Web Services.
    http://docs.pythonboto.org/en/latest/getting_started.html
    http://www.pythoncentral.io/introduction-to-python-on-aws-with-boto/

    Note: Make sure that there's a correct ~/.boto config file
    that has your AWS KEY and SECRET KEY
"""

import boto
#from boto.ec2 import EC2Connection
import boto.ec2
#from boto.s3.connection import S3Connection
import time


def s3_bucket_and_keyvalue_example(s3_conn):
    """ Create a new S3 bucket (each bucket must have its own unique name
        (worldwide), enter a key/value pair, then delete key/value pair
        and destroy bucket """

    # Create bucket
    bucket = s3_conn.create_bucket('boto-demo-willliu-%s' % int(time.time()))

    # Create a new key/value pair
    key = bucket.new_key('mykey')
    key.set_contents_from_string('This is a test!')

    time.sleep(2)  # Sleep to ensure the data is eventually there

    # Retrieve the contents of 'mykey' (i.e. 'This is a test!')
    print "Contents of key is: ", key.get_contents_as_string()
    key.delete()  # Delete the key
    bucket.delete()  # Delete the bucket


def ec2_launch_and_terminate_instance(ec2_conn):
    """ Launch, stop, and terminate EC2 instances """

    # Launch a specific instance with this image
    ec2_conn.run_instance('<ami-image-id>')
    # FROM: http://star.mit.edu/cluster/  Latest AMI IDs (us-east-1)
    # Sample 32bit 12.04 Ubuntu with StarCluster: ami-7c5c3915 (i386)
    # Sample 64bit 12.04 Ubuntu with StarCluster: ami-765b3e1f (x86_64)

    # 'Graceful' stop instance (shut down, but not terminates so still billed)
    ec2_conn.stop_instances(instance_ids=['instance-id-1', 'instance-id-2'])

    # Completely done with instance, terminate/destroy it, never get back
    ec2_conn.terminate_instances(instance_ids=
                                 ['instance-id-1', 'instance-id-2'])


def check_what_instances_running(conn):
    """ Get info and check health status of instances """
    reservations = conn.get_all_reservations()
    print reservations  # e.g. [Reservation:r-00000000]

    # A reservation corresponds to a command to start instances
    instances = reservations[0].instances
    print instances # e.g. [Instance:i-00000000]

    # An instance object gives you more meta-data about the instance
    inst = instances[0]
    print "Type of instance is: ", inst.instance_type  # e.g. u'c1.xlarge'
    print "Availability zone is: ", inst.placement # e.g. u'us-west-2'

    # Check health status of instance
    statuses = conn.get_all_instance_status()
    print "Statuses: ", statuses  # e.g. [InstanceStatus:i-00000000]


def ebs_basics(conn):
    """ EBS is used by EC2 instances as permanent storage
        Note: EBS must be in the same availability zone as EC2 instance """

    # Create Volume
    vol = conn.create_volume(50, "us-east-1d")  # 50GB
    print "Volume is: ", vol  # Volume:vol-00000000

    # Check Volume is ready and available
    curr_vol = conn.get_all_volumes([vol.id])[0]
    print "Current Volume Status: ", curr_vol.status  # u'available'
    print "Current Volume Zone: ", curr_vol.zone  # u'us-west-2'

    # Now attach volume to an EC2 instance
    conn.attach_volume(vol.id, inst.id, "/dev/sdx")  # u'attaching'
    # Will now have a new volume attached to your instance
    # For some Linux kernels, /dev/sdx may translate as /dev/xvdv

if __name__ == '__main__':

    boto.set_stream_logger('boto')  # debug logging

    ### Connect to services and authorize
    try:
        s3_conn = boto.connect_s3()
        ec2_conn = boto.ec2.connect_to_region("us-east-1d")

    except "NoAuthHandlerFound":
        print "Check your login creditials at ~/.boto config file"


    #s3_bucket_and_keyvalue_example(s3_conn)
    #ec2_launch_and_terminate_instance(ec2_conn)
    #check_what_instances_running(ec2_conn)  # Can also be ec2_conn
    ebs_basics(ec2_conn)  # Must run EBS in same as EC2 instance


