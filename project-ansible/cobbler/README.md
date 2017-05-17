
**Cobbler** 中主要添加了*httpd/rsync/tftp/dnsmasq*服务。
·所有服务安装在一台服务器上。·

##其中roles的目录结构如下：
├── cobbler
│   ├── handler
│   │   └── main.yml
│   ├── tasks
│   │   ├── conf_cobbler.yml
│   │   ├── install.yml
│   │   ├── main.yml
│   │   └── start.yml
│   └── templates
│       ├── dnsmasq.j2
│       ├── modules.j2
│       └── settings.j2
├── dnsmasq
│   └── tasks
│       ├── cobbler_command.yml
│       ├── install_conf.yml
│       └── main.yml
├── httpd
│   └── tasks
│       └── main.yml
├── init_sys
│   └── tasks
│       └── main.yml
├── rsync
│   └── tasks
│       └── main.yml
└── tftp
    └── tasks
        └── main.yml

