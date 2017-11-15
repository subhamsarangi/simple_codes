import socket
import struct
import textwrap

def main():
    # Capture Packets
    conn = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
    conn.bind(("YOUR_INTERFACE_IP",0))
    conn.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
    conn.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)

    while True:
        raw_data,addr = conn.recvfrom(65536)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        print('\nEthernet Frame:')
        print('Destination: {}, Source: {}. Protocol: {}'.format(dest_mac, src_mac, eth_proto))


# unpack ethernet frame
def ethernet_frame(data):
    dest_mac, scr_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac),get_mac_addr(src_mac), socket.htons(proto), data[14:]

#return properly formatted mac address(i.e. AA:BB:CC:DD:EE:FF)
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_addr).upper()

main()
