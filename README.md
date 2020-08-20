# Information Collector v1.3

<p>
 
__*Project dedicated to collecting information in the first stages of a Pentest.<br />
The project is not yet finished, as I am evolving it as I have time, so it will receive several updates yet.*__

</p>

---

## Required libraries and installations

<p>
 
Some libraries are needed, such as: socket, sys, dns.resolver, time, requests.<br />
To install them, just copy and paste the following codes into the terminal, remembering that each version of the pip corresponds to a version of python.

</p>

---

### Installation

`pip3 install sockets`
`pip3 install dnspython`
`pip3 install requests`

---

## What is in the project and what will be implemented?

<p>
 
In the list below, it will be possible to view everything that currently exists in the project and everything that I currently intend to implement.<br />

</p>

---

### What exists and what will come:

 - [x] PortScan.<br />
 - [x] DNS Brute Force 1<br />
 - [x] DNS Brute Force 2<br />
 - [x] DNS Brute Force 3<br />
 - [x] Domain folder discovery<br />
 - [x] Can save the output<br />
 
---

## PortScan Category and Full Category

<p>
 
*Next, I'll talk a little bit about the categories, both the portscan category and the full category, I'll talk a little bit about how it works and about planning.*

</p>

---

### PortScan

<p>
 
Within the PortScan category it is possible to do two types of scans, one with the main ports, and the other complete.<br /><br />
The scan with the main doors presents both the open and closed doors of the desired target, but both are differentiated by color.<br />
In the full scan, it scans all the target's doors, but with a differential from the other, it presents only the open doors.

</p>

---

### Full Category

<p>
 
There are currently two functions in the full category: DNS Brute Force, PortScan and Directory Scan.<br /><br />
The Brute Force DNS has been updated and is now complete. The word lists have also been changed, but can be found at the link below, along with a description of them.<br />
PortScan, on the other hand, scans the main doors, presenting open and closed doors and differentiating them by colors.<br />
The directory scan scans using the large Brute Force DNS word list and shows only the directories found or all directories, depending on the user's choice.<br />

</p>

---

### Planning

<p>
 
 As the entire project plan has already been finalized, I intend only to update it, guaranteeing at least once a week a re-study of the project, to correct problems and updates.<br />
 In addition to adding an executable script to automate the necessary installations.
 
</p>

---

## Links

<p>

__*Here you can find important links!*__

<p>

---

### Word-Lists

<p>

All word lists used in this project were found in the repository [WordLists-20111129](https://github.com/emadshanab/WordLists-20111129), which can be accessed by clicking on the name of the repository.

<p>

---