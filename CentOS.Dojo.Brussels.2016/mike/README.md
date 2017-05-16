# "My Environment Mike"

"My Environment Mike" has his own box that he has tricked out to his
liking.  Mike wants to have his environment connect seamlessly with the
dev tools and for them to stay out of the way.

## Use Case Goal

Demonstrate a developer workstation based docker cli talking to the ADB.

## Script

0. If your local workstation supports docker, run `docker images`
   so you can prove the docker client is talking to the right daemon.
   The presumption is you have images pulled and the ADB doesn't.

1. Install the vagrant-adbinfo plugin

        vagrant plugin install vagrant-adbinfo

2. Run the plugin to get environment variables and certificates

        $ eval "$(vagrant adbinfo)"

3. `docker images`

    Notice there are no images

4. `docker pull busybox`

5. `docker images`

    See busybox

6. `docker run --rm busybox echo "Hello Dojo"`
