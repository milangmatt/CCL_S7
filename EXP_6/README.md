# Virtual Box Installation

## Overview

VirtualBox is a free, open-source hypervisor for running virtual machines (VMs) on desktop and server hosts. It enables you to run multiple operating systems concurrently on a single physical machine for testing, development, or isolation.

Topics covered:
- What virtualization is and common terminology
- Installing VirtualBox on common Linux distributions
- Installing VirtualBox Extension Pack
- Creating and configuring a Windows 10 VM
- Post-installation tasks: Guest Additions, shared folders, networking, snapshots
- Troubleshooting and tips

---

## Virtualization basics

- Hypervisor types:
    - Type 1 (bare-metal): runs directly on hardware (e.g., ESXi).
    - Type 2 (hosted): runs on top of a host OS (VirtualBox, VMware Workstation).
- Key concepts:
    - Guest OS: the OS inside the VM.
    - Host OS: the OS on the physical machine.
    - Virtual hardware: virtual CPU, memory, disk, network, and devices.
    - Virtualization extensions: Intel VT-x / AMD-V required for 64-bit guests and nested virtualization.
- Use cases: development, testing, sandboxing, legacy app support, network labbing.

---

## Prerequisites

- A Linux host with a recent kernel and package manager.
- BIOS/UEFI virtualization enabled (Intel VT-x / AMD-V).
- Sufficient disk space and RAM for host + VM (Windows 10: recommend 40 GB disk, 4–8 GB RAM).
- Windows 10 ISO and valid license (or evaluation ISO from Microsoft).

---

## Installing VirtualBox on Ubuntu

### Step 1: Update your system
```bash
sudo apt update && sudo apt upgrade -y
```

Keeps all packages current and ensures compatibility before adding new software.

### Step 2: Install dependencies
```bash
sudo apt install -y wget curl gnupg software-properties-common
```

These tools are used to fetch, verify, and manage external repositories safely.


### Step 3: Add the Oracle VirtualBox repository
```bash
wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
```

Then add the repo:
```bash
sudo add-apt-repository "deb [arch=amd64] https://download.virtualbox.org/virtualbox/debian $(lsb_release -cs) contrib"
```

Adds Oracle’s official repository so that Ubuntu can install and update VirtualBox directly from it.

### Step 4: Install VirtualBox
```bash
sudo apt update
sudo apt install -y virtualbox-7.0
```

Installs the latest VirtualBox version (v7.0 at the time of writing).

### Step 5: Verify installation
```bash
virtualbox --help
```
Confirms VirtualBox is successfully installed and the command is available.

---

## Creating a Windows 10 VM

1. Create VM
     - Name: Windows 10
     - Type: Microsoft Windows
     - Version: Windows 10 (64-bit)
     - Memory: 4096 MB (4 GB) or more
     - Processors: 2 cores or more (enable PAE/NX if needed)
     - Enable EFI only if using UEFI install media

2. Virtual disk
     - Create a VDI or VHD file, dynamically allocated or fixed.
     - Size: 50 GB+ recommended (40 GB minimum).
     - For performance, consider placing VDI on fast SSD and using fixed-size disks.

3. Storage & ISO
     - Attach Windows 10 ISO to the VM's virtual optical drive in Storage settings.

4. System settings
     - Enable VT-x/AMD-V (Default: VirtualBox uses host extensions; ensure BIOS enabled).
     - Chipset: PIIX3 or ICH9 (PIIX3 is fine for most).
     - Enable 3D acceleration only if you need GUI acceleration (may reduce stability).
     - Video memory: increase to 128 MB for smoother GUI.

5. Network
     - NAT: simplest, VM can access the internet.
     - Bridged: VM appears on same LAN as host (useful for network testing).
     - Host-only: for isolated host-guest networking.
     - Consider adding a second adapter for host-only communication or internal testing.

6. Start VM and install
     - Boot from ISO, follow Windows 10 installer steps.
     - Create user, apply license, install updates.

---

## Post-installation: Guest Additions

- Guest Additions improves graphics, mouse integration, clipboard, shared folders, and folder drag-and-drop.
- From the running VM menu: Devices → Insert Guest Additions CD image...
- Inside Windows: run the Guest Additions installer from the mounted virtual CD and reboot when prompted.

---

## Shared Folders & Clipboard

- Shared folders: configure in VM settings → Shared Folders. Choose Auto-mount and Make Permanent.
- After Guest Additions installation, Windows will gain access to //VBOXSVR/sharename or a mapped network drive.
- Enable bidirectional clipboard/drag-and-drop in Devices menu for convenience (note: not always secure).

---

## Snapshots and Backups

- Use snapshots to capture VM state before risky changes.
- Snapshots are not backups; export appliances for portable backups (File → Export Appliance).
- Keep important data in guest backups or shared folders mapped to host.

---

## Common issues & troubleshooting

- VM shows only 32-bit OS choices: ensure virtualization is enabled in BIOS and host supports VT-x/AMD-V.
- Kernel module build errors: install kernel headers and run /sbin/vboxconfig.
- USB devices not visible: install Extension Pack and add user to vboxusers group, then re-login.
- Slow disk performance: use fixed-size disk or enable host I/O cache where appropriate.
- Network problems: try switching between NAT/Bridged and recreate host-only adapters using VirtualBox network manager.

---

## Security considerations

- Treat VM images like real machines: patch guests, enable firewalls, and avoid exposing administrative services unless necessary.
- Encrypt virtual disks if storing sensitive data (requires Extension Pack).
- Be cautious with shared folders and bidirectional clipboard when working with untrusted guests.

---

## References & further reading

- Official site: https://www.virtualbox.org
- Downloads, manual, and forums accessible from the VirtualBox website
- Distribution-specific packaging and kernel integration docs

---

This README gives a compact guide for installing VirtualBox on Linux and setting up a Windows 10 VM. Adjust memory and disk sizes to match your hardware and workload.