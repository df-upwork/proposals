There are 2 good solutions for your requirements:
1) Entra Certificate-Based Authentication (CBA) using a third-party managed PKI (PKIaaS)
1.1) Essence
This method uses standard smart card protocols (PIV) and fully supports automatic sign-out upon token removal through Windows' native functionality.
To reduce the complexity of managing the PKI infrastructure, this solution utilizes cloud-based PKI services (PKIaaS) provided by specialized vendors (e.g., Entrust, Sectigo, Keyfactor).
The vendor manages the CA infrastructure and CRL publication.
Such solutions often include a Certificate Management System (CMS) designed to manage physical tokens (smart cards/YubiKeys in PIV mode).
The CMS simplifies user enrollment, certificate provisioning to tokens, and self-service
1.2) Advantages
1.2.1) The solution provides full native support for the requirement of automatic sign-out upon token removal through the Windows policy «Interactive logon: Smart card removal behavior».
1.2.2) The complexity of deploying and maintaining the PKI is offloaded to the service provider.
1.2.3) The presence of an integrated CMS significantly simplifies the lifecycle management of smart cards and YubiKeys (enrollment, PIN management, replacement).
1.2.4) The solution is cloud-based and does not require on-premises infrastructure.
1.2.5) Providers guarantee the high availability and security of the PKI and CRL.
1.3) Disadvantages
1.3.1) The solution entails ongoing operational costs for the subscription.
1.3.2) This solution requires entrusting the management of a critical security infrastructure to a third-party provider.
1.3.3) Integration with Entra ID and potentially Intune requires implementation time and effort.
2) FIDO2 authentication
2.1) Essence
This method uses the FIDO2 standard for passwordless authentication.
Users use physical tokens (e.g., a YubiKey in FIDO2 mode) to sign in to Entra ID-joined Windows devices.
FIDO2 provides phishing-resistant multifactor authentication.
2.2) Advantages
2.2.1) It completely eliminates the need for PKI, which significantly simplifies deployment and support.
2.2.2) It provides a high level of security (Phishing-resistant MFA).
2.2.3) The user experience is similar to CBA: the user inserts the token and enters a PIN code.
2.2.4) It eliminates the complexities related to certificate management (expiration dates, revocation, CRL).
2.2.5) The solution is completely cloud-based, easily scalable, and natively supported by Entra ID and Windows.
2.3) Disadvantages
Windows does not natively support automatic sign-out upon removal of a FIDO2 key.
The built-in Windows security policy «Interactive logon: Smart card removal behavior» works only with tokens using the smart card protocol (PIV).
This protocol is used in Certificate-Based Authentication (CBA).
Implementing the required behavior for FIDO2 requires third-party software or scripts, which complicates deployment and support.
---
My GitHub profile: https://github.com/dmitrii-fediuk