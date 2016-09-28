import boto.ec2
import sys
import time


# Establish connection with AWS
def instanceConnection(region):
    try:
        connection = boto.ec2.connect_to_region(region,
                                aws_access_key_id = 'Insert the Access Key',
                                aws_secret_access_key = 'Insert the Secret Access Key')
        return connection
    except:
        return None

# Start one or many Instances
def startInstance(noOfInstances, region):
    aws = instanceConnection(region)
    if aws is not None:
        runningInstance = []
        try:
            print ('Initializing ' + str(noOfInstances) + ' EC2 instance(s) in ' + region + ' region ...')
            for i in range(noOfInstances):
                start = aws.run_instances('ami-6869aa05', instance_type='t2.micro')
                print 'Starting Instance', i+1
                runningInstance.append(start.instances[0])
                print runningInstance[i]
            print 'Initializing...'
            time.sleep(15)
            print 'Initialized'
        except:
            print (sys.exc_info()[1])
        while True:
            try:
                askUser = raw_input('What do you want to do?\n1 Know instance(s) info\n'
                                    '2 Terminate instance\n0 Exit\n')
                if askUser == '0':
                    sys.exit(0)
                elif askUser == '1':
                    statusInstance(region)
                elif askUser == '2':
                    terminateInstance(region)
                else:
                    raise ValueError
            except ValueError as e:
                print 'Invalid input', e
                continue
            break
    else:
        print ('Error in establishing connection with AWS...')
        sys.exit(0)

# View status of one or many Instances
def statusInstance(region):
    aws = instanceConnection(region)
    if aws is not None:
        reservations = aws.get_all_reservations()
        activeInstances = []

        for reservation in reservations:
            if reservation.instances[0].state == 'running' or reservation.instances[0].state == 'pending':
                instances = reservation.instances
                activeInstances.append(instances)
        if len(activeInstances) != 0:
            for reservation in reservations:
                if reservation.instances[0].state == 'running' or reservation.instances[0].state == 'pending':
                    instances = reservation.instances
                    for instance in instances:
                        print 'Following are the instance information :\n'
                        statuses = aws.get_all_instance_status()
                        print instance, ' State - '
                        print 'Type - ', instance.instance_type
                        print 'Instance ', statuses[0].instance_status, ' System ', statuses[0].system_status
        else:
            print 'There are no available instances.'
            sys.exit(0)
        while True:
            try:
                askUser = raw_input('Options:\n1 Want to terminate instances?\n0 Exit\n')
                if askUser == '0':
                    sys.exit(0);
                elif askUser == '1':
                    terminateInstance(region)
                else:
                    raise ValueError
            except ValueError as e:
                print 'Invalid input', e
                continue
            break
    else:
        print ('Error in establishing connection with AWS...')
        sys.exit(0)

# Terminate one or many Instances
def terminateInstance(region):
    aws = instanceConnection(region)
    reservations = aws.get_all_reservations()
    activeInstances = []
    for reservation in reservations:
        if reservation.instances[0].state == 'running' or reservation.instances[0].state == 'pending':
            instances = reservation.instances[0]
            activeInstances.append(instances)
    print activeInstances

    if len(activeInstances) != 0:
        while True:
            try:
                deleteResponse = raw_input('How many Instances you want to terminate? :\n'
                                           '1 All\n2 individual instance(s)\n0 None - exit\n')
                if deleteResponse == '0':
                    sys.exit(0)
                elif deleteResponse == '1':
                    for instance in activeInstances:
                        instance.terminate()
                    print 'All instances terminated.'
                elif deleteResponse == '2':
                    while len(activeInstances) > 0:
                        instancesToRemove = int(raw_input('Enter number of instances to delete - '))
                        delInstances = []
                        for i in range(0, instancesToRemove):
                            instanceID = raw_input('Enter instance id to terminate - ')
                            delInstances.append(instanceID)
                        aws.terminate_instances(instance_ids=delInstances)
                        print 'Instance(s) terminated.'
                        break
                    break
                else:
                    raise ValueError
            except ValueError as vE:
                print 'Invalid input.', vE
                continue
            break
    else:
        print 'There are no available instances.'
        sys.exit(0)

# -----------------------------------------------
# It starts from here
# -----------------------------------------------
print 'Welcome to EC2 Launcher\n'

# Lists of Available regions on AWS
with open("list_of_region.txt") as f:
    regions = f.readlines()
print 'List of Available regions:'
for n,line in enumerate(regions,1):
    print '{:2}.' .format(n), line.rstrip()
print 'Enter the region\n'
region = raw_input()

# Activity to do - Start/Status/Stop one or many Instances
print 'Want to start or view status of or terminate instance?\n'
response = raw_input()
while True:
    try:
        if response == 'start':
            noOfInstances = int(raw_input('Enter the number of Instances you want :- '))
            startInstance(noOfInstances, region)
        elif response == 'status':
            statusInstance(region)
        elif response == 'terminate':
            terminateInstance(region)
        else:
            raise ValueError
    except ValueError as ve:
        print 'Invalid command.', ve
    break