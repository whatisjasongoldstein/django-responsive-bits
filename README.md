Django Responsive Bits
======================

The earlier beginnings of a responsive utility belt. I'll add things as I need 
them/have time to break them out of my other sites.

**Fair warning:** this is literally a first pass. I may have written it while on a plane. I don't know if it works in IE.

## Images

Most [responsive image implementations](https://github.com/scottjehl/picturefill) look at the size of the document to decide what to do.
(See CSS background images with media queries.) 
That's all well and good, but it seems like it would be better to examine the image itself,
so if your image is 300 pixels wide, you just know that you probably want the 300px thumbnail,
or something close to it.

### Setup &amp; Usages:

    Put `responsive_bits` in INSTALLED_APPS.

    A newish version of jQuery is required.

    Add `<script src="{{ STATIC_URL }}js/deferred-images.js">` in your base template.


    {% load thumanils responsive_tags %}
    
    {% thumbnail object.image 600x360 crop=",1" as small_img %}
    {% thumbnail object.image 1000x600 crop=",1" as medium_img %}
    {% thumbnail object.image 1200x720 crop=",1" as large_img %}
    {% thumbnail object.image 1600x960 crop=",1" as massive_img %}

    <img data-img-sizes={% image_sizes 1=small_img 900=medium_img 1200=large_img 1500=massive_img %} src="{{ small_img }}">

And that's it. You get the small version by default, the medium version if the image is at least 900px wide, etc.

Always go smallest to largest.

Setting `src` is optional, but if you don't your image will be blank without javascript, and people living in 1998 will laugh at you.

Requires easy-thumbnails.


### On the Sad, Shameful Lack of Tests

I know, I know. Coming soon.


### TODO

* Optional retina support. I'm not convinced it's wise to give retina devices HD images all the time, but it should be a flag.
* Tests.
* More features so this isn't a sad little repo with one thing in it.


