# Command line for the win

# Project Report: Secure File Transfer Using SFTP

## Overview

The purpose of this project was to solve and learn command line challenges in [Command Challenge](https://cmdchallenge.com/) and securely transfer the screenshots from my Local Terminal to **ALX SOFTWARE ENGINEERING** sandbox environment using the Secure File Transfer Protocol (SFTP) command-line tool. This report outlines the steps taken to achieve the successful transfer, and documents the process and steps taken.

## Project Details

### Prerequisites
In order to successfully transfer from my Local Terminal to the Sandbox environment, the following requirements were met.

- I ensured that SSH connection to my Ubuntu server was established in my local system.
- I ensured that SFTP was installed on the local machine, acknowledging its common inclusion in most Unix-based systems.
- I gathered essential credentials, including the hostname of the sandbox server, the username, and the associated password (__from ALX intranet__) for secure access.
- I ensured the challenge screenshots were present in the local directory(in this case, **_alx-system_engineering-devops/command_line_for_the_win_**).

### SSH Key Generation

Before utilizing SFTP, I generated SSH key using the following command:

```bash

ssh-keygen -b 4096
```

Following the key generation, I connected the public key to the Ubuntu server in my terminal using the directions provided in this page [set up SSH keys](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-20-04).

### Establishing Connection

1. I opened my terminal on the local machine.
2. I executed the SFTP command to initiate a secure connection to the sandbox environment, providing the required credentials:

    ```bash
    sftp username@hostname
    ```

___username@hostname___ being the credentials from the intranet sandbox

I then entered the password when prompted for authentication.

### Navigating to Target Directory

1. Executing the command ```sftp username@hostname ``` connected me to the sftp environment with the prompt **sftp>**.
2. I then moved to the desired directory on the sandbox environment using the `cd` command.
3. I utilized the `ls` command to list available directories for reference.
4. I also, ran some other commands like ```pwd``` etc. for confirmation and references.

### Uploading Files

1. I ran the `put` command to efficiently transfer multiple files with a similar naming pattern:

    ```bash
    put *.png
    ```

2. I then uploaded the `README.md` file separately using the command:

    ```bash
    put README.md
    ```

### Verifying Transfer

1. I confirmed the successful transfer by executing the `ls` command to list files in the sandbox directory.


## Conclusion

The completion of this project demonstrates proficiency in utilizing the SFTP command-line tool for secure file transfers. The meticulous documentation of each step ensures transparency and facilitates a clear understanding of the undertaken process. This report, alongside the integrated steps in the README.md file, provides a comprehensive overview of the steps I took to achieve the desired result. The challenge and the processes it took to set up sftp and upload the files were very tough and challenging, but its worth it. Am glad to have participated in this challenge. I learned a lot.
