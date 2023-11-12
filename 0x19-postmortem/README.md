# Postmortem: Apache 500 Error Outage

## Issue Summary

**Duration:** 
- Start Time: [00:00] (UTC)
- End Time: [00:50] (UTC)

**Impact:**
- The Apache 500 error resulted in a service disruption for the Wordpress website running on a LAMP stack.
- Users experienced inability to access the website and encountered HTTP 500 Internal Server Error.
- Approximately [100%] of users were affected during the outage.

**Root Cause:**
- The root cause of the issue was a misconfiguration in the `wp-settings.php` file, specifically related to a typo in the path to the PHP files.

## Timeline

- **Detection:**
  - Start Time: [00:00] (UTC)
  - The issue was initially detected through monitoring alerts indicating a spike in HTTP 500 errors on the server.
  
- **Investigation:**
  - Actions Taken: [00:10] (UTC)
    - An engineer initiated an investigation into the logs to identify the source of the error.
    - Restarting apache2 do not fix the issue
    - Initial assumptions pointed towards potential issues with PHP configurations or the Apache server.
    - Misleading paths: Investigations initially focused on PHP configurations, leading to time spent exploring unnecessary paths.
    
- **Escalation:**
  - The incident was escalated to the DevOps team as the investigation revealed a server-side misconfiguration: [00:30] (UTC)
    - using Strace we identified the issue as a typo in the path to a PHP file
  
- **Resolution:**
  - Actions Taken: 
    - A Puppet manifest (`0-strace_is_your_friend.pp`) was created to fix the misconfiguration.
    - The manifest corrected the path typo in the `wp-settings.php` file, resolving the Apache 500 error.
  - End Time: [00:50] (UTC)

## Root Cause and Resolution

**Root Cause:**
- The root cause of the Apache 500 error was traced to a typo in the path to PHP files within the `wp-settings.php` file. The incorrect path led to the server's inability to locate the necessary PHP files, resulting in the HTTP 500 Internal Server Error.

**Resolution:**
- The issue was resolved by creating a Puppet manifest (`0-strace_is_your_friend.pp`) that executed the command: `sed -i s/phpp/php/g /var/www/html/wp-settings.php`. This corrected the path typo in the `wp-settings.php` file, eliminating the misconfiguration causing the Apache 500 error.

## Corrective and Preventative Measures

**Improvements/Fixes:**
- Regular code reviews for configuration files to catch potential typos or misconfigurations.
- Implement automated testing for critical paths to ensure configurations are correct.

**Tasks:**
- Establish a comprehensive monitoring system for Apache logs and PHP errors.
- Conduct a thorough review of all configuration files for potential errors.
- Implement a Puppet manifest to automate the correction of known misconfigurations.
- Schedule regular training sessions for the team to enhance troubleshooting skills.
- all servers should be tested localy before deployment

## Conclusion

In conclusion, the Apache 500 error was swiftly addressed by identifying and correcting a misconfiguration in the `wp-settings.php` file. The incident highlighted the importance of rigorous monitoring, quick detection, and automated corrective measures to minimize downtime and improve system resilience. The outlined corrective and preventative measures aim to enhance system robustness and prevent similar issues in the future.
