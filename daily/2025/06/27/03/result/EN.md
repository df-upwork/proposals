1) Your proposed method is fundamentally incorrect.
The official Microsoft documentation explicitly states: «Using ABE with Azure Files isn't currently supported»
https://learn.microsoft.com/en-us/azure/storage/files/storage-files-faq#access-based-enumeration
I describe 4 correct methods to solve your task in points 2-5.
2) Azure Files with identity-based controls (specifically, using Windows ACLs).
To implement user and group-level permissions, Azure Files must be integrated with one of the supported identity sources.
Azure supports 3 primary sources:
2.1) On-premises Active Directory Domain Services (AD DS)
2.2) Microsoft Entra Domain Services
2.3) Microsoft Entra Kerberos for hybrid identities.
Once identity-based authentication is enabled, Azure Files fully supports standard Windows access control lists (ACLs) at the directory and file levels.
This is the mechanism that simulates ABE behavior.
3) Azure NetApp Files (ANF): https://learn.microsoft.com/en-us/azure/azure-netapp-files/network-attached-storage-permissions
4) SharePoint Online: rather than of creating a traditional file server in the cloud, use a platform designed for document collaboration.
5) Windows File Server on an Azure virtual machine:
5.1) Deploy a virtual machine with the Windows Server OS in Azure. 
5.2) Attach Managed Disks to it for data storage. 
5.3) Configure the file server role. 
5.4) Create shared folders. 
5.5) Configure permissions.
Because it is a complete Windows Server operating system, it provides native support for ABE, which can be enabled for each shared folder via Server Manager or PowerShell.