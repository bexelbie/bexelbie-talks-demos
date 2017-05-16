# "IDE Igor"

"IDE Igor" has always used an IDE.  He wants to do containers on his
terms.

## Use Case Goal

Demonstrate [Eclipse Docker Tooling](http://www.eclipse.org/community/eclipse_newsletter/2015/june/article3.php) Integration.

## Script

1. Install the vagrant-adbinfo plugin

        vagrant plugin install vagrant-adbinfo

2. Run the plugin to see the environment variables and certificates

        $ vagrant adbinfo

3. Run the plugin to get environment variables and certificates

        $ eval "$(vagrant adbinfo)"

4. Run Eclipse from the same shell as above

    1. In **Docker Explore** view, click **Connection Wizard**

        Notice that the docker connection information is prepopulated.

    2. Click **Test Connection** and verify it works

    3. Click **Finish**

    4. Right-click on **Images** and choose **Pull**.  Image Name is
       **busybox:latest**.  Click **Finish**.  Wait for image to pull.

    5. Expand **Images** and right-click on the **busybox** image.
       Click **Run**.  Give the image a name and the command of
       `echo Hello Dojo`

    6. Click **Finish** and check the **Console View**
