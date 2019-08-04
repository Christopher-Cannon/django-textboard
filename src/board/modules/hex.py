# Function to convert decimals to hexadecimal
def dec_to_hex(num):
    hexa = "0123456789ABCDEF"
    hex_num = ""

    while(num != 0):
        # Determine hex digit from remainder
        hex_num = hexa[num % 16] + hex_num
        # Get the next number
        num = num // 16

    return hex_num

# Return last 6 chars of a string
def truncate(str):
    return str[len(str)-6:len(str)]

# Convert a split decimal IP into a hex IP (form of a list)
def ip_to_hex(dec_ip):
    return [dec_to_hex(int(n)) for n in dec_ip]

# Generate unique poster ID
def get_hex_id(og_ip):
    ip = og_ip.split('.')

    ip.append(int(ip[0]) + int(ip[2]))
    ip.append(int(ip[1]) + int(ip[3]))
    ip.append(int(ip[0]) + int(ip[3]))

    return truncate(''.join(ip_to_hex(ip)))
