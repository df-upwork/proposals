3 most likely causes of your problem:
1) `⋇1`
It is possible that when creating CNAME records in the DNS control panel, you specified the Fully Qualified Domain Name (FQDN) in the host name field.
Many registrars (e.g. GoDaddy or Namecheap) automatically append the zone name to the value if it does not end with a dot.
As a result, a record of the form `selector1._domainkey.yourdomain.com.yourdomain.com` is created, which is technically correct but is located at the wrong address.
The Microsoft Defender validator queries the expected address `selector1._domainkey.yourdomain.com` and receives an `NXDOMAIN` response, which blocks activation.
2) `⋇2`
It is possible that you use a DNS provider with CDN functionality (most often Cloudflare) and have left the proxying mode (orange cloud) enabled for DKIM records.
In this mode, the DNS server returns A records with the proxy server IP addresses instead of a CNAME pointing to `onmicrosoft.com`.
Microsoft 365 requires a non-proxied CNAME record for ownership verification and the operation of the automatic key rotation mechanism.
Breaking the CNAME chain results in Defender being unable to verify the configuration, even if the record is published.
3) `⋇3`
This hypothesis is based on the architectural features of the distributed cloud system Exchange Online, where a temporary or permanent desynchronization between the graphical user interface (GUI) and the actual state of objects in the backend is possible.
An example of the problem: https://www.reddit.com/r/sysadmin/comments/11itcpm
In the Microsoft 365 ecosystem, DKIM configuration management is performed via `DkimSigningConfig` objects stored in the Azure Active Directory directory service and replicated to Exchange Online Protection (EOP) transport servers.
Documented cases are known where the «Enable DKIM» toggle in the Microsoft Defender portal (security.microsoft.com) is displayed as greyed out or is in the «Enabled» position, but in fact, email signing is not performed.
This state, called «stuck state», occurs when the configuration change command from the GUI was not correctly processed by the domain controller or did not undergo full replication across all geographic zones.
Even with absolutely correct and validated DNS records, the transport service does not start adding the DKIM-Signature header, since the internal Enabled flag for the given domain remains at the value $false.
Moreover, an attempt to toggle the switch again in the GUI often does not lead to rectifying the situation, as the interface uses cached data about the object state.