# savant

Scrape video links from Google Drive

`pip install savant`

```python
>>> import savant
>>> savant.get_link("https://drive.google.com/file/d/0BxbhZzYBRTxnZDREcGtGa0pSc0k/view?usp=sharing")
u'https://r5---sn-i3b7knel.c.docs.google.com/videoplayback?requiressl=yes&id=588dd4855aff61b8&itag=18&source=webdrive&app=texmex&ip=49.149.125.213&ipbits=8&expire=1454717545&sparams=requiressl,id,itag,source,ip,ipbits,expire&signature=168F1A419378ED4676B6955D2EC0491B7A0D6504.15AA6E2B864F61707C8D6B6B5A11B3AD8C968DC4&key=ck2&mm=30&mn=sn-i3b7knel&ms=nxu&mt=1454703054&mv=m&nh=IgpwcjAyLmhrZzA4KgkxMjcuMC4wLjE&pl=19,34'
>>> savant.get_link("https://drive.google.com/file/d/0BxbhZzYBRTxnQVJFSmg0THR3R0E/view?usp=sharing", "video/webm")
u'https://r2---sn-i3b7kn7s.c.docs.google.com/videoplayback?requiressl=yes&id=9285db755ac8a1e5&itag=43&source=webdrive&app=texmex&ip=49.149.125.213&ipbits=8&expire=1454717573&sparams=requiressl,id,itag,source,ip,ipbits,expire&signature=3CFEBF62D0A4BCFB9934B79C0A6B670FC05012C1.AE05B2216C49FE053432EFB785BA5B24C0982E0C&key=ck2&mm=30&mn=sn-i3b7kn7s&ms=nxu&mt=1454703054&mv=m&nh=IgpwcjAyLmhrZzA4KgkxMjcuMC4wLjE&pl=19'
```

## Methods

### get_urls(drive_url)

### get_link(drive_url, video_format='video/mp4')

### get_links(drive_url)

Supported formats: `video/mp4` (default), `video/x-flv`, `video/webm`
