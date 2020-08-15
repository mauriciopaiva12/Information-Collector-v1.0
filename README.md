# Information Collector v1.1

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
In the coming days, I intend to implement the second third of the brute force DNS, containing in this next update a 'medium' size word-list.<br />

</p>

---

### What exists and what will come:

 - [x] PortScan.<br />
 - [x] DNS Brute Force 1<br />
 - [ ] DNS Brute Force 2<br />
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
 
There are currently two functions in the full category: DNS Brute Force and PortScan. <br /> <br />
The DNS Brute Force contains a small word-list, it contains 338 words, that is, it contains 338 attempts at subdomains, presenting only the existing subdomains. <br />
PortScan, on the other hand, scans the main doors, presenting both open and closed doors and differentiating them by color.

</p>

---

### Planning

<p>
 
 I plan to place the second third of the Brute Force DNS as soon as possible, as long as the second third is already ready, the only part that prevents the implementation is that I have not finished the proper word-list for that implementation. <br />
Right after the implementation of the second third of the Brute Force DNS, I will start the cataloging and implementation of the 'large' word-list, which will be specific to the third and last part of the Brute Force DNS. <br />
After the next implementation, I will start studies on how to implement the first third of subdomain discovery, as well as evaluate the main ports and see if there is a need to add a few more ports to expand detection.
 
</p>
