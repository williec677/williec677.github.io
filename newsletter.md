---
layout: page
title: Follow the Journal
permalink: /newsletter/
description: "Get The MrTicTocTalk Weekly Watch Report and new Journal articles, free."
---
New guides and release coverage added regularly. Pick whichever way of following is easiest for you.

## The MrTicTocTalk Weekly Watch Report

{% include newsletter-form.html %}

## By RSS

Copy this feed address into any reader app (Feedly, Inoreader, NetNewsWire, Reeder):

`{{ '/feed.xml' | absolute_url }}`

<a class="button" href="https://feedly.com/i/subscription/feed/{{ '/feed.xml' | absolute_url | url_encode }}" rel="noopener" target="_blank">Follow on Feedly</a>

## On Instagram

More watch talk lives at [@mrtictoctalk](https://www.instagram.com/mrtictoctalk/).

{% if site.x_url != "" %}
## On X

New posts are also shared on [X @mrtictoctalk]({{ site.x_url }}).
{% endif %}
