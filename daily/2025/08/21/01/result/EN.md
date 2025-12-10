The reason for your problem is obvious to me: the use of the wrong Stripe API method: `PaymentIntent` instead of the correct `SetupIntent`.
1) The `authentication_required` decline code is a hard decline, which directly indicates that the issuing bank requires customer authentication (e.g., via 3D Secure) to process the transaction.
Such a decline during an automatic charge attempt at the end of the trial period unequivocally indicates the absence of a previously obtained and validated mandate to charge funds off-session.
2) Stripe's Smart Retries system, which is designed to handle soft declines, by design ignores hard declines, including `authentication_required`, which explains the systemic and irresolvable nature of the problem without intervention in the code.
3) The high rate of such declines (~25%) is not an indicator of credit risk or the unwillingness of customers to pay, but a direct measurement of an architectural failure, in which the integration is technically incapable of proving to the bank the existence of the customer's consent for the recurring payment.
4) The high rate of declines on the first attempt to charge funds after the end of the trial period is a direct and expected consequence of the lack of proper Strong Customer Authentication (SCA) during the initial session.
Issuing banks, in accordance with regulatory requirements such as PSD2 in Europe, decline off-session transactions with the authentication_required code if the merchant has not obtained explicit customer consent for recurring payments through an appropriate authentication mechanism.
5) The fact that the problem occurs exclusively when using the custom API solution and is absent in the native HighLevel checkout convincingly proves that the error lies precisely in the logic of the custom code.
Native integrations and out-of-the-box solutions, such as Stripe Checkout, implement the correct logic with `SetupIntent` for subscriptions by default, whereas the custom development made an error by implementing this flow incorrectly.
6) The mentioned error «Invalid value for confirm card payment – client_secret is null» indirectly confirms the hypothesis, indicating a convoluted and incorrect logic for handling Intents on the client-side.
Such errors often arise when attempting to re-confirm an already completed or expired intent, which is entirely possible in a scenario where a PaymentIntent is erroneously repurposed to create a subscription.
---
My GitHub profile: https://github.com/dmitrii-fediuk
