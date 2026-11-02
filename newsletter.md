---
layout: page
title: Follow the Journal
permalink: /newsletter/
description: "Get new MrTicTocTalk Journal articles by RSS or email, free."
---
New articles go up every **Tuesday and Friday at 9 AM Eastern**. Pick whichever way of following is easiest for you.

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

Daily watch talk lives at [@mrtictoctalk](https://www.instagram.com/mrtictoctalk/).
