## Experiment 6

#  Virtual Box Installation

### AIM

Install oracle virtual box on top of Ubuntu OS and set up a virtual machine of Windows 10

### STEPS


1. First make  sure that the Ubuntu OS is upto date
2. Install the required dependencies
3. Add oracle vitual box GPG keys
4. Add oracle vitual box repository
5. Install Virtual box
6. Download windows 10 ISO from Microsoft Office website
7. Create a Virtual Machine for Windows 10
    1. Open Virtual Box
    2. Click `New` to create a new virtual machine
    3. Allocate resources for CPU, storage etc..
    4. Choose the Windows 10 ISO
    5. Check start and begin Windows 10  installation


### RESULT

The virtual box installation was done successfully running Windows 10 over Ubuntu OS

### COMMANDS

```bash
sudo apt update
sudo apt upgrade
```

```bash
sudo apt install -y wget curl gnupg software-properties-common
```

```bash
wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
```

```bash
sudo add-apt-repository "deb [arch=amd64] https://download.virtualbox.org/virtualbox/debian $(lsb_release -cs) contrib"
```

```bash
sudo apt update
sudo apt install -y virtualbox-7.0
```