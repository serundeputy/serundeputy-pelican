Title: { A useful .gitignore }
Date: 2015-02-07
Category: backdrop


<p>
<img src="https://backdropcms.org/files/Backdrop-Logo-Vertical.png" width="88" alt="Backdrop Logo" style="float: left; margin: 10px;" />
I usually ignore the css files and just version the sass files and compile sass on deploys.<br />
Here is a useful <span class="inline-code">.gitignore</span> file for backdrop:
</p>
<div class="clearfix"></div>
<pre>
<code class="bash">
# Ignore configuration files that may contain sensitive information.
settings.php
sites/*/settings*.php

# Ignore paths that contain user-generated content.
files
private
sites/*/files
sites/*/private

# Ignore sass stuff.
.sass-cache
stylesheets

# Ignore PHPStorm stuff.
.idea
*.idea/*
</code>
</pre>
<p>
tweets away; 
<a href="http://twitter.com/serundeputy">@serundeputy</a>
</p>
