Title: { Tracking Backdrop CMS Core Repo }
Date: 2015-03-15
Category: backdrop


<img src="/files/inline-images/drop_301_redirect_logo.png" width="88" alt="Backdrop Logo" style="float: left; margin-right: 10px;" />
<p>
If you are developing for backdrop core <a href="https://github.com/backdrop/backdrop">gihtub.com/backdrop/backdrop</a> the process is to fork the backdrop repo <span class="inline-code">git checkout Issue&#35;/human-readable-description-of-issue</span>.  {hack, hack, hack, hack} Fix the issue.  Add and commit your changes to your new branch.  Push your new branch to your forked repo on github and make a pull request (<span class="inline-code">PR</span>) against the canonical backdrop repo <span class="inline-code">backdrop/backdrop</span>.
</p>
<p>
This process is well documented in the <a href="https://backdropcms.org/develop/pull-requests">backdrop handbook</a>.
</p>
<p>
But what happens when your repo is out of sync with the backdrop core repo?  If you forked <span class="inline-code">1.x</span> when backdrop was at <span class="inline-code">1.0.2</span> and now backdrop is on <span class="inline-code">1.0.4</span> if you follow the above process you could end up with <span class="inline-code">merge conflicts</span> in your <span class="inline-code">PR</span>.
</p>

<p>
What you want to do is have your repo track the <span class="inline-code">backdrop/backdrop</span> repo.  First set up your <span class="inline-code">git</span> repo to track the <span class="inline-code">backdrop/backdrop</span> repo.  Add these lines to your <span class="inline-code">.git/config</span> file:
</p>
<p>
<div class="my-code">
<code>
[remote "core"]
  url = https://github.com/backdrop/backdrop.git
  fetch = +refs/heads/*:refs/remotes/core/*

</code>
</div>
</p>
<p>
these lines let your fork keep track of the canonical <span class="inline-code">backdrop/backdrop</span> repo.
</p>
<p>
Now if your repo falls behind the core <span class="inline-code">backdrop/backdrop</span> repo and you want to work on an issue you'll need to catch up.  To do that <span class="inline-code">fetch</span> the latest <span class="inline-code">core/1.x</span> that you are now tracking and merge into your forked <span class="inline-code">1.x</span> branch before making your issue branch and filing the <span class="inline-code">PR</span>.  That process looks like this:
<div class="my-code">
<code>
git fetch core
git checkout 1.x
git merge core/1.x

</code>
</div>
Now your code is up to date with the latest and greatest backdrop core code and filing your <span class="inline-code">PR</span> should be conflict free.
</p>

<p>
Hope this helps!  Come help us out in the <a href="https://github.com/backdrop/backdrop-issues/issues">backdrop issue queue</a> and file some <span class="inline-code">PR</span>s.  It's fun and rewarding.
<br /><br />
Follow us on twitter: { <a href="https://twitter.com/serundeputy">@serundeputy</a>, <a href="https://twitter.com/backdropcms">@backdropcms</a> }.
</p>

