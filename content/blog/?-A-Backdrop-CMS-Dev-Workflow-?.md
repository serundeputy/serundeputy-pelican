Title: { ? A Backdrop CMS Dev Workflow ? }
Date: 2017-08-02
Category: blog


<div style="float: left; margin-right: 9px;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/qybUFnY7Y8w" frameborder="0" allowfullscreen style="height: 315px"></iframe>
</div>
<p>DevOps and Website development can be a daunting and sometimes fragile business. That is where best practices come into play. So when it came time to #redesign <em>serundeputy.io</em> I decided to take advantage of some of the best practices that Backdrop and Web Development at large have to offer.

<ul style="margin-left: 577px;">
	<li><a href="https://docs.lndo.io">Lando</a> ~ Lando is a free, open source and cross-platform local development environment tool built on Docker container technology. It is the successor project to Kalabox.</li>
	<li><a href="https://backdropcms.org">Backdrop CMS</a> Configuration Management ~ Manage site configuration in code.</li>
	<li><a href="http://sass-lang.com/">SASS</a> ~ For quite sometime I've been slumming it with straight <span class="inline-code">css</span> here on <em>serundeputy.io</em>.
 So this was a welcome improvement.</li>
        <li><a href="https://gulpjs.com/">Gulp</a> ~ Solid task management to compile and watch my SASS files!</li>
        <li><a href="https://getcomposer.org/">Composer</a> ~ You heard right; composer with Backdrop! Pull in, manage, and use PHP code from the wild with composer!</li>
</ul>
</p>
<p style="clear: both;">
Let's take a look at how to implement these tools and have a rock solid, development environment, and process that can extend from a team of one to any number of developers. 
</p>

<h3>Lando</h3>
<p>
With a single <code class="bash">.lando.yml</code> file I get a dockerized development stack isolated from my local computer.  Configurable to the service and tooling so I can choose the PHP version, web server, and tools I need for production parity! Get tools like drush; including the backdrop-drush-extension installed and configured for free! #wooooot; Go Lando!  
<br />
Here is the <code class="bash">.lando.yml</code> config file for this site:


<pre>
<code class="yaml">
# Backdrop recipe
name: serundeputy

# Start with the default Backdrop recipe
recipe: backdrop

# Configure the Backdrop recipe
config:

  # See: https://backdropcms.org/requirements

  # Optionally specify the php version to use.
  #
  # If ommitted this will default to the latest php version supported by Backdrop.
  # Consult the `php` service to see what versions are available. Note that all
  # such versions may not be supported in Backdrop 6 so YMMV.
  #
  # See: https://backdropcms.org/requirements
  #
  # NOTE: that this needs to be wrapped in quotes so that it is a string
  #
  php: '7.0'

  # Optionally specify whether you want to serve Backdrop via nginx or apache
  #
  # If ommitted this will default to the latest apache
  #
  # See: https://backdropcms.org/requirements
  #
  # via: nginx

  # Optionally specify the location of the webroot relative to your approot.
  #
  # If ommitted this will be your approot itself.
  #
  webroot: www

  # Optionally specify the version of Backdrush you want for your site
  #
  # This can be either
  #   - `stable`
  #   - `dev`
  #   - `any valid git ref for which there will be a github download` eg 0.0.3
  #
  # If ommitted this will use the stable Backdrush.
  #
  backdrush: stable

  # Optionally specify the database type, this can be one of:
  #
  #   - `mysql`
  #   - `mariadb`
  #
  # If ommitted this will default to the latest mysql. You can additionally provide
  # a version with `type:version` but you will need to consult the documentation
  # for the correct DB service to see what versions are available
  #
  # See: https://backdropcms.org/requirements
  #
  database: mariadb

  # Optionally activate xdebug
  xdebug: true

  # Optionally mix in your own config files
  #
  # If ommitted this will use the default Backdrop config files for the respective
  # services.
  #
  # Definitely consult the relevant documentaion for each service to make sure
  # you are specifying the correct value for the config.
  #
  # conf:
    # server: config/backdrop.conf
    # database: config/mysql
    # php: config/php.ini

services:
  node-cli:
    type: node:6.10
    globals:
      gulp-cli: "latest"

# See: https://docs.lndo.io/config/tooling.html
tooling:
  npm:
    service: node-cli
  node:
    service: node-cli
  gulp:
    service: node-cli
</code>
</pre>
Drop this file into your project root and <code class="bash">lando start</code> and boom! You are up and running.
</p>

<h3>Configuration Management Workflow</h3>
<p>
This one is near and dear to my ?.  Configure views, menu items, layouts, export to code and deploy to production!  Here is how:

<ul>
  <li>Configure a nested web root.  The project root looks like this:</li>
