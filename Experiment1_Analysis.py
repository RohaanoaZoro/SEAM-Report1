import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

# print(os.getcwd())
df = pd.read_csv("E1_train_answers.csv")
groundtruth = pd.read_csv('E1_groundtruth.csv')
firstrow = df.iloc[0].tolist()
# df=df[['Start Date','Response ID','Which group were you assigned to?','A-LEAKED-PRIVILEGE-REMOTE','A-SPOOFING-AUTH—WORKLOAD','A-DOS-WORKERNODE','A-ELEVATION-PRIVILEGE-MALICIOUS-IMG','A-EXPLOIT-PRIVILEGED-CONTAINER','A-PORT-JAMMING-NETWORK-POLICIES','A-LEAKED-SECRET-DOCKERFILE','A-CHAIN-ATTACK-MALICIOUS-INPUTS','A-UNAUTH-CONFIG-TAMPERING','A-SPOOFING-LAYER-3','B-TID1-EXPLOIT-PRIVILEGES-WEB-PODS','B-LEAKED-PRIVILEGE-REMOTE','B-SPOOFING-AUTH—WORKLOAD','B-DOS-WORKERNODE','B-ELEVATION-PRIVILEGE-MALICIOUS-IMG','B-EXPLOIT-PRIVILEGED-CONTAINER','B-PORT-JAMMING-NETWORK-POLICIES','B-LEAKED-SECRET-DOCKERFILE','B-CHAIN-ATTACK-MALICIOUS-INPUTS','B-UNAUTH-CONFIG-TAMPERING','B-SPOOFING-LAYER-3']]

groundtruth = groundtruth[['ID','Real threats?']]

df = df[['GroupA','ExperimentA','ExperimentB']]

groupA = df['ExperimentA']
groupB = df['ExperimentB']
groupA = groupA[1::]
groupB = groupB[1::]

groupA_dict = {}
groupB_dict = {}
groundtruth_dict = {}

for index,row in groundtruth.iterrows():
    groundtruth_dict[row['ID']] = row['Real threats?']

for response in groupA: #going through each users entire response
    if type(response)!=float:
        for option in response.split(','): #going through each option chosen by a user
            id = int(option.split('.')[0])
            if id in groupA_dict:
                groupA_dict[id] += 1
            else:
                groupA_dict[id] = 1

for response in groupB: #going through each users entire response
    if type(response)!=float:
        for option in response.split(','): #going through each option chosen by a user
            id = int(option.split('.')[0])
            if id in groupB_dict:
                groupB_dict[id] += 1
            else:
                groupB_dict[id] = 1
            
# print(groupA_dict)
# print(groupB_dict)
print(groundtruth_dict)

A_correct = [None,None,None,None,None, None]
B_correct = [None,None,None,None,None, None]
groups = [None,None,None,None,None, None]
for i in groundtruth_dict:
    if groundtruth_dict[i]=='Yes':
        if A_correct[i-1]==None and B_correct[i-1]==None and groups[i-1]==None:
          A_correct[i-1] = 43-groupA_dict[i]
          B_correct[i-1] = 43-groupB_dict[i]
          groups[i-1] = i

print(groups)
data = [A_correct,B_correct]
X = np.arange(6)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X + 0.00, data[0], color = 'orange',label='A', width = 0.25)
ax.bar(X + 0.25, data[1], color = 'gold',label='B', width = 0.25)
ax.legend()
ax.set_xticklabels([1]+groups)
plt.xlabel("Threat ID")
plt.ylabel("No. of correctly identified FALSE threats")
plt.show()
print(groupA_dict)
print(groupB_dict)

sum = 0 
for i in groupA_dict:
  if i<=6:
    sum=sum+groupA_dict[i]
meanA = sum/6

sum=0
for i in groupB_dict:
  if i<=6:
    sum = sum+groupB_dict[i]
meanB = sum/6

tempA = 0
for i in groupA_dict:
  if i<=6:
    tempA = tempA + (groupA_dict[i]-meanA)**2
varA = tempA/5

tempB = 0
for i in groupB_dict:
  if i<=6:
    tempB = tempB + (groupB_dict[i]-meanB)**2
varB = tempB/5

denominator = ((5*(varA)**2)+(5*(varB)**2)/6+6-2) * (1/6+1/6)**0.5
t = (meanA-meanB)/denominator
print(t)


