1) In a well-designed e-commerce store, a «maps API», in principle, should not have a critical impact on order processing.
The existence of such a dependency indicates poor store architecture.
2) It can be assumed that in your e-commerce store, the «maps API» performs some of the following roles:
2.1) It determines the distance or delivery zone based on the customer's address to calculate the exact cost.
2.2) It helps users enter their address correctly by offering suggestions or by validating it.
2.3) It determines the sales tax rate based on the customer's location.
All these roles are auxiliary, and in a well-designed e-commerce store, a failure of the «maps API» should not prevent customers from making purchases.
In the modern world, customer geolocation is inherently inaccurate. 
For example, many customers use a VPN or make purchases while not at home.
3) The most likely reasons for the «maps API» failure:
3.1) Most «maps APIs» (including the most popular one — Google Maps) set a monthly or daily limit for free requests.
If the store does not use a paid plan for its «maps API», then it can be assumed that the store has exhausted the limit of free requests to the «maps API».
This is the most likely reason.
3.2) Most «maps APIs» (including Google Maps) require a linked bank card for payments beyond the free limits.
If the free limits have been exceeded (reason 3.1) and there are problems with payment (e.g., the card has expired or there are insufficient funds), the API stops working.
This is the second most likely reason.
3.3) The «maps API» key, specified in the WooCommerce settings, may be incorrect, has been deleted, or has been deactivated.
3.4) There are other reasons as well, but they are less likely.