</ul>
<pre>
<code class="bash">  
- serundeputy/
    - config/
        - active/
        - staging/
    - www/
</code>
</pre>
Here the <code class="bash">www/</code> directory is your <code class="php">BACKDROP_ROOT</code> and <code class="bash">serundeputy/</code> is the project and <code class="bash">git</code> root.
<ul>
  <li>Now configure your <code class="bash">settings.php</code> to point at your config directories:</li>
</ul>
<pre>
<code class="lang-php">
$config_directories['active'] = '../config/active';
$config_directories['staging'] = '../config/staging';
</code>
</pre>

I am using the versioned staging directory approach to configuration management and so I have the <code class="bash">staging/</code> under version control and the <code class="bash">active/</code> directory is <code class="bash">.gitignore</code>'d.  Like so:

<pre>
<code class="bash">
# Ignore active config
config/active
</code>
</pre>

Where the <code class="bash">.gitignore</code> file is directly in the project root. Now when you make a configuration change like adding a block to a layout or any configuration change in the Backdrop UI and save it you can export it to code, add it to version control, deploy it, and import it on the production server (or another team members local when they pull new code).

Make a configuration change, for example, change the site name and then export it to code:
<pre>
<code class="bash">
lando drush bcex
</code>
</pre>

Add the newly exported code to git and push up the changes:
<pre>
<code class="bash">
git add -A
git commit -m "Updating site name."
git push origin {branch_name}
</code>
</pre>

Now on the production server pull the code in and import the configuration:
<pre>
<code class="bash">
git pull origin {branch_name}
drush bcim -y
</code>
</pre>

The command <code class="bash">drush bcex</code> is 'Backdrop Configuration Export' command and the <code class="bash">drush bcim</code> is the 'Backdrop Configuration Import' command.
</p>

<h3>Gulp and SASS</h3>

With <code class="bash">lando</code> it is very easy to include tooling and services on a per project basis and that is exactly what I've done here.  At the bottom of the <code class="bash">.lando.yml</code> there is a tooling and services section:

<pre>
<code class="yaml">
services:
  node-cli:
    type: node:6.10
    globals:
      gulp-cli: "latest"

# See: https://docs.lndo.io/config/tooling.html
tooling:
  npm:
    service: node-cli
  node:
    service: node-cli
  gulp:
    service: node-cli
</code>
</pre>

This adds a <code class="bash">npm</code>, <code class="bash">node</code>, and <code class="bash">gulp</code> to the app.  This coupled with the <code class="bash">gulpfile.js</code> allows me to use SASS!  Here is how to watch the SASS files:

<pre>
<code class="bash">
lando gulp
</code>
</pre>

<h3>Composer</h3>
<p>
The previous iteration of this site had a twitter feed with a vertical display of tweets tagged with <code class="bash">#backdropintheevening</code>; the new design called for a horizontal display of those tweets.  I'm sure there were/are plenty of ways I could have CSSd or javascripted the tweets into the horizontal form, but I've been looking for an excuse to play around with the twitter API and this was it.
</p>
<p>
Googling around led me to the conclusion that most PHP developers are using the <code class="bash">abraham/twitteroauth</code> library.  So I decided to use this as well. Pull in the library:
<pre>
<code class="bash">
composer require abraham/twitteroauth
</code>
</pre>
Now I wrote a simple custom module to pull in the library and interact with the twitter API to pull in my tweets and get the markup I needed to make the horizontal display.  At the top of the <code class="bash">serundeputy_tweets.module</code> file is where we pull in the <code class="bash">abraham/twitteroauth</code> it looks like this:
<pre>
<code class="php">
require_once BACKDROP_ROOT . "/../vendor/autoload.php";

use Abraham\TwitterOAuth\TwitterOAuth;
</code>
</pre>
This technique will allow me to pull in any composer library and load up the <code class="bash">autoloader.php</code> and then import the library with a <code class="bash">use</code> statement. Now the module has access the <code class="bash">abraham/twitteroauth</code> and all the functions it provides to interact with the twitter API!
</p>

<h3>Conclusion</h3>
Leveraging the power of modern dev tools I now have a sane, dare I say even fun way, to develop new features and iterations of the <i>serundeputy.io</i> site!  You can see the full source code of the site on GitHub: <a href="https://github.com/serundeputy/serundrop">serundeputy/serundrop</a>.

External links and resources:
<ul>
  <li>Backdrop CMS: <a href="https://backdropcms.org">Backdrop</a></li>
  <li>Lando local dev stack: <a href="https://docs.lndo.io">Lando</a></li>
  <li>Twitter OAuth API Library: <a href="https://twitteroauth.com/">abraham/twitteroauth</a></li>
</ul>
