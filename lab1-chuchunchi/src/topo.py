from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
import os

class MininetTopo(Topo):
    def build(self):
        # Add hosts to a topology
        self.addHost("h1")
        self.addHost("h2")
        self.addHost("h3")
        self.addHost("h4")
        # Add switchs to a topology
        self.addSwitch("s1")
        self.addSwitch("s2")
        # Add bidirectional links to a topology, and set bandwidth(Mbps)
        self.addLink("h1", "s1", bw=2)
        self.addLink("h2", "s1", bw=10)
        self.addLink("s1", "s2", bw=5)
        self.addLink("h3", "s2", bw=10)
        self.addLink("h4", "s2", bw=2)
 
if __name__ == '__main__':
    setLogLevel('info')
    if not os.path.isdir("../out/"):
        os.mkdir("../out/")
    # Create a topology
    topo = MininetTopo() 
    # Create and manage a network with a OvS controller and use TCLink
    net = Mininet(
        topo = topo,
        controller = OVSController,
        link = TCLink)
    # Start a network
    net.start()
    
    # iperf
    h1 = net.get("h1")
    h2 = net.get("h2")
    # Use tcpdump to record packet in background
    print("start to record trace in h2")
    h2.cmd("tcpdump -w ../out/h2_output.pcap &")
    # Create flow via iperf
    print("create flow via iperf")
    # TCP flow
    h2.cmd("iperf -s -i 1 -t 5 -p 7777 > ../out/result_s.txt &")
    h1.cmd("iperf -c " + str(h2.IP()) + " -i 1 -t 5 -p 7777 > ../out/result_c.txt &")

    CLI(net)
    net.stop()
