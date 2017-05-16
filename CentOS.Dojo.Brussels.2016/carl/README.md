# "Commandline Carl"

"Command Line Carl" wants a command prompt.  He doesn't want the rest.
His company/wife/budget gave him a box that doesn't run docker or he
doesn't want to pollute his 'email layer.'

## Use Case Goal

This use case works.  This is not new, novel or ground breaking.  This is
basic "hello world" level functionality.

## Script

1. `$ vagrant ssh`

2. `$ systemctl status docker -l`

    Notice that the docker daemon is started and using TLS and is
    configured by default on a unix domain socket and port 2376.

3. `$ docker pull busybox`

    Why busybox?  It is small and we don't want to stress out on
    conference wifi.

4. `$ docker run --rm busybox echo "Hello Dojo"`
