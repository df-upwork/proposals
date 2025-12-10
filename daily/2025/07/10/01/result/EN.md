1) Run `docker compose logs --follow gvmd ospd-openvas`, and then start a new scan in another terminal.
This will display the real-time logs for two key services in the Greenbone Vulnerability Management (GVM) architecture:
1.1) `ospd-openvas` (OSPD daemon for OpenVAS).
This is the scanner itself.
Its logs are the most important because the actual error is most likely to occur here (e.g., a problem accessing plugins, an incorrect configuration, or a failure at startup).
1.2) `gvmd` (Greenbone Vulnerability Manager Daemon).
This is the central management service.
Its logs will show how it initiates the scan, passes the task to the scanner, and why it registers the failure with the message «interrupted at 0%».
2) Reviewing the logs of 1.1 and 1.2 provides a complete picture of the interaction between the management component and the executor.
This is the most effective way to determine the cause of the scan failure.
---
I have completed 536 projects here on Upwork.
My GitHub profile: https://github.com/dmitrii-fediuk
My websites: https://df.tips?order=views, https://mage2.pro?order=views, https://dmitry.ai?order=views