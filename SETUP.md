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
Create a free follow.it account using the feed `https://williec677.github.io/feed.xml`. Copy your subscribe page URL into:
`followit_url: "https://follow.it/..."`
A subscribe button then appears on the Newsletter page and under every post.

## Publishing schedule
Posts in `_posts/` dated in the future stay hidden. A GitHub Action rebuilds the site every day at 9:05 AM ET (14:05 UTC), so each post goes live on its date. To add a post, copy an existing one, change the date and text, and commit. Note: GitHub pauses scheduled workflows after 60 days with no commits, so make any small commit (or tap "Enable workflow" in the Actions tab) at least every 60 days.

## Never put secrets here
This repo is public. IDs above are public identifiers that appear in every link anyway. Never commit passwords, API keys, tax info, or bank details.
