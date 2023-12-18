---
layout: post
---
# Configuring Logrotate for Apache Server Logs

Logrotate is a system utility that manages the automatic rotation and compression of log files. This is especially useful for web servers like Apache to prevent log files from consuming too much disk space. Here's a guide on how to configure a logrotate script for an Apache server on a Linux system.

## Step 1: Install Logrotate (if not already installed)

Make sure logrotate is installed on your system. You can install it using the package manager for your Linux distribution. For example, on Debian-based systems:

```
sudo apt-get install logrotate
```
## Step 2: Create a Logrotate Configuration File for Apache

Create a logrotate configuration file specific to Apache. Use a text editor to create the file, for example:

```
sudo nano /etc/logrotate.d/apache2
```
Add the following content to the file:

```
/path/to/apache/logs/*.log {
    weekly
    missingok
    rotate 4
    compress
    delaycompress
    notifempty
    create 640 root adm
    sharedscripts
    postrotate
        /etc/init.d/apache2 reload > /dev/null
    endscript
}
```
Adjust the /path/to/apache/logs/ to the actual path where your Apache logs are stored.

Explanation of key directives:

*  **weekly**: Rotate logs on a weekly basis.
*  **missingok**: Don't raise an error if the log file is missing.
*  **rotate** 4: Keep four rotated log files.
*  **compress**: Compress the rotated logs.
*  **delaycompress**: Postpone compression until the next rotation.
*  **notifempty**: Do not rotate the log if it is empty.
*  **create 640 root adm**: Create new log files with specified permissions and ownership.
*  **sharedscripts**: Run postrotate script only once even if multiple log files match.
*  **postrotate**: Command(s) to be executed after log rotation, such as reloading Apache.

## Step 3: Save and Exit

Save the changes to the logrotate configuration file and exit the text editor.
Step 4: Test the Configuration

You can manually test the logrotate configuration by running:

```
sudo logrotate -d /etc/logrotate.conf
```

This will run logrotate in debug mode, showing you what it would do without actually making any changes. Ensure there are no errors in the output.

## Step 5: Automatic Rotation

Logrotate is typically configured to run as a daily cron job. However, you can check your system's cron configuration to confirm. On many systems, logrotate is configured in the /etc/cron.daily/logrotate script.

That's it! You have successfully configured logrotate for your Apache server logs. This will help manage log files efficiently and prevent them from taking up excessive disk space.

### Feel free to customize the paths and configuration options based on your specific Apache setup and preferences.

[/back](./../)