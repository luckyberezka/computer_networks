import argparse
import subprocess
import ipaddress
import validators


def mtu_get(host):
    process = subprocess.run(
        ['cat', '/proc/sys/net/ipv4/icmp_echo_ignore_all'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    if process.stdout == 1:
        print('ICMP ERROR!')
        exit(1)

    left_border = 0
    right_border = 8973
    
    
    process = subprocess.run(
        ["ping", host, '-M', 'do', '-s', str(0), '-c', '1'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    if process.returncode != 0:
        print('HOST NOT RESPONSE!')
        exit(1)

    while left_border != right_border and left_border < right_border - 1:
        middle_value = (left_border + right_border) // 2
        process = subprocess.run(
            ["ping", host, '-M', 'do', '-s', str(middle_value), '-c', '5'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if process.returncode == 0:
            left_border = middle_value
        elif process.returncode == 1:
            right_border = middle_value
        else:
            print('PING ERROR!')
            exit(1)
    return left_border


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('host')
    args = parser.parse_args()
    host = args.host
    if not validators.domain(host):
        try:
            ipaddress.ip_address(host)
        except Exception:
            print('Invalid host!')
            exit(1)
    print('MTU is {}'.format(mtu_get(host) + 28))


if __name__ == '__main__':
    main()
