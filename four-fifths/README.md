<h1>StuyDash</h1>
<h2>By group <a href="#group-four-fifths">four-fifths</a></h2>

<h3>Project: Stuy Student Dashboard - Everything a Stuy student needs.</h3>

<h4>Website Services:</h4>
<ul>
  <li>Intellegent Bell Schedule App
    <ul>
      <li>Detects which bell schedule the current day is</li>
      <li>Displays the proper bell schedule app for the current day</li>
      <li>Information on which period it is (or what periods we are between)</li>
      <li>Displays the current Gym day (A, A1, A2, B, B1, B2)</li>
      <li>Current Temperature and Conditions (as of the page load)</li>
    </ul>
  </li>
  <br/>
  <li>Full Weekly Schedule with link to the post on the Stuy site</li>
  <li>Displays current Stuy news entries with links to their posts</li>
  <li>Quick links to:
    <ul>
      <li><a href="http://stuy.enschool.org">Stuy Homepage</a></li>
      <li><a href="http://www.students-stuyhs.theschoolsystem.net/login.rb">Student Tools<a></li>
      <li><a href="http://schools.nyc.gov/Calendar/default.htm">NYC Calendar</a></li>
      <li><a href="http://www.mta.info">MTA</a></li>
    </ul>
  </li>
</ul>

<h4>Features:</h4>
<ul>
  <li>Convenient text interface</li>
  <li>Mobile Site</li>
  <li>Phone Hotline</li>
</ul>

<h4>Setup:</h4>

<h6>Required Modules ("pip install modulename")</h6>
<ul>
  <li>flask</li>
  <li>beautifulsoup4</li>
  <li>html5lib</li>
  <li>twilio</li>
  <li>ua_parser (download source from <a href="https://github.com/tobie/ua-parser">GitHub</a>)</li>
</ul>

<h6>ua_parser setup</h6>
<ul>
  <li>"git clone https://github.com/tobie/ua-parser.git"</li>
  <li>"cd ua-parser"</li>
  <li>"python setup.py"</li>
  <li>You can then remove the dir ua-parser from your hard drive.</li>
</ul>

<h6>Note: app.py runs on <a href="http://ml7.stuycs.org:7205">ml7.stuycs.org:7205</a>...</h6>

<h4>Known BUGS in the Website<h4>

<ul>
	<li>If the Stuy site is unreachable, StuyDash crashes.</li>
	<li>The favicon's rounded corners show a white background, not a transparent one.</li>
	<li>The date passed in by extractor.py is not necessarily in the right time zone.</li>
	<li>Possible bugs in mobile site's stylesheets.</li>
	<li>No MTA implementation.</li>
</ul>

<h4>GROUP four-fifths:</h4>

<ul>
  <li><strong>Group Leader:</strong> Zachary
    <ul>
      <li>Screen-Scraping (extractor.py)</li>
      <li>Website Design and Construction (app.py and supporting files)</li>
    </ul>
  </li>
  
  <li>Jack
    <ul>
	<li>Twilio API:</li>
    	<li>SMS interface (sendSMS.py)</li>
    	<li>Phone Information Hotline (hotline.py)</li>
    </ul>
  </li>
  
  <li>Cameron
    <ul>
      <li>Weather API (Weather.py)</li>
    </ul>
  </li>
  
  <li>Jason
    <ul>
      <li>MTA API (MTAService.py)</li>
    </ul>
  </li>
</ul>