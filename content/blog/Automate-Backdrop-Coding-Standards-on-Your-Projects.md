Title: { Automate Backdrop Coding Standards on Your Projects }
Date: 2018-07-27
Category: blog


<h2>Backdrop Coder</h2>
<hr />

<p>
<a href="https://packagist.org/packages/backdrop/coder">Backdrop coder</a> is a packagist package that provides a library that <a href="https://packagist.org/packages/squizlabs/php_codesniffer"><span class="inline-code">phpcs</span></a> uses to check your code against the standards defined on <a href="https://api.backdropcms.org">Backdrop CMS API</a> site. To download and use the library is very easy and I'll show you how! Adhering to objective coding standards is a great way to keep your application lean and healthy. It is also an easy way to get started with Continuous Integration (CI) if you and your team have been eyeing that but unable to make the leap.
</p>

<h2>Install the Backdrop Coder Library</h2>
<hr />

To install the <span class="inline-code">backdrop/coder</span> library we will use <a href="https://getcomposer.org/">composer</a> in my case I'm using <a href="https://docs.devwithlando.io">Lando</a> which installs composer for us on all <span class="inline-code">PHP</span> applications.

<p>
<pre>
<code class="bash">
lando composer require backdrop/coder
</code>
</pre>
</p>
<p>
The result of this command is that it downloads the <span class="inline-code">backdrop/coder</span> library and puts it into the <span class="inline-code">vendor</span> directory.
<div style="text-align: center">
<img src="/files/vendor-backdrop-coder.png" width="666" />
</div>

Now we have everything we need to run the code checking against the Backdorp codiing standards! Running this command will test the code in your custom modules:

<pre>
<code class="bash">
lando php vendor/bin/phpcs --standard=vendor/backdrop/coder/coder_sniffer/Backdrop --extensions="module,inc,php" www/modules/custom/
</code>
</pre>

Running the command will return you to command prompt if all is well with the code stanadards.  If it finds errors it will output a report similar to this:

<pre>
<code class="bash">

FILE: /app/www/modules/custom/serundeputy_tweets/serundeputy_tweets.module
--------------------------------------------------------------------------------
FOUND 1 ERROR(S) AFFECTING 1 LINE(S)
--------------------------------------------------------------------------------
 7 | ERROR | Whitespace found at end of line
--------------------------------------------------------------------------------
UPGRADE TO PHP_CODESNIFFER 2.0 TO FIX ERRORS AUTOMATICALLY
--------------------------------------------------------------------------------

</code>
</pre>

This error reports that on line 7 or the serundeputy_tweets.module there is whitespace at the end of a line.  Perfect! Simple to read and to fix.  Just open the file and remove that whitespace.

That is quite a lot to remember to type in order to run your code checking! So, lets wrap that up in a convenient composer script.

</p>


<h2>Configure <span class="inline-code">composer.json</span> and Running the Checks Locally</h2>
<hr />

<p>

Here is a copy of my <span class="inline-code">composer.json</span> file:

<pre>
<code class="json">
{
    "require": {
        "abraham/twitteroauth": "^0.7.4",
        "backdrop/coder": "^1.0"
    },
    "scripts": {
        "test": [ 
            "vendor/bin/phpcs --standard=vendor/backdrop/coder/coder_sniffer/Backdrop --extensions=\"module,inc,php\" www/modules/custom/",
            "vendor/bin/phpcs --standard=vendor/backdrop/coder/coder_sniffer/Backdrop --extensions=\"module,inc,php\" www/themes/serundeputy"
        ] 
    }
}

</code>
</pre>

The important bit for code standards is adding the <span class="inline-code">scripts</span> key with a <span class="inline-code">test</span> key and inside of <span class="inline-code">test</span> we drop two <span class="inline-code">phpcs</span> commands to test the code in <span class="inline-code">www/modules/custom</span> and <span class="inline-code">www/themes/serundeputy</span>, which will test the code in my custom modules and custom theme.

Now to run the whole shebang we just need a simple line:

<pre>
<code class="bash">
lando composer test
</code>
</pre>

Much easier! 

</p>


<h2>Configure CI</h2>
<hr />

Now to add it to our CI process (or make your first CI process if you don't already have one)! I'll use the <a href="https://travis-ci.org/">Travis CI</a> service.  If you don't have a TravisCI account head over there and sign up for one and you can even sign in with your <a href="https://github.com">GitHub</a> account.  Once you are signed into Travis head over to your profile page and enable Travis for your code repo:

<div style="text-align: center;">
  <img src="/files/serundrop-travis.png" width="666" alt="Screenshot of Travis CI config" />
</div>

Now add a <span class="inline-code">.travis.yml</span> config file to the root of your code repo to tell travis what tests to run:

<p>
<pre>
<code class="yaml">
# Configuration file for running the test suite. Results typically at http://travis-ci.org/backdrop/backdrop
# whitelist
language: php
php:
  - 7.0 
before_script:
  - composer install
script: composer test
</code>
</pre>

So you see we are just installing the <span class="inline-code">composer</span> dependencies and then running the same testing command we did locally in CI: <span class="inline-code">composer test</span>.

Here is a failing test run from travis:

<div style="text-align: center;">
  <img src="/files/serundrop-travis-fail.png" width="666" alt="Screenshot of Travis CI run failng" />
</div>

And the corresponding run after fixing the errors:

<div style="text-align: center;">
  <img src="/files/serundrop-travis-pass.png" width="666" alt="Screenshot of Travis CI run passing" />
</div>

Now with each PR you and your team can make sure the code going into the project is up to spec and if you file a PR and it fails you can see that and fix it before you request code review by a human. Everyone is happier!

</p>

<h2>Conclusion</h2>
<hr />

<p>

At first it can seem nit picky and annoying to get started with phpcs and code standards, but at the end of the day you'll end up with leaner, more efficient, self documenting applications. This in turn leads to happier developers, clients, and better productivity and profitability. It is also a low hanging fruit option to get jumpstarted with CI which up the level of your work again.  So for a small amount of work and learning to get started you are forever upping your skill set and deliverables!

I say do it.

References and Tools:
<ul>
  <li><a href="https://packagist.org/packages/backdrop/coder">Backdrop Coder</a> ~ backdrop/coder package on packagist</li>
  <li><a href="https://getcomposer.org">Composer</a> ~ PHP dependency manager</li>
  <li><a href="https://docs.devwithlando.io">Lando</a> ~ Local development environment isolating per app dev tools</li>
  <li><a href="https://packagist.org/packages/squizlabs/php_codesniffer">phpcs</a> ~ squizlabs/php_codesniffer code sniffer</li>
  <li><a href="https://travis-ci.org/">Travis CI</a> ~ Continuous Integration service</li>
</ul>

Follow me on twitter if you are so inclined: <a href="https://twitter.com/serundeputy">@serundeputy</a>.
</p>

<style>
.inline-code {
  font-family: monospace;
}
</style>
