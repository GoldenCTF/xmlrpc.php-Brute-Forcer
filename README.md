XMLRPC Fuzzer for Wordpress


Overview


xmlrpcfuzzer.py is a Python script designed to perform a fuzzing attack against the xmlrpc.php endpoint of a Wordpress site. This script attempts to authenticate using the wp.getUsersBlogs method by iterating over a list of potential passwords.

The xmlrpc.php file in a Wordpress installation is an endpoint that enables remote communication with the site. It allows external applications to send commands to your Wordpress site without having to log in through the web interface.

Prerequisites
Python 3
requests library. install with 
```

pip3 install requests

```

Installation
Clone the repository or download xmlrpcfuzzer.py directly.
Ensure the script is executable:
```

chmod +x xmlrpcfuzzer.py

```
Usage
Prepare a wordlist with potential passwords.
Run the script by providing the URL of the target Wordpress site, the username to attempt to log in with, and the path to the wordlist:

```
python3 xmlrpcfuzzer.py -username <username> -w /path/to/wordlist.txt -u http://url.com

```

Arguments
-u, --url: The URL of the target Wordpress site.
-w, --wordlist: Path to the wordlist file containing potential passwords.
-username: Username for which to attempt login.
How It Works
The script sends XMLRPC requests to the xmlrpc.php endpoint, using the wp.getUsersBlogs method. It iterates over the wordlist, using each word as a password in turn. If the script encounters a 403 fault code, it assumes that the attempt was unsuccessful and tries the next password. If a request does not return this fault code, the script assumes the attempt was successful and outputs the correct password.

Disclaimer
Use this script responsibly and only against sites for which you have explicit permission to test. Unauthorized testing can be illegal and unethical.
