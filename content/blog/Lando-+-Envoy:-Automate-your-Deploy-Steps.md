Title: { Lando + Envoy: Automate your Deploy Steps }
Date: 2018-07-29
Category: blog


<h2>Why Envoy</h2>
<hr />
<p>
About 4 or 5 years ago a colleague <a href="https://twitter.com/jacksonhoose">@jacksonhoose</a> introduced me to deploy technology called Envoy. At that time I was not ready to hear, explore, and adopt it. I was steeped in a world of ruby, compass, capistrano, and who knows what, but about 6 months ago Envoy came back on my radar and this time I was ready!

<a href="https://laravel.com/docs/5.6/envoy">Envoy</a> is a task runner put together by the <a href="https://laravel.com">Laravel</a> team. When I can I like to use hosts like Pantheon and Platform.sh that give me a wealth of tools, containers in production, and a lot less DevOps headaches when something like <a href="http://heartbleed.com/">Heartbleed</a> happens ?. 

That said not all clients can afford the hosting costs of these providers ?. And then <a href="https://linode.com">Linode</a>, <a href="https://www.digitalocean.com">Digital Ocean</a>, or <a href="https://aws.amazon.com/what-is-cloud-computing/?sc_channel=PS&sc_campaign=acquisition_US&sc_publisher=google&sc_medium=ACQ-P%7CPS-GO%7CBrand%7CSU%7CCore%7CCore%7CUS%7CEN%7CText&sc_content=sitelink&sc_detail=aws&sc_category=core&sc_segment=what_is_cloud_computing&sc_matchtype=e&sc_country=US&s_kwcid=AL!4422!3!280392801017!e!!g!!aws&ef_id=WgzYSgAAAGNYiE_V:20180729121503:s">AWS</a> become good choices starting at as little as $5/mo. So when working on your family member or friends website with affordable hosting we can use <span class="inline-code">envoy</span> to automate our deploy steps and get some of that deploy consistency that we know and love from the big hosting providers.

This post will show you how to add <span class="inline-code">envoy</span> as tooling to <a href="https://docs.devwithlando.io">Lando</a>. The particular app in this example is <a href="https://backdropcms.org">Backdrop CMS</a>, but any PHP app can take advantage of Envoy, really any app (but non PHP devs prolly not looking for ways to add PHP to the mix ?).  Apps like WordPress, Symfony, Backdrop, Drupal, and of course Laravel are a perfect fit.
</p>

<h2>Install Envoy</h2>
<hr />

<p>
To add <span class="inline-code">envoy</span> tooling to your <span class="inline-code">.lando.yml</span> file add the following <span class="inline-code">run</span> step:

<pre>
<code class="yaml">
services:
  appserver:
    run:
      - cd $LANDO_MOUNT && composer install
      - composer global require laravel/envoy

</code>
</pre>

And a corresponding <span class="inline-code">tooling</span> entry:

<pre>
<code class="yaml">
# See: https://docs.lndo.io/config/tooling.html
tooling:
  envoy:
    service: appserver
</code>
</pre>

Now we are ready to start using Envoy, but first let's configure it.

</p>

<h2>Configure Envoy</h2>
<hr />
<p>
To use Envoy you will set up a file in the root of your project called: <span class="inline-code">Envoy.blade.php</span>. Here is mine:

<pre>
<code class="php">
@servers(['web' => ['USER@SERVER_IP']])

@task('ll', ['on' => 'web'])
  cd /var/www/serundeputy
  ls -alh
@endtask

@task('deploy', ['on' => 'web'])
  cd /var/www/serundeputy
  @if ($branch)
    git pull origin {{ $branch }}
  @endif
  composer install
  cd /var/www/serundeputy/www
  drush updb -y
  drush bcim -y
  drush cc all
@endtask
</code>
</pre>

The <span class="inline-code">Envoy.blade.php</span> file uses Laravel blade syntax and in it we define <span class="inline-code">servers</span> array and some <span class="inline-code">task</span>s.  In this example you'll want to replace <span class="inline-code">USER</span> with a user that has <span class="inline-code">ssh</span> access to the server in question and <span class="inline-code">SERVER_IP</span> with the <span class="inline-code">ip address</span> of the server you are deploying to.

In the <span class="inline-code">deploy</span> task we simply write the shell commands that we want to happen for our app.  In this case move to the app directory, run composer install, and some drush commands. That is it, so simple! 

You don't have to worry about different people doing different steps, forgetting steps, or typing something incorrectly. Consistency and peace of mind ☮️.

You can define as many or few <span class="inline-code">task</span>s as you need. For example you could break out the deploy task to separate <span class="inline-code">deploy-staging</span> and <span class="inline-code">deploy-production</span> tasks.

</p>


<h2>Run an Envoy Deploy</h2>
<hr />
<p>
Now that we have our tasks set up in our <span class="inline-code">Envoy.blade.php</span> file we can run them. For example to <span class="inline-code">deploy</span> run:

<pre>
<code class="bash">
lando envoy run deploy --branch=master
</code>
</pre>

Running this one command runs all the tasks in the <span class="inline-code">deploy</span> task!

</p>

<h2>Conclusion</h2>
<hr />
<p>

Consistency. No need to ssh into the server. No danger of running unwanted commands on the server. No leaving the shell open on a production server session for your cat to walk across your keyboard ?. Just the things you want and need to happen for your app.

Tools and Resources:
<ul>
<li><a href="https://laravel.com/docs/5.6/envoy">Envoy</a> ~ Run tasks on your remote servers.</li>
<li><a href="https://docs.devwithlando.io">Lando</a> ~ A flexible local dev environment based on docker.</li>
</ul>

If you are so inclined follow me on twitter: <a href="https://twitter.com/serundeputy">@serundeputy</a>.

</p>


<style>
.inline-code {
  font-family: monospace;
}
</style>
