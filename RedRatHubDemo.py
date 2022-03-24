#
# Simple Python test program to use the RedRatHub.
#
# Ethan Johnson, David Blight, Chris Dodge - RedRat Ltd.
#
import RedRatHub
import time

client = RedRatHub.Client()

# Connect to the RedRatHub
client.OpenSocket('10.86.79.113', 40000)

# Send some IR signals
client.SendMessage('"ip="10.86.79.113" dataset="Sky+" signal="9" output="12:10"')
print("Sent signal\n")
time.sleep(2)

client.SendMessage('"ip="10.86.79.113" dataset="Sky+" signal="9" output="12:10"')
print("Sent signal\n")
time.sleep(2)

client.SendMessage('"ip="10.86.79.113" dataset="Sky+" signal="9" output="12:10"')
print("Sent signal\n")
time.sleep(2)

# List the datasets known by the hub
print("List of datasets:")
list = client.ReadData('hubquery="list datasets"')
print(list)

client.CloseSocket()
print("Finished.");
