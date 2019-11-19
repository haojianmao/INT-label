# INT-label:Lightweight In-band Network-Wide Telemetry Without Explicitly Using Probe Packets

Fine-grained, network-wide visibility is vital to reliably maintaining and troubleshooting high-density, mega-scale modern data center networks to accommodate heterogeneous mission-critical applications. However, traditional management protocols, such as SNMP, fall short of highresolution monitoring for highly dynamic data center networks due to the inefficient controller-driven, per-device polling mechanism. With end host-launched full-mesh pings, Pingmesh is capable of providing the maximum latency measurement coverage. Pingmesh is excellent but still flawed. It cannot extract hop-by-hop latency or look into the queue depth inside switches for in-depth analysis, but, for network applications such as load balancing, failure localization and management automation, these underlying information is increasingly insightful. In-band Network Telemetry (INT), one of the killer applications of P4, allows probe or data packets to query device-internal states, such as queue depth and queuing latency, when they pass through the data plane pipeline, which is considered promising and has been embedded into several venders’ latest merchant silicon. As a chip-level primitive, INT simply defines the interaction between the incoming packets and the device-internal states for monitoring. For network-wide telemetry, further orchestration on top of INT is needed.

There are two design patterns to achieve network-wide measurement coverage based on INT, that is, distributed probing and centralized probing. HULA follows the distributed probing and adopts the ToR switches to flood the probes into data center network’s multi-rooted topology for measurement coverage. Since each probe sender does not have the global view of the network to make any coordination, one link will be repetitively monitored by many probes simultaneously with huge bandwidth overhead. For high-resolution monitoring, the bandwidth waste will get even worse. To overcome this limitation, centralized probing relies on the SDN controller to make optimized probing path planning. For example, INT-path collects the network topology and generates non-overlapped probing paths that cover the entire network with a minimum path number using an Euler trail-based algorithm. INT-path is theoretically perfect but still has deployment flaws. First, it still explicitly relies on bandwidth-occupying probe packets. Besides, it embeds source routing into the probe packet to specify the route the probe takes. This makes the probe header even bloated especially for a longer probing path. 

![Image text](https://github.com/Ng-95/INT-label/blob/master/INT_label/Architecture.png)

To tackle the above problems, in this work, we propose INT-label, an ultra-lightweight In-band Network-Wide Telemetry architecture. Distinct from previous work, INT-label follows a “probeless” architecture, that is, the INT-label-capable device periodically labels device-internal states onto data packets rather than explicitly introducing probe packets. Specifically, on each outgoing port of the device, the packets will be sampled according to a predefined label interval T and labelled with the instant device-internal states. As a result, INT-label can still achieve network-wide coverage with finegrained telemetry resolution while introducing minor bandwidth overhead. Along the forwarding path consisting of different devices, the same packet will be labelled independently simply according to the local sample decision, that is to say, INT-label is completely stateless without involving any probing path-related dependency. Therefore, there is no need to leverage the SDN controller for conducting centralized path planning. 

INT-label is decoupled from the topology, allowing seamless adaptation to link failures. Like INT, INT-label also relies on the programmability of data plane provided by P4 and the in-network labelling is designed to be transparent to the end hosts. The INT information will be extracted and sent to the SDN controller at the last-hop network device for network-wide telemetry data analysis. To avoid telemetry resolution degradation due to potential loss of labelled packets on some unreliable links, we further design a feedback mechanism to adaptively change the label frequency when the controller gets aware of the packet loss by analyzing the telemetry result.

