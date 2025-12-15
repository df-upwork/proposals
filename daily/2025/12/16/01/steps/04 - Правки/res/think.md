## 1\.

1.  `𐒌(1)`

<!-- end list -->

1)  `⋇1`
    The Microsoft Defender portal may be desynchronized with the backend Exchange Online configuration.
    The internal `DkimSigningConfig` object often remains in an inconsistent state even if the interface displays the status as «Enabled».
    Consequently, outgoing emails trigger `dkim=fail` errors (e.g. «no key for signature») despite the presence of correct DNS records.
    Attempts to update the configuration via the portal often fail due to cached data.
    An example of the problem: [https://www.reddit.com/r/sysadmin/comments/11itcpm](https://www.google.com/search?q=https://www.reddit.com/r/sysadmin/comments/11itcpm)