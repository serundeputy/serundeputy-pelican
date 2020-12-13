Title: { Backdrop from Local to Live Server }
Date: 2015-02-05
Category: blog


<img src="https://backdropcms.org/files/inline-images/Backdrop-Logo-Vertical_0.png" width="88" alt="Backdrop Logo" style="float: left; margin: 10px;" />
<p>
You install backdrop, you configure it, theme it, make some modules; how to get it to the server?
</p>
<p>
With the new Configuration Management Initiative (CMI) things are a little different. 
</p>
<p>
My usual steps are to pull in the code base with <span class="inline-code">git</span>:
<div class="my-code">
<code>
git pull origin {your_awesome_branch_name}

</code>
</div>
<br />
Push up your files:
<div class="my-code">
<code>rsync -av files/ user@{server_url:/path/to/backdrop/root/files}

</code>
</div>
<br />
Push up your database:
<div class="my-code">
<code>
mysql -u {your_db_user} -p {awesome_db_name} &lt; {your_sql_dumpfile.sql} -h {database_server_ip_address}

</code>
</div>
</p>
<p>
Then visit my URL.  In this case though it did not work.
<br />
</p>
<p>
Enter <span class="inline-code">settings.php</span> in which you will now find variables that you can point to your chosen config settings directories:
<div class="my-code">
<code>
  $config_directories['active'] = 'files/config_&lt;hash&gt;/active';
  $config_directories['staging'] = 'files/config_&lt;hash&gt;/staging';

</code>
</div>
Point these config variables at your config directory in your <span class="inline-code">files</span> directory and whala website extrodinaire.
</p>
<p>
You will also want to update your database credentials for the server in <span class="inline-code">settings.php</span>:
<div class="my-code">
<code>
$database = 'mysql://{server_db_user}:{db_password}@localhost/serundrop';
$database_prefix = '';

</code>
</div>
</p>
<p>
special thanks to support from <a href="https://twitter.com/jenlampton">@jenlampton</a> and <a href="https://twitter.com/quicksketch">@quicksketch</a> for their mentorship on this issue and <a href="http://backdropcms.org">backdrop</a> in general.
</p>
