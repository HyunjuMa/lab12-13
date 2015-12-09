# This script created a queue
#
# Author - Paul Doyle Aug 2013
#
#
import boto.sqs
import boto.sqs.queue
import argparse
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
sys.path.append('/data')
from keys import access_key_id, secret_access_key


parser = argparse.ArgumentParser()
parser.add_argument("qname")
args = parser.parse_args()

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

try:
	q=conn.get_queue(args.qname)
except:
	print "Failed to find queue ",args.qname
try:
	conn.delete_queue(q,True)
	print args.qname, " queue has been deleted"
except:
	print "Could not delete the queue, or it does not exist"
