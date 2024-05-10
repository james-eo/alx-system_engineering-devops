# Postmortem: Website Outage Incident

# 500 Internal Server Error

![Postmortem](https://github.com/james-eo/alx-system_engineering-devops/blob/main/0x19-postmortem/postmtm.png)

## Issue Summary:

- **Duration:** May 8, 2024, from 10:00 AM to 12:30 PM (UTC)
- **Impact:** The outage affected all users attempting to access our firm's website during  
the specified timeframe. Users experienced HTTP 500 Internal Server errors and were unable to  
navigate the website. Approximately 80% of users were affected.

## Root Cause:  
The root cause of the outage was traced back to a typo error in the file extension  
of critical PHP files. Files that were supposed to be saved with the extension .php  
were mistakenly saved with the extension .phpp. This error caused Apache2 to  
display "no such file or directory" errors, returning a -1 status code.

![Postmortem analysis](https://github.com/james-eo/alx-system_engineering-devops/blob/main/0x19-postmortem/postmtm1.jpeg)

## Timeline:

- **10:00 AM (UTC):** Issue detected as monitoring alerts indicated a surge in HTTP 500 Internal Server errors on the website.  
- **10:05 AM (UTC):** Engineering team notified of the issue.  
- **10:10 AM (UTC):** Investigation began, focusing on recent changes to the system and server logs.  
- **10:30 AM (UTC):** Initial assumption made that the issue might be related to server misconfiguration or software update.  
- **11:00 AM (UTC):** Further investigation revealed the presence of files with the .phpp extension instead of .php.  
- **11:15 AM (UTC):** Incident escalated to senior engineering team for assistance.  
- **12:00 PM (UTC):** Puppet manifest written to automate the task of correcting file extensions.  
- **12:30 PM (UTC):** Issue resolved after all affected files were renamed to the correct .php extension.  

## Root Cause and Resolution:
The issue originated from a simple typo error where critical PHP files were saved  
with the incorrect .phpp extension. This error caused Apache2 to fail in locating the files,  
resulting in HTTP 500 Internal Server errors. The problem was fixed by writing a Puppet manifest to  
automatically rename files with the .phpp extension to .php.

## Corrective and Preventative Measures:

- ### Improvements/Fixes:  
  - Implement stricter code review processes to catch such errors before deployment.  
  - Enhance monitoring systems to detect file system anomalies and abnormal server behavior.  
  - Conduct regular audits of file extensions across critical systems.

- ### Tasks to Address the Issue:  
  - Implement automated testing scripts to check for file extensions before deployment.
  - Develop a playbook for handling similar incidents in the future, including step-by-step resolution procedures.
  - Conduct a comprehensive review of all critical system configurations to identify and rectify potential vulnerabilities.

## Conclusion:
The website outage incident was caused by a simple yet critical  
typo error in file extensions. Through swift detection and collaboration,  
the issue was resolved, and corrective measures were implemented to prevent similar  
incidents in the future. We remain committed to ensuring the stability and reliability  
of our systems to provide uninterrupted service to our users.
