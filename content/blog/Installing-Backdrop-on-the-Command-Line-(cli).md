Title: Installing Backdrop on the Command Line (cli)
Date: 2017-06-29
Category: blog


<p>You can use drush to download and install Backdrop from the command line.<br />
<code>drush dlb backdrop --path="my-backdrop"</code></p>

<p>Change into the directory:<br />
<code>cd my-backdrop</code><br />
You should get an output similar to this:</p>

<p><img alt="" data-file-id="12" src="/images/drush-si-screenshot.png" width="808" /></p>

<p>Use <code class="inline">drush si</code> command to install Backdrop and set up the database.<br />
<code> drush si --db-url="mysql://DB_USERNAME:DB_PASSWORD@localhost/DB_NAME" -y </code></p>

