Title: { Headless Backdrop CMS }
Date: 2015-12-26
Category: backdrop


<p><img alt="drop redirect logo" data-file-id="8" src="/files/inline-images/drop_301_redirect_logo.png" width="111" />&nbsp;Headless is a big deal right?</p>

<p>&nbsp;</p>

<p>The idea is to decouple the CMS from the front end theme, so for example, you can have all the power of Backdrop tools to add content to your site pages, images, blog posts, etc ... and use whatever front end components your front end devs like: {node, ember, angular, ... } whatever floats their boat.</p>

<p>First I wrote a backdrop module that leverages some of the Backrop CMS API functions to deliver some JSON endpoints for the front end app&nbsp;to consume. &nbsp;The module has implementations of:</p>

<ul>
	<li><a href="https://api.backdropcms.org/api/backdrop/core%21modules%21system%21system.api.php/function/hook_menu/1">hook_menu()</a>

	<ul>
		<li>page callback(s)</li>
	</ul>
	</li>
	<li><a href="https://api.backdropcms.org/api/backdrop/core%21includes%21common.inc/function/backdrop_json_output/1">backdrop_json_output()</a></li>
	<li><a href="https://api.backdropcms.org/api/backdrop/core%21includes%21common.inc/function/backdrop_exit/1">backdrop_exit()</a></li>
</ul>

<p>The module creates two end points that deliver JSON Objects. &nbsp;You can see examples of those end points here:</p>

<ul>
	<li>This node
	<ul>
		<li><a href="http://serundrop.staffordtavern.com/api/node/19">http://serundrop.staffordtavern.com/api/node/19</a></li>
	</ul>
	</li>
	<li>All nodes of type page
	<ul>
		<li><a href="http://serundrop.staffordtavern.com/api/list/page">http://serundrop.staffordtavern.com/api/list/page</a></li>
		<li>You can replace 'page' in the URL with any content type that exists on your site. &nbsp;So, for example on this site I have a content type called 'event', so this works:&nbsp;
		<ul>
			<li><a href="http://serundrop.staffordtavern.com/api/list/event">http://serundrop.staffordtavern.com/api/list/event</a></li>
		</ul>
		</li>
	</ul>
	</li>
</ul>

<p>Then you need a front end to consume the results of your API. &nbsp;In this case I used node.js, express and dust. &nbsp;The express app creates endpoints that load in the json objects and flow them throught to template files. &nbsp;In the template files you have access to the JSON object and all of its properties. &nbsp;You have full control over your markup and can surround the JSON properties with whatever kind of markup you want, thus your front end devs are not tied to the markup output by Backdrop CMS, which sometimes gives front devs a headache. &nbsp;Particularly if they are not expert Backdrop/Drupal font end themers.</p>

<p>For example you can see this node (node/19) delivered throught the API, consumed by the express app, and rendered through the dust template here:&nbsp;</p>

<ul>
	<li>http://serundrop.staffordtavern.com:3333/node/19</li>
</ul>

<p>You can see the module code here:</p>

<ul>
	<li>https://github.com/serundeputy/serundrop/blob/master/modules/custom/big/big.module</li>
</ul>

<p>And the express js app here:</p>

<ul>
	<li>https://github.com/serundeputy/serundrop-front/blob/master/app.js</li>
</ul>

<p>Have fun writing your headless Backdrop CMS apps!</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>Follow us on twitter: {<a href="https://twitter.com/serundeputy">@serundeputy</a>, <a href="https://twitter.com/backdropcms">@backdropcms</a>}</p>

<p>&nbsp;</p>

