Title: { $config->set('nested_stuff', 'new_value'); }
Date: 2015-03-22
Category: backdrop


<img src="https://backdropcms.org/files/inline-images/Drop.png" width="88"  alt="Backdrop Logo" style="float: right; margin-left: 10px; margin-bottom: 10px;" />
<p>
Interested in updating <span class="inline-code">config</span> within nested <span class="inline-code">json</span>?  The documentation on updating the json objects did not reference accessing objects within objects.  So, here is how to do it.
</p>
<p>
Take for example a module: <span class="inline-code">my_module</span> with config in <span class="inline-code">./my_module/config/my_module.settings.json</span>.  Lets define the structure of the settings file:
<div class="my-code">
<code>
{
  &nbsp;&nbsp;  "_config_name": "my_module.settings",
        &nbsp;&nbsp;&nbsp;&nbsp; "layer_one": "eggs",
        &nbsp;&nbsp;&nbsp;&nbsp; "layer_two": {
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"something_in_layer_two": "a thing",
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"another_thing_in_layer_two": "another thing"
     &nbsp;&nbsp;}
}
</code>
</div>
</p>
<p>
<br />
Given this structure accessing <span class="inline-code">'layer_one'</span> is simple and well documented on <a href="https://api.backdropcms.org/converting-modules-from-drupal">api.backdropcms.org</a>, but accessing <span class="inline-code">'something_in_layer_two'</span> requires traversing the <span class="inline-code">json</span> object within its parent object.  This is done with <span class="inline-code">.</span> operators.
</p>
<p>
Load the config file:
<div class="my-code">
<code>

$config = config('my_module.settings');
</code>
</div>
</p>
<p>
<br />
Change the value of <span class="inline-code">'something_in_layer_two'</span>:
<div class="my-code">
<code>

$config->set('layer_two.something_in_layer_two', 'new value');
$config->save();
</code>
</div>
</p>
<p>
<br />
Just glue the <span class="inline-code">keys</span> together with <span class="inline-code">.</span>'s.  Not hard, but if you don't know, you don't know.
</p>
<p>
Hope that helps; follow: { <a href="https://twitter.com/serundeputy">@serundeputy</a>, <a href="https://twitter.com/backdropcms">@backdropcms</a> }. Special thanks to docwilmot who pointed me in the right direction on this.
</p>
