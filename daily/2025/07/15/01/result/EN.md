1) The «Reauthorize» action and the «Integrations» screen are not related to your problem: you are wasting time and effort.
2) The context of the problem is the Digital Markets Act (DMA) of the European Union.
When implementing the DMA, Google makes you, the website owner, responsible for collecting consent using its  «Consent Mode» protocol.
3) In May 2025, Google updated its «Consent Mode» protocol by changing the cookie format («GS2 Cookie»).
This is what broke your module (WeltPixel Google Analytics 4 PRO).
4) WeltPixel is aware of the problem and describes it in the module's changelog on its website:
«Important adjustment (PRO): Implemented the use of the updated GS2 Cookie, a potentially integration-breakning change Google introduced in May 2025 without prior notice. 
If your tracking implementation is experiencing attribution or issues surrounding data tracking, please update to this version ASAP.»
5) The correct solution:
5.1) Verify that the WeltPixel module is indeed properly updated.
5.2) Verify that the new version of the module does not conflict with other installed modules and the used Magento theme.
5.3) Verify that another module — for consent management — is correctly installed and working in Magento.
In particular, WeltPixel itself offers such a module: https://www.weltpixel.com/google-consent-mode-v2.html
---
I have completed 536 Magento projects here on Upwork.
My GitHub profiles: https://github.com/dmitrii-fediuk and https://github.com/mage2pro
My websites: https://mage2.pro?order=views, https://df.tips?order=views, https://dmitry.ai?order=views