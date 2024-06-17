# Postmortem

This directory, dealing with unscheduled outages is covered.

In the event of a failure of a system, an engineer should be able to deal with the problem and ensure it does not happen again. System-monitoring tools can be put in place to notify the relevant team on outages if they occur.\
A service can be specified that the monitoring tool will be checking for such asnotify if more than 50% of disk space has been used up on the server, if server is serving HTTP requests corrctly and others.\
An on-call management system is set up in such a way that when the monitoring tool detects an anomaly, it alerts the person on call immediately for action to be taken. The on-call person acknowledges the alert once made. The isue can be escalted if alerted person cannot work on the issue at the time or cannot be reached.
