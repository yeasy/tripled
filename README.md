TripleD
=======

TripleD -- OpenStack Cloud Detection, Diagnosis and Debug

#About
Do you need to get some useful information with your OpenStack platform?

Are you crazy when the cloud platform behavior abnormally?

TripleD is a tool designed to help analyze your openstack platform intelligently and find problem and try to suggest solution automatically.

#Installation
First, get the installation package from github

`git clone https://github.com/yeasy/tripled.git`

Then install with

`cd tripled; sudo bash ./install.sh`

After the installation, start triple with

`sudo tripled`

#Usage
The usage of TripleD is simple and intuitive.

The supported usage options will shown with the `--h` flag.

```
$sudo tripled
usage: tripled [-h] [--config-dir DIR] [--config-file PATH] [--version]
               [--LOG-log_file PATH]

optional arguments:
  -h, --help            show this help message and exit
  --config-dir DIR      Path to a config directory to pull *.conf files from.
                        This file set is sorted, so as to provide a
                        predictable parse order if individual options are
                        over-ridden. The set is parsed after the file(s)
                        specified via previous --config-file, arguments hence
                        over-ridden options in the directory take precedence.
  --config-file PATH    Path to a config file to use. Multiple config files
                        can be specified, with values in later files taking
                        precedence. The default files used are: None
  --version             show program's version number and exit

Log options:
  --LOG-log_file PATH, --logfile PATH
                        (Optional) Name of log file to output to. If no
                        default is set, logging will go to stdout.

```

##Configuration files
The default configuration file will be installed into `/etc/tripled/tripled.conf`.

Users can manually indicate the configuration file with the `--config-file` option.

A sample configuration file is also included in the package
```
$cat etc/tripled.conf                                                                       
[LOG]
log_file = /var/log/tripled.log
use_stderr = True
logging_default_level = debug

[STACK]
control_nodes = 127.0.0.1
network_nodes = 127.0.0.1
compute_nodes = 10.0.1.101

[CHECK]
system = True
neutron = True
nova = True

[AUTH]
auth_url = http://127.0.0.1:5000/v2.0
username = admin
password = admin
tenant_name = admin
```

#Features

#Todo
