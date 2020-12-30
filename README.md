# [serundeputy.io](https://serundeputy.io)

Geoff St. Pierre (serundeputy) weblog.

## pelican

This is a static markdown blog generated with [pelican](docs.getpelican.com)

## devloping

`pelican -lr`
  * listens and refreshes site on file changes
  * 127.0.0.1:8000

## deploying

* `git push origin main`
* ssh to server
* `git fetch --all`
* `git merge origin/main`
* `pelican content`
  * this generates the static `output` directory
* profit
