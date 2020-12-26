Title: { git patches, apache modules and vagrant }
Date: 2015-04-04
Category: backdrop


<img src="/files/bd-git-apache-drupal-vagrant.png" width="161px" alt="Backdrop Logo" style="float: left; margin-right: 19px;" />
<p>
The motivation for this post are these two use cases. 
<ul>
<li><a href="https://github.com/backdrop/backdrop-issues/issues/681">https://github.com/backdrop/backdrop-issues/issues/681</a></li>
<li><a href="https://www.drupal.org/node/1599774">https://www.drupal.org/node/1599774</a></li>
</ul>
which revolve around syntax changes from Apache 2.2 to Apache 2.4.  
<br />
In Apache 2.2 the syntax is: 
<div style="text-align: center;">
<span class="inline-code">
Order allow,deny
</span>
</div>
is changing to:
<div style="text-align: center;">
<span class="inline-code">
Require all denied
</span>
</div>
in Apache 2.4
</p>
<p>
Now if you are using apache 2.4 and you have the <span class="inline-code"><a href="http://httpd.apache.org/docs/2.4/mod/mod_access_compat.html">mod_access_compat</a></span> enabled then that does not really matter, but if it is not enabled and you use the old syntax it will break your site.
</p>
<p>
So to test these patches I needed to have Apache 2.2/Apache 2.4, mod_access_compat enabled/disabled, and patched/unpatched versions of backdrop and drupal.  Enter <a href="https://www.vagrantup.com/">Vagrant</a>.  Vagrant gave me a virtual environment where I could easily switch in and out these components without breaking the 50+ dev sites I have going on my local machine.  It is a completely isolated sandbox that if I break apache in the VM I don't break it for every site I'm working on just that VM.
</p>
<p>
I used the <a href="http://www.drupalvm.com/">drupal vm</a> vagrant box, by <a href="http://jeffgeerling.com/">Jeff Geerling</a> which you can quickly download, configure and <span class="inline-code">vagrant up</span> and have a working <span class="inline-code">LAMP</span> stack that includes <span class="inline-code">Apache 2.4</span>.
</p>
<p>
Now to enable/disable the apache modules use (on Ubuntu/Debian):
<div style="text-align: center;">
<span class="inline-code">sudo a2dismod -f access_compat</span>
</div>
<br />
<br />
that will disable the <span class="inline-code">access_compat</span> module.  Then you need to restart apache for the changes to take effect.
<div style="text-align: center;">
<span class="inline-code">sudo service apache2 restart</span>
</div>
Now in this configuration if you download backdrop or drupal and install them (or try to through the gui) you get <span class="inline-code">500 Internal server error</span>.  Apply the patch and you will not get a <span class="inline-code">500</span>. 
</p>
<p>
<h3>Applying the Patch</h3>
Download the patch to the root of your backdrop install:
<div style="text-align: center">
<span class="inline-code">wget https://github.com/backdrop/backdrop/pull/808.patch</span>
</div>
Apply the patch:
<div style="text-align: center;">
<span class="inline-code">git apply 808.patch<span>
</div>
To reverse the patch:
<div style="text-align: center;">
<span class="inline-code">git apply -R 808.patch</span>
</div>
</p>
<p>
Tweet out your questions/comments <a href="http://twitter.com/serundeputy">serundeputy</a>.
</p>
