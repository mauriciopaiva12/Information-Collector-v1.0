# Information Collector v1.2

<p>
 
__*Project dedicated to collecting information in the first stages of a Pentest.<br />
The project is not yet finished, as I am evolving it as I have time, so it will receive several updates yet.*__

</p>

---

## Required libraries and installations

<p>
 
Some libraries are needed, such as: socket, sys, dns.resolver, time.<br />
To install them, just copy and paste the following codes into the terminal, remembering that each version of the pip corresponds to a version of python.

</p>

---

### Installation

`pip3 install sockets`
`pip3 install dnspython`

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
 - [ ] DNS Brute Force 3<br />
 - [ ] Domain folder discovery 1<br />
 - [ ] Domain folder discovery 2<br />
 - [ ] Domain folder discovery 3<br />
 - [ ] Can save the output<br />
 
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
 
There are currently two functions in the full category: DNS Brute Force and PortScan.<br /><br />
The DNS Brute Force contains two word lists, one 'small', which contains 338 words and the other 'average', which contains 601 words, both presenting only the existing subdomains.<br />
PortScan, on the other hand, scans the main doors, presenting open and closed doors and differentiating them by colors.

</p>

---

### Planning

<p>
 
 I intend to put the last part of Brute Force DNS in the next few days, the last part of Brute Force DNS is ready, the only part that prevents the implementation is that I still don't have the proper word list for that implementation.<br />
As I implemented the second third of the DNS Brute Force, I will already start searching and cataloging a 'big' list of words.<br />
I intend to set up a program that automates this process and that tries to guarantee the absence of repeated words in the word list.<br /><br />
After the next implementation, I will start studies on how to implement the first third of subdomain discovery, as well as assess the main ports and see if there is a need to add a few more ports to expand detection.
 
</p>
