
![guns-anime](https://github.com/hy011121/Stripe-Api-CC-Validation/assets/75035965/f6ce30ff-1b62-432e-a690-3cbbdd7f458b)

## Use script
 - **Replcae Proxy:** username:password@example:port
 - **Input CC:** 1234567890123456|12|25|123
 - **Input PK:** pk_test_1234567890
 - **Input CS:** cs_test_abcdefghijklmnopqrstuvwxyz

"pk" (Publishable Key) and "cs" (Client Secret), you need to enter these values when prompted by the program

## General Description:
This code is a malicious and illegal implementation that attempts to leverage Stripe's API to commit credit card fraud. This code attempts to process a payment transaction using illegally obtained credit card information. The use of proxies indicates an attempt to conceal the location or identity of the criminal behind this attack.

## Key Steps:
1. Initialize the HTTP session with the requests module.
2. Defines a `pistuff` function that accepts credit card details as well as Stripe API keys and client secrets.
3. Create HTTP headers to be used in requests, including fake user-agents.
4. Send a request to the `https://m.stripe.com/6` to get some information about payment.
5. Parsing the JSON response to get `muid`, `sid`, and `guid`.
6. Process the secret client to get `pi` (PaymentIntent).
7. Create payment data to send to Stripe APIs.
8. Send a payment confirmation request to `https://api.stripe.com/v1/payment_intents/{pi}/confirm`.
9. Check the status of the response to determine if the payment was successful or declined.
10. Returns the corresponding message based on the response status.

## Important Message:
This code is a vivid example of criminal activity and credit card fraud. The use or distribution of this kind of code is unlawful and may result in serious legal consequences. In addition, this kind of action is very unethical and harms the parties affected by it.

## Note:
Using this code for any purpose other than legitimate learning or security testing is strictly prohibited. The use of this code to commit credit card fraud or other illegal activities is illegal and ethically unacceptable.

