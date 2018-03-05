---
layout: bare
title: Metazoa
subtitle: Mostly birds
category: metazoa
---

{% assign metazoalinks = site.categories[page.category] | map: "url" | join: ',' %}

<div class="container" markdown="1">

<div class="row">
  <div class="col-xs-12 bigfont-column"><p></p></div>
</div>

<div class="row">
  <div class="col-xs-4 bigfont-column" id="firstm"></div>
  <script>
    var metazoa_string = "{{metazoalinks }}";
    var metazoa = metazoa_string.split(',');
    var mfirst = metazoa[metazoa.length - 1];
    var elem = document.createElement("a");
    elem.href = mfirst;
    elem.text = "First";
    elem.setAttribute("class", "btn btn-tall btn-primary btn-block medbigfont");
    document.getElementById("firstm").appendChild(elem);
  </script>
  <div class="col-xs-4 bigfont-column" id="randm"></div>
  <script>
    var metazoa_string = "{{metazoalinks }}";
    var metazoa = metazoa_string.split(',');
    var mrand = metazoa[Math.floor(Math.random() * metazoa.length)];
    var elem = document.createElement("a");
    elem.href = mrand;
    elem.text = "Random";
    elem.setAttribute("class", "btn btn-tall btn-primary btn-block medbigfont");
    document.getElementById("randm").appendChild(elem);
  </script>
  <div class="col-xs-4 bigfont-column" id="latestm"></div>
  <script>
    var metazoa_string = "{{metazoalinks }}";
    var metazoa = metazoa_string.split(',');
    var mlatest = metazoa[0];
    var elem = document.createElement("a");
    elem.href = mlatest;
    elem.text = "Latest";
    elem.setAttribute("class", "btn btn-tall btn-primary btn-block medbigfont");
    document.getElementById("latestm").appendChild(elem);
  </script>
</div>

<div class="row">
  <div class="col-xs-12 col-md-12 bigfont-column"><p></p></div>
</div>


<div class="row" markdown="1">


{% assign counter = 0 %}
{% assign maxPostCount = 10 %}

<div class="col-xs-12 bigfont-column" markdown="1"> 
Here are a few of my most recent captures:
</div>

<div class="col-xs-12 hidden-xs bigfont-column"> 

<table>
<thead>
<tr>
<th>Preview</th>
<th>Title</th>
<th>Date</th>
<th>Class/Superorder</th>
</tr>
</thead>
<tbody>
{% for post in site.categories[page.category] %}
{% if counter < maxPostCount %}
{% assign counter=counter | plus:1 %}
<tr class='clickable-row' data-href='{{post.url}}'>
  <td><img src="/images/metazoa_thumbs/{{post.mimage}}" alt="{{post.title}}" /></td>
  <td>{{ post.title }}</td>
  <td>{{ post.date | date: "%B %d, %Y" }}</td>
  <td>{{post.mclass}}</td>
</tr>
  {% endif %}
{% endfor %}
</tbody>
</table>

</div>

<div class="col-xs-12 visible-xs-block bigfont-column" markdown="1"> 

<table>
<thead>
<tr>
<th>Preview</th>
<th>Title</th>
</tr>
</thead>
<tbody>
{% assign counter=0 %}
{% for post in site.categories[page.category] %}
{% if counter < maxPostCount %}
{% assign counter=counter | plus:1 %}
<tr class='clickable-row' data-href='{{post.url}}'>
  <td><img src="/images/metazoa_thumbs/{{post.mimage}}" alt="{{post.title}}" /></td>
  <td>{{ post.title }}</td>
</tr>
  {% endif %}
{% endfor %}
</tbody>
</table>

</div>

<div class="col-xs-12 bigfont-column" markdown="1"> 
Unless otherwise specified, these are all wild animals that were
not baited in any manner. Baiting is limited backyard birdfeeders for
feeder birds and sugary stuff on the pavement for ants. Park or reserve
rules were followed in the capture of all images.

High resolution images if available will be provided on request to educators,
park rangers, wildlife conservancy organizations, close friends, and family.

The full list of animals that I have digitally captured and posted is
[here](/metazoalist.html).
</div>
</div>

</div>
