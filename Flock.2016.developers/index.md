<!--Meta author:'Brian (bex) Exelbierd'-->
<!--Meta title:adb-fedora-->
<!--Meta description:'What is the ADB and Why should it be in Fedora'-->
<!--Meta theme:solarized-->
<!--Meta history:true-->
<!--Meta width:1280 height:800-->

<!--sec-->
## Bringing Developers into the Flock

Brian (bex) Exelbierd (@bexelbie) and Dusty Mabe (@dustymabe)

https://github.com/bexelbie/bexelbie-talks-demos/ Flock.2016.developers

Flock @ Kraków, Poland - 3 August 2016

<!--sec-->
## Agenda

- What is the Atomic Development Bundle (ADB)?
- Why should we build it in Fedora?

<!--sec-->
## What the ADB is not?

1. The Asian Develpment Bank - www.adb.org
2. The Android Debug Bridge - developer.android.org

Names are hard!

https://github.com/projectatomic/adb-atomic-developer-bundle/issues/67

<!--sec-->
## What is the ADB?

"The Atomic Developer Bundle (ADB) is a prepackaged development
environment filled with production-grade, pre-configured tools, that makes
container developers' lives easier. The ADB supports the development
of multi-container applications against different technologies and
orchestrators while providing a path that promotes best practices."

<!--sec-->
## Why does someone use the ADB?

- Pre-Configured
- Multiple Environment Support
  - Windows, Linux, Mac OS X
  - OpenShift, Kubernetes, Apache Mesos-Marathon, and plain Docker
  - Language Independent
  - Multiple Development Models: IDE, CLI, and SSH
- Production-Grade
- Self-Contained
- Open Source

<!--sec-->
## So Wait, What is it?

- preconfigured virtual machine
- leverages vagrant and a variety of virtualization providers
- integrated into the environment
  - environment variables/configuration
  - file sharing (vagrant-sshfs)
- easily controlled: vagrant-service-manager

<!--sec1.1-->
## Demo

<!--sec1.2-->
## Docker Only
- Docker isn't running on host
- vagrant up
- vagrant service-manager env
- eval "$(vagrant service-manager env)"
- vagrant service-manager install-cli docker
- docker images
- docker pull fedora
- docker run -it --rm fedora /bin/bash
- cat Dockerfile - just ls a dir
- docker build -t bextest .
- docker run -it --rm bextest
  - error expected
- docker run -it --rm -v $PWD:/workdir bextest
  - success
- vagrant ssh
  - mount
    - notice fuse mount

<!--sec1.3-->
## OpenShift
- vagrant up
- visit https://10.1.2.2:8443/console and login in
  - admin/admin
  - openshift-dev/devel
- vagrant service-manager env
- eval "$(vagrant service-manager env)"
- vagrant service-manager install-cli openshift
  - busted!
- pre-downloaded/openshift-origin-client-tools-v1.2.0-2e62fab-linux-64bit/oc login 10.1.2.2

<!--sec1.4-->
## Vagrant Service-Manager
- vagrant service-manager help

<!--sec-->
## ADB: The Future (only some)

- Persistent Storage
- Landrush (private DNS) instead of xip.io
- Documentation (including publishing and versioning)
- Tests and Test Driven Development
- Vagrant service-manager install-cli extension and bugs
- Vagrant service-manager Windows PowerShell, detection
- Fedora client-side dependencies

<!--sec-->
## Why should we build it in Fedora?

It follows our foundations ...

- Freedom: Free Software
- Friends: Attract developer-users to Fedora
- Features: Help grow (or create a new) development environment
- First: Support advancement with our platform

<!--sec-->
## Freedom: Free Software

# Yes

<!--sec-->
## Friends: Attract developer-users to Fedora

Today, Fedora's developer story is pretty much one of two things:

1. Install our desktop<!-- .element: class="fragment" data-fragment-index="1" -->

2. Use our VM as your desktop<!-- .element: class="fragment" data-fragment-index="2" -->

<!--sec-->
### developer.fedoraproject.org

- A fantastic resource that you should be making better
- Built on the premise that a developer is both:
  - Sitting at a fedora prompt with root access
  - Willing to take ownership of adding software to their machine

<!--sec-->
### Fedora Loves Python

1. Our tools are in python
2. We have python modules (You saw Miroslav Suchý yesterday right?)
3. We are going to work on the Python3 ABI

All of these assume you're using Fedora on your workstation<!-- .element: class="fragment" data-fragment-index="1" -->

<!--sec-->
## Features: Help grow (or create a new) development environment

The ADB aims to be a container development environment built on best practices and the latest tools

So, let's deliver a development environment regardless of what their "email layer" is. (Apologies to @1angdon)

And ... Fedora can make more of these over time<!-- .element: class="fragment" data-fragment-index="1" -->

<!--sec-->
### Remember developer.fedoraproject.org

Here is how node.js is described:

1. dnf install npm
2. dnf install nodejs-&lt;module_name&gt;
3. Read about why npm installs are sub-optimal
4. Link the modules locally by setting a path or running more commands
5. Consider adding more testing repos

<!--sec-->
### We can make this list longer

![atlas.hashicorp.com/fedora](atlas.png)

atlas.hashicorp.com/fedora

<!--sec-->
### What Could this look like?

1. vagrant init fedora/nodejs
2. vagrant up
3. vagrant ssh
4. There is no step 4

You can still use your preferred host editor (think GUI) ...

... and Fedora's node.js

<!--sec-->
## First: Support advancement with our platform

Like Project FAO (Fedora + Atomic + OpenShift) - Fedora Cloud

- ADB size problem
- packaging of binaries, OpenShift, etc.
- Fedora: We move fast!

<!--sec-->
# Questions?

- Brian (bex) Exelbierd (@bexelbie - bex@pobox.com)
- Dusty Mabe (@dustymabe - dusty@dustymabe.com)
- Slides: https://github.com/bexelbie/bexelbie-talks-demos/ Flock.2016.developers
- ADB: https://github.com/projectatomic/adb-atomic-developer-bundle
- Project Atomic: http://www.projectatomic.io/

# Thank You
