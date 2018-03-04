---
layout: default
title: Metazoa
subtitle: Mostly birds
category: metazoa
---

{% assign metazoalinks = site.categories[page.category] | map: "url" | join: ',' %}

<div class="col-xs-12 col-md-4 bigfont-column"><p id="firstm"></p></div>
<script>
  var metazoa_string = "{{metazoalinks }}";
  var metazoa = metazoa_string.split(',');
  var mfirst = metazoa[metazoa.length - 1];
  var elem = document.createElement("a");
  elem.href = mfirst;
  elem.text = "First";
  elem.setAttribute("class", "btn btn-tall btn-primary btn-block bigfont");
  document.getElementById("firstm").appendChild(elem);
</script>
<div class="col-xs-12 col-md-4 bigfont-column"><p id="randm"></p></div>
<script>
  var metazoa_string = "{{metazoalinks }}";
  var metazoa = metazoa_string.split(',');
  var mrand = metazoa[Math.floor(Math.random() * metazoa.length)];
  var elem = document.createElement("a");
  elem.href = mrand;
  elem.text = "Random";
  elem.setAttribute("class", "btn btn-tall btn-primary btn-block bigfont");
  document.getElementById("randm").appendChild(elem);
</script>
<div class="col-xs-12 col-md-4 bigfont-column" id="latestm"><p id="latestm"></p></div>
<script>
  var metazoa_string = "{{metazoalinks }}";
  var metazoa = metazoa_string.split(',');
  var mlatest = metazoa[0];
  var elem = document.createElement("a");
  elem.href = mlatest;
  elem.text = "Latest";
  elem.setAttribute("class", "btn btn-tall btn-primary btn-block bigfont");
  document.getElementById("latestm").appendChild(elem);
</script>

<div class="col-xs-12 col-md-12 blogpost" markdown="1"> 

Unless otherwise specified, these are all wild animals that were
not baited in any manner. Baiting is limited backyard birdfeeders for
feeder birds and sugary stuff on the pavement for ants. Park or reserve
rules were followed in the capture of all images.

High resolution images if available will be provided on request to educators,
park rangers, wildlife conservancy organizations, close friends, and family.

The full list of animals that I have digitally captured and posted:

{% for post in site.categories[page.category] %}* [{{ post.title }}]({{ post.url }}) - {{ post.date | date: "%B %d, %Y" }} ({{post.mclass}})
{% endfor %}


</div>
