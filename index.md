---
layout: default
title: Eric Appelt
subtitle: Software, Science, and Stuff
---

<div class="col-xs-12 col-md-6 bigfont-column"> 
  <p id="randm"></p>
</div>
<script>
  var metazoa_string = "{{site.data["metazoa"] | join: ',' }}";
  var metazoa = metazoa_string.split(',');
  var mrand = metazoa[Math.floor(Math.random() * metazoa.length)];
  var elem = document.createElement("img");
  elem.src = mrand;
  elem.setAttribute("alt", "random metazoan");
  elem.setAttribute("class", "img-responsive center-block framed-image");
  document.getElementById("randm").appendChild(elem);
</script>

<div class="col-xs-12 col-md-6 bigfont-column" markdown="1"> 

### A collection of photos and writing

This is my small personal and demonstration website. Here you can:
* read a little bit [about me](/about.html),
* read some things that I have [written](/writing.html), or
* look at [pictures of wildlife](/metazoa.html) that I have taken.

I recommend the pictures.
</div>
