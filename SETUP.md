# Setup guide (phone friendly)

Everything here can be done from the GitHub mobile site. Each step: open the file link, tap the pencil (Edit), change one line, tap **Commit changes**. The site rebuilds itself in about 2 minutes.

Edit link for the config file: https://github.com/williec677/williec677.github.io/edit/main/_config.yml

## 1. Amazon Associates (after approval)
Find your tracking ID in Associates Central (looks like `yourname-20`). In `_config.yml` set:
`amazon_tag: "yourname-20"`
Every Amazon link on the site gets `tag=` added automatically.

## 2. eBay Partner Network (after approval)
EPN dashboard > Campaigns > copy the 10 digit Campaign ID. Set:
`ebay_campid: "5338xxxxxx"`

## 3. Chrono24 via Awin (after Chrono24 approves you)
Awin dashboard shows your publisher ID (top right) and Chrono24's advertiser ID. Set:
`awin_affid: "1234567"` and `chrono24_awinmid: "12345"`
Both must be filled for Chrono24 links to be tagged. Until then they are plain links.

## 4. Google AdSense (after approval)
Set `publisher_id: "ca-pub-XXXXXXXXXXXXXXXX"`. Ads stay off while it is blank.
Then create a file named `ads.txt` in the repo root containing one line:
`google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0`
(Use your number without the `ca-` prefix.) If you get EU visitors, turn on Google's free consent message (Privacy & messaging) in AdSense.

## 5. Newsletter (follow.it, free)
Create a free follow.it account using the feed `https://mrtictoctalk.com/feed.xml`. Copy your subscribe page URL into:
`followit_url: "https://follow.it/..."`
A subscribe button then appears on the Newsletter page and under every post.

## Publishing schedule
Posts in `_posts/` dated in the future stay hidden. A GitHub Action rebuilds the site every day at 9:05 AM ET (14:05 UTC), so each post goes live on its date. To add a post, copy an existing one, change the date and text, and commit. Note: GitHub pauses scheduled workflows after 60 days with no commits, so make any small commit (or tap "Enable workflow" in the Actions tab) at least every 60 days.

## Post front matter for search
Every post can carry these fields on top of `title`, `description` and `date`:

* `seo_title:` the text used in the browser tab and Google title link. Keep it under 60 characters. The site adds " | MrTicTocTalk" only when the whole title still fits under 60. If a post has no `seo_title`, the full `title` is used, so add one whenever the title is long.
* `cluster:` the topic group, used to pick the "Keep reading" links under the post. Current values: `gmt`, `dive`, `vintage`, `affordable`, `alternatives`, `gear`. Posts in the same cluster are shown first, then the newest other posts.
* `noindex: true` keeps a page out of search results (used on the 404 page). Do not set it on normal posts.

## Post images
Put post images in `assets/img/posts/`, named after the post slug, for example `assets/img/posts/rolex-gmt-master-ii-16710-buyers-guide.jpg`.

Rules:
* Each image must be under 200KB. Resize to about 1200 pixels wide and compress before you upload.
* Alt text is required. Describe the watch in plain words, for example "Rolex GMT Master II 16710 with the Coke bezel on the wrist".
* Use only your own photos, or images you have permission to use.

To use an image as the social card (og:image) for a post, add it to the front matter with its alt text:

```
image:
  path: /assets/img/posts/rolex-gmt-master-ii-16710-buyers-guide.jpg
  alt: "Rolex GMT Master II 16710 with the Coke bezel on the wrist"
```

Posts without an `image:` use the site default card, the MrTicTocTalk logo (`/assets/img/brand/logo-full.png`). To show an image inside the post, use Markdown with alt text: `![Rolex GMT Master II 16710 on the wrist](/assets/img/posts/rolex-gmt-master-ii-16710-buyers-guide.jpg)`.

## IndexNow
After each successful deploy, the workflow tells IndexNow (used by Bing and others, not Google) about new or changed posts. The key is the file `5908965c96dc3e71d77eefc66b4d9099.txt` in the repo root; do not delete or rename it. If the ping fails, the deploy still counts as a success. To resubmit every URL, run the workflow by hand from the Actions tab (Run workflow).

## Before turning on Chrono24 or AdSense
Chrono24 links stay plain, unlabeled links until both Awin IDs are set. When Chrono24 or AdSense goes live, add it back to the Affiliate Disclosure page and the Privacy page (AdSense needs its cookie and opt out section) in the same commit.

## Never put secrets here
This repo is public. IDs above are public identifiers that appear in every link anyway. Never commit passwords, API keys, tax info, or bank details.
