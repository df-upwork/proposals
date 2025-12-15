The 3 most likely causes of your problem:
1) `⋇1`
The Microsoft Defender portal may be desynchronized with the backend Exchange Online backend configuration.
The internal `DkimSigningConfig` object often remains disabled even if the interface displays the status as «Enabled».
Consequently, the system fails to append signatures despite the presence of correct DNS records.
Attempts to update the configuration via the portal often fail due to cached data.
An example of the problem: https://www.reddit.com/r/sysadmin/comments/11itcpm
2) `⋇2`
Specifying the fully qualified domain name in the «Host» field often causes registrars (e.g. GoDaddy) to append the zone name.
This results in a record like `selector1._domainkey.yourdomain.com.yourdomain.com` located at the wrong address.
The Microsoft Defender validator queries the expected address, receives an `NXDOMAIN` response, and blocks activation.
3) `⋇3`
The DNS provider may have proxying enabled for DKIM records.
In this mode, the DNS server returns `A` records instead of a `CNAME` pointing to `onmicrosoft.com`.
However, Microsoft 365 requires a non-proxied `CNAME` for verification and key rotation.
Thus, Microsoft Defender cannot verify the configuration despite the published record.
