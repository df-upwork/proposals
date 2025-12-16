The 3 most likely causes of your problem:
1) The Microsoft Defender portal may be desynchronized with the Exchange Online backend configuration
The internal `DkimSigningConfig` object often remains in an inconsistent state even though the interface shows the «Enabled» status.
Consequently, outgoing emails trigger `dkim=fail` errors (e.g., «no key for signature») despite having correct DNS records.
Attempts to update the configuration via the portal often fail due to cached data.
A similar case: https://www.reddit.com/r/sysadmin/comments/11itcpm
2) Entering the full domain name in the «Host» field often causes registrars (e.g. GoDaddy) to append the zone name.
This results in a record like `selector1._domainkey.yourdomain.com.yourdomain.com` being published at an incorrect hostname.
The Microsoft Defender validator queries the expected hostname, receives an `NXDOMAIN` response, and blocks activation.
3) Your DNS configuration may have proxying enabled for DKIM records.
In this mode, the DNS server returns `A` records instead of a `CNAME` pointing to `onmicrosoft.com`.
However, Microsoft 365 requires a non-proxied `CNAME` for verification and key rotation.
Thus, Microsoft Defender cannot verify the configuration even though the record appears active.
---
My GitHub profile: https://github.com/dmitrii-fediuk