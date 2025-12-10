1) Your problem is almost certainly caused by a critical defect in Samsung NVMe drive firmware: **bug 3B2QGXA7** (hereafter — `B†`).
`https://www.google.com/search?q="3B2QGXA7"&pws=0&gl=US`
2) At a certain operating time or load, `B†` forces the device into a **persistent «read-only» mode** or causes it to **freeze** completely.
3) Apparently, the **increased write load** during the **virtual machine migration** you mentioned triggered the manifestation of `B†` across multiple disks.
4) VMware vSAN organizes disks into disk groups, where each group typically consists of **1** **cache tier disk** (hereafter — `C1`) and 1 or more **capacity tier disks** (hereafter — `C2`).
5) The configuration observed on your screenshot (hereafter — `S`) most likely represents a group (**1** `C1` + **4** `C2`). 
6) The observed inconsistent states (specifically, the «In CMMDS/VSI» status showing «**No/No**» for `C2` and «**Yes/Yes**» for `C1`) are characteristic of a severe failure where the system **metadata** is deeply **desynchronized**.
This condition is often referred to as a «**phantom disk group**» or «**stale entries**».
7) **Pattern 1** is observed on `C1`.
It shows «**Metadata Health: Red**» (hereafter — `H-R`) while remaining partially accessible («**Operational health: OK**») and present in the cluster database («**In CMMDS/VSI: Yes/Yes**», hereafter — `VSI-Y`).
`H-R` indicates corruption of critical vSAN metadata stored on this disk, which is essential for the entire disk group.
This corruption likely occurred when `C1` encountered `B†`, causing write operations to fail (e.g. transitioning to read-only mode).
8) **Pattern 2** is observed on `C2`, which show the status «**Unknown disk health**» (hereafter — `H-U`) and «**In CMMDS/VSI: No/No**» (hereafter — `VSI-N`).
`H-U` indicates a failure at the physical communication layer (driver/PSA), meaning the hypervisor cannot query the disk's state.
This strongly suggests that the `C2` disks themselves are physically unresponsive (frozen) due to `B†`.
Furthermore, because `C1` has failed and its metadata is corrupted, the vSAN Local Log Structured Object Manager (LSOM) cannot logically mount these capacity disks, resulting in the `VSI-N` state.
9) It is critical to understand that **all 5 disks are likely physically compromised** by `B†`, as **they are likely identical models from the same batch**.
Therefore, attempting to **reuse any of these disks without remediation** (firmware update or replacement) poses a **critical risk of data loss** and immediate recurrence of `B†`.
10) **You use cheap consumer-grade equipment in your work**, as evidenced by the disk name «Local SAMSUNG Disk» in your screenshot.
This fully matches the profile of affected users describing problems with Samsung 980 Pro in virtualization environments.
11) `B†` manifests differently depending on the role of the disk (cache vs capacity), the load, and the timing of the failure.
11.1) For `C1`, `B†` likely caused it to transition to a state (e.g. read-only) where writes failed, consequently corrupting critical metadata.
It remained accessible enough to maintain a partial registration in the cluster database (`VSI-Y`), leading to the inconsistent state.
11.2) For `C2`, `B†` likely caused them to freeze and become physically unresponsive.
This physical state is a direct cause of `H-U`, indicating a loss of low-level communication with the devices.
Furthermore, `C2` disks are logically inaccessible because the failure of `C1` prevents the vSAN Local Log Structured Object Manager (LSOM) from mounting the disk group.
This combination of physical failure and logical inaccessibility results in the `VSI-N` state.
12) The persistence of the issue after the reboot you described («problem remains») is a characteristic feature of `B†`.
The affected disks transition into a protective mode enforced by their internal controllers.
A server power cycle does not restore their write capability, as the lock is written to the non-volatile memory of the disks themselves.
13) ESXi 7.0.3 uses an updated NVMe driver stack, which is more sensitive to protocol specification violations.
The old `vmklinux` driver might have attempted to reset the device, but the new `nvme-pcie` driver, upon receiving critical errors, immediately stops servicing the device to avoid data corruption.