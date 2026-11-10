---
layout: page
title: Follow the Journal
permalink: /newsletter/
description: "Get new MrTicTocTalk Journal articles by RSS or email, free."
---
New guides and release coverage added regularly. Pick whichever way of following is easiest for you.

{% if site.newsletter.followit_url != "" %}
## By email

<a class="button" href="{{ site.newsletter.followit_url }}" rel="noopener" target="_blank">Get new articles by email</a>

Free, no spam, unsubscribe any time.
{% endif %}

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
