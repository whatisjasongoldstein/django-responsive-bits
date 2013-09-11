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

    <img data-img-sizes={% image_sizes 1=small_img.url 900=medium_img.url 1200=large_img.url 1500=massive_img.url %} src="{{ small_img }}">

And that's it. You get the small version by default, the medium version if the image is at least 900px wide, etc.

Always go smallest to largest.

Setting `src` is optional, but if you don't your image will be blank without javascript, and people living in 1998 will laugh at you. You also risk a flash of empty image.

You can also support retina devices by adding `data-retina="true"` (or any value), and the image width used to decide which thumbnail to use will be multiplied by the device's pixel density. Use this wisely; just because I have a nice screen
doesn't mean the coffee shop wifi or 3G connection isn't going to wimper when you start throwing giant images at me.

My example uses [Easy Thumbnails](https://github.com/SmileyChris/easy-thumbnails) (`pip install easy-thumbnails`), but virtually any library should be fine. The important part is that you can pass the thumbnail urls in as variables.


## Background Images

Some people prefer using background images. The advantage is the request isn't blocking, there's no duplicate requests, and resizing "just works". There's a tag for that too.

    {% load thumanils responsive_tags %}

    {% thumbnail object.image 600x360 crop=",1" as small_img %}
    {% thumbnail object.image 1000x600 crop=",1" as large_img %}
    {% thumbnail object.image 1200x720 crop=",1" as huge_img %}

    <figure id="#foobar"></figure>
    {% image_sizes_css selector="#foobar" default=small_img.url 1280=large_img.url 1680=huge_img.url %}

This will output...

    <style type="text/css">
        #foobar {background-image: url('default-image.jpg');}
        @media (min-width: 1280px){
            #foobar {background-image: url('large-image.jpg');}
        }
        @media (min-width: 1680px){
            #foobar {background-image: url('huge-image.jpg');}
        }
    </style>

I'm on the fence about whether the templatetag abstraction is actually more elegant than just writing the snippet. I'm also considering a javascript-driven solution that measures the image itself. Feedback welcome.


### On the Sad, Shameful Lack of Tests

I know, I know. Coming soon.


### TODO

* Tests.
* More features so this isn't a sad little repo with one thing in it.


