HA on a Juniper SRX300 pair is done as follows:
1) Connect `ge-0/0/1` (node0) with `ge-1/0/1` (node1) for the control link.
2) Connect `ge-0/0/7` (node0) with `ge-1/0/7` (node1) for the fabric link.
3) Connect 4G modems: I recommend 2 modems (one for each node) to physically provide 4G on both SRX devices.
4) Connect multiple ports (for LAG) from each SRX300 to the Cisco Catalyst stack.
5)
```
set system host-name srx300-node0
set system root-authentication plain-text-password
set system services ssh
```
6) On the primary SRX300, configure the chassis cluster:
6.1) If the SRX is still in standalone mode, then enable the cluster:
```
set chassis cluster cluster-id 1 node 0 reboot
commit
```
After the reboot, switch to the cluster mode, and interfaces will be renamed to the format `ge-0/0/x`, `ge-1/0/x`.
6.2)
```
set chassis cluster cluster-id 1 node 0
set chassis cluster reth-count 2
set chassis cluster redundancy-group 0 node 0 priority 200
set chassis cluster redundancy-group 0 node 1 priority 100
set chassis cluster redundancy-group 1 node 0 priority 200
set chassis cluster redundancy-group 1 node 1 priority 100
set chassis cluster redundancy-group 1 node 0 interface-monitor ge-0/0/2 weight 255
set chassis cluster redundancy-group 1 node 0 interface-monitor ge-0/0/0 weight 255
set chassis cluster redundancy-group 1 node 1 interface-monitor ge-1/0/2 weight 255
set chassis cluster redundancy-group 1 node 1 interface-monitor ge-1/0/0 weight 255
set chassis cluster control-link ge-0/0/1
set chassis cluster cluster-id 1 node 0 fabric-link ge-0/0/7
commit check
commit
request system reboot
```
Wait for the reboot to complete.
7) On the secondary SRX300 (node1) configure the chassis cluster:
7.1) If the SRX is still in standalone mode, first enable the cluster (similar to 6.1):
```
set chassis cluster cluster-id 1 node 1 reboot
commit
```
7.2)
```
set chassis cluster cluster-id 1 node 1
set chassis cluster control-link ge-1/0/1
set chassis cluster cluster-id 1 node 1 fabric-link ge-1/0/7
commit check
commit
request system reboot
```
8) Configure redundant Ethernet interfaces:
```
set interfaces reth0 redundant-ether-options redundancy-group 1
set interfaces reth0 aggregated-ether-options lacp active
set interfaces reth0 aggregated-ether-options minimum-links 1
set interfaces reth0 unit 0 family inet address 192.168.1.254/24

set interfaces reth1 redundant-ether-options redundancy-group 1
set interfaces reth1 aggregated-ether-options lacp active
set interfaces reth1 unit 0 family inet address 10.0.0.254/30
```
9) Bind physical interfaces to the redundant interfaces:
```
set interfaces ge-0/0/0 gigether-options redundant-parent reth0
set interfaces ge-1/0/0 gigether-options redundant-parent reth0
set interfaces ge-0/0/2 gigether-options redundant-parent reth1
set interfaces ge-1/0/2 gigether-options redundant-parent reth1
```
10) Configure a 4G interface on the primary SRX300 (PPP):
```
set interfaces pp0 unit 0 family inet negotiate-address
set interfaces pp0 unit 0 ppp-options chap access-profile 4g-profile
set interfaces pp0 unit 0 ppp-options pap access-profile 4g-profile
set access profile 4g-profile authentication-order [ chap pap ]
set access profile 4g-profile client [username] secret [password]
```
11) Configure a backup route over 4G:
```
set routing-options static route 0.0.0.0/0 qualified-next-hop 10.0.0.253 preference 10
set routing-options static route 0.0.0.0/0 next-hop pp0.0 preference 20
```
12) Configure `ip-monitoring` to check the main link:
```
set services ip-monitoring enable

set services ip-monitoring policy MAIN-LINK test test1 probe-count 5
set services ip-monitoring policy MAIN-LINK test test1 test-interval 5
set services ip-monitoring policy MAIN-LINK test test1 target 8.8.8.8
set services ip-monitoring policy MAIN-LINK test test1 source-interface reth1.0

set services ip-monitoring policy MAIN-LINK then preferred-route route 0.0.0.0/0 next-hop 10.0.0.253 qualified-next-hop pp0.0
set services ip-monitoring policy MAIN-LINK then failover-route route 0.0.0.0/0 next-hop pp0.0
```
13) Configure DNS servers for the main link:
```
set system name-server 8.8.8.8
set system name-server 8.8.4.4
```
14) Configure DNS forwarding with automatic switching:
```
set system services dns forwarding server 8.8.8.8
set system services dns forwarding server 8.8.4.4

set event-options policy primary-down events chassiscluster_status_change
set event-options policy primary-down within 30
set event-options policy primary-down match "RG1: node0 lost the primary role"
set event-options policy primary-down then execute-commands commands "delete system services dns forwarding server 8.8.8.8"
set event-options policy primary-down then execute-commands commands "delete system services dns forwarding server 8.8.4.4"
<…>
```
Since Upwork limits a proposal to 5000 characters, I published the rest on my website: https://df.tips/t/2610
