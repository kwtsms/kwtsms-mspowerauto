# kwtSMS

kwtSMS is a Kuwait-based SMS gateway that delivers messages to 200+ countries. This connector sends SMS from flows and apps: OTP verification, transactional alerts and notifications, in English, Arabic and Unicode.

## Publisher: kwtSMS

## Prerequisites

You need a kwtSMS account with API access enabled. Sign up at https://www.kwtsms.com.

## Supported operations

| Operation | Description |
|-----------|-------------|
| Send SMS | Send a message to one or more recipients (max 200 per request). Optional test mode. |
| Check Balance | Get available and total purchased SMS credits. |
| List Sender IDs | Get all approved sender IDs for your account. |
| Check Coverage | List active country codes available for sending. |
| Validate Numbers | Validate phone numbers. Returns OK, ER (format error) and NR (no route) lists. |

## Obtaining credentials

1. Log in to your kwtSMS account at https://www.kwtsms.com.
2. Open the API information page and copy your API username and API password. They are issued separately: not your mobile number or account login.
3. You need at least one approved Sender ID. The default testing sender is `KWT-SMS`.

## Creating a connection

The connection asks for three values: Username (API username), Password (API password) and Sender ID (case sensitive). They are added to each request by the connector.

## Getting started

1. Add the Check Balance action to a flow and run it to confirm the connection works.
2. Add Send SMS with Test Mode set to 1. The message is queued but not delivered, and credits can be recovered by deleting it from the Queue in your kwtSMS account.
3. Set Test Mode back to 0 for live sending.

## Known issues and limitations

- Phone numbers must be in international format, digits only (for example `965XXXXXXXX`). No `+` prefix, no spaces, no dashes.
- English messages: 160 characters per page. Arabic messages: 70 characters per page. No emojis or HTML.
- Maximum 200 numbers per Send SMS request. For larger lists, split into multiple requests.
- The `unix-timestamp` in responses uses GMT+3 (Asia/Kuwait) server time, not UTC.
- Delivery reports (DLR) are not available for Kuwait numbers, only for international numbers.
- The default `KWT-SMS` sender ID is for testing only and may be delayed or blocked on some carriers. Use a private sender ID for production.

## Support

- Website: https://www.kwtsms.com
- Support: https://www.kwtsms.com/support.html
- Email: support@kwtsms.com
