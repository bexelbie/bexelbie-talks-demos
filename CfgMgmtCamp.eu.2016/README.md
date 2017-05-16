# [Nulecule: Packaging, Distributing & Deploying Container Applications the Cloud Way](http://lanyrd.com/2016/cfgmgmtcamp/sdxytt/)
## Presented at [Config Management Camp EU 2016](http://cfgmgmtcamp.eu/schedule/speakers/BrianExelbierd.html) on 2 Feb 2016

This repo contains the slides slides and files used for the talk and demo
I presented about [Nulecule](https://github.com/projectatomic/nulecule).

I am very grateful to my colleagues, [Tomas
Kral](https://www.twitter.com/kadel) and Michael Scherer, for their
assistance with the demos and talk.  I also want to thank [Vaclav
Pavlin](https://twitter.com/vpavlin) for having faith in me to present
when he couldn't.

## Talk Description

Currently there is no standard mechanism for creating, distributing
and deploying applications on containers. Applications that need
orchestration for multiple containers and hosts require hand-crafted
customization that is difficult to replicate and manage, not to mention
time-consuming. Nulecule is a specification for defining the packaged
contents, including metadata, dependencies and orchestration providers, of
container-based applications. Atomic App is the reference implementation
of Nulecule that provides an easy method for packaging, distributing and
running applications. This talk was original scheduled to be delivered
by Vaclav Pavlin.

## [Slides](http://www.winglemeyer.org/bexelbie-talks-demos/CfgMgmtCamp.eu.2016/slides.pdf) [Source File - Download   from Google Docs](slides.pptx)

## Setup Notes

The demo was conducted from a laptop running Fedora 23,
though it could have been run (theoretically) from any
laptop supporting [ansible](http://www.ansible.com/) and
[vagrant](https://www.vagrantup.com/) + a hypervisor.

The demo used to virtual machines.
The machines were both [Atomic Developer
Bundle](https://github.com/projectatomic/adb-atomic-developer-bundle/)
virtual machines.  Specifically there was a [Kubernetes
singlenode](https://github.com/projectatomic/adb-atomic-developer-bundle/tree/master/components/centos/centos-k8s-singlenode-setup)
[CentOS 7](https://www.centos.org/) virtual machine and a [Mesos-Marathon
singlenode](https://github.com/projectatomic/adb-atomic-developer-bundle/tree/master/components/centos/centos-mesos-marathon-singlenode-setup)
CentOS 7 virtual machine.

**Note:** The Mesos-Marathon machine was slightly modified to correct
an upstream bug discovered by [Tomas Kral](https://twitter.com/kadel)
while working on his lab for [DevConf.cz 2016](http://www.devconf.cz/).

### Setup Steps

1. With the Kubernetes Machine

    1. Inject a valid SSH key that will allow passwordless entry by the
       user who will run the ansible playbook.  Don't forget to verify
       it works and save the host.

    2. `docker pull` the following images, if you wish to cache them
       ahead of time:

        * projectatomic/gitlab-centos7-atomicapp : Nulecule Example
        * swordphilic/gitlab : used with the example
        * swordphilic/postgresql : used with the example
        * swordphilic/redis : used with the example

2. With the Marathon Machine

    1. Inject a valid SSH key that will allow passwordless entry by the
       user who will run the ansible playbook.  Don't forget to verify
       it works and save the host.

    2. `docker pull` the following images, if you wish to cache them
       ahead of time:

        * tomaskral/etherpad-atomicapp : Used for the demo as it contains
          patches pending for upstream
        * tomaskral/mariadb-atomicapp : Used for the demo as it contains
          patches pending for upstream
        * centos/etherpad : Used with the etherpad demo
        * centos7/mariadb : Used with the etherpad demo
        * tomaskral/nginx-atomicapp : Used in lieu of
          projectatomic/helloapache as that image was not
          yet rebuilt for the newest version of [Atomic
          App](https://github.com/projectatomic/atomicapp).
        * tomaskral/nonroot-nginx : Used for the hello apache demo

## Demo Script

* Kubernetes Virtual Machine
    * Gitlab Test URL: http://10.2.1.2:30001 (docker)
    * Gitlab Test URL: http://10.2.1.2:30000 (kubernetes)

* Marathon Virtual Machine
    * Marathon URL: http://10.2.2.2:8080
    * Hello Apache (nginx) Test URL: http://10.2.2.2
    * Etherpad Test URL: http://10.2.2.2:9001

### Docker and Kubernetes Demo

1. `ssh vagrant@10.2.1.2`

2. Nothing up my sleeve ...

        docker images
        kubectl get_pods
        docker ps -a

3. Get a Nulecule App we can examine

        atomic run projectatomic/gitlab-centos7-atomicapp --mode fetch

4. Let's try it with some changes

        cp answers.conf.sample answers.conf
        vi answers.conf

    - set port to 30001
    - set provider to docker

5. Run and see the glory of DEBUG output

        atomic run projectatomic/gitlab-centos7-atomicapp .

6. cd to the install directory and show the file tree

        cd /var/lib/atomicapp/projecatomic-gitlab-centos7-atomicapp-*
        find .

7. Become root for edit rights `sudo su`

8. Examine files

    - Dockerfile : Used to build the Nulecule App Container.  Why a
      container? The container gives us a way to delivery application
      metadata using tools already found in the environment.  Why invent
      a new tool to do something we can already do.

    - Nulecule : point out graph, parameters (and attributes/defaults)
      and artifacts

    - artifacts/*/* : point out parameters substitution

    - answers.conf.sample : A default set of answers, ready for editing

9. `docker ps` WOOO!

10. http://10.2.1.2:30001/ WOOO!

11. That was nice and all ... but kill it

        docker rm -f `docker ps -qa`

12. Let's do that again with Kubernetes

13. `atomic run projectatomic/gitlab-centos7-atomicapp --provider kubernetes .`

    We can override stuff on the command line if we want

14. `kubectl get pods` WOOO!

15. `docker ps` WOOO!

16. http://10.2.1.2:30001/ WOOO!

### Mesos-Marathon Demo

1. cd to the ansible directory

2. Show the demo.yml and included .yml files

3. Show the answers.conf files

4. Open Mesos Marathon http://10.2.2.2:8080

5. `ansible-playbook -i inventory demo.yml`

6. See 3 applications start (etherpad, mariadb, nginx)

    **Note:** The nginx process will start fastest.  Test it at
    http://10.2.2.2  The Etherpad will take about 2 min to start as
    it has to do a bunch of `npm` work.  When it works, it will be on
    http://10.2.2.2:9001

## Speaker Bio

Brian Exelbierd (@bexelbie) is a Red Hatter with experience in many
different IS/IT areas, including time in large and small enterprises,
US state government, non-profits and for-profits. Brian joined Red Hat in
2014 to work on platform technologies and containers. An active member of
Project Atomic, Brian has worked closely on the design and implementation
of the Atomic Developer Bundle and has also worked with documentation
and related tasks. Brian lives in Brno, Czech Republic and is happy to
show visitors good adopted-country beer.
