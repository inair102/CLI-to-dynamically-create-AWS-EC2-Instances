#CLI to dynamically create AWS EC2 Instances

The following project dynamically creates AWS EC2 Instances by taking command line arguments.<br>

<strong> Working:-</strong><br>
Run the script on a terminal (eg: User$ python aws_ec2_launcher.py)<br>
If the user ran the script and started instances and quit from the program, he/she can again run the script to either view the status or termination of the previous instances, but has enter the correct region for it, else can start new instances too.<br>
Enter the required inputs for:<br>
1. Number of instances<br>
2. Instance region<br>
3. Activities to be performed (start, stop, view status of instance(s))<br>

<strong>Commands</strong>:-<br>
1. start<br>
2. status<br>
3. stop or terminate<br>
4. When asked for region, enter in the displayed format, i.e., for example <strong>us-east-1</strong><br>

The program consists for 4 major functions<br>
1. <strong>instanceConnection()</strong><br>
Takes in the region as input argument and initiates a connection with Amazon AWS.<br>
On line 10 and 11 provide the required access key and secret key.<br>
2. <strong>startInstance()</strong><br>
Takes in the number of isntances and the instance region as input arguments and spins up EC2 instances in the said region.<br>
3. <strong>statusInstance()</strong><br>
Takes in the region as the input argument and displays the status information of the active instances.<br>
4. <strong>terminateInstance()</strong><br>
Takes in the instance region as input argument and asks for either terminating all the active instances or terminate single/multiple instances.<br>

<strong>Limitations:-</strong><br>
1. Not all test cases are taken care of.<br>
2. Case of blank access key and secret access key is not handled.<br>
3. Handling of 0 instances is not taken into consideration.<br>