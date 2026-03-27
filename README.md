# kwtSMS

Send single or bulk SMS messages worldwide through the kwtSMS gateway. Check your credit balance, list approved sender IDs, validate phone numbers, and verify country coverage.

## Publisher: kwtSMS

## Prerequisites

You need a kwtSMS account with API access enabled. Sign up at [kwtsms.com](https://www.kwtsms.com).

## Obtaining Credentials

1. Log in to your kwtSMS account at [kwtsms.com](https://www.kwtsms.com)
2. Your API credentials are the same username and password you use to log in
3. You need at least one approved Sender ID. The default testing sender is `KWT-SMS`

**Note:** Your API username is NOT your mobile number. Use the account username and password.

## Supported Operations

### Send SMS
Send an SMS message to one or more recipients. Supports bulk sends with comma-separated numbers (max 200 per request). Includes an optional test mode for development.

### Check Balance
Check your available SMS credits and total purchased credits.

### List Sender IDs
List all approved sender IDs for your account.

### Check Coverage
List active country prefixes available for sending on your account.

### Validate Numbers
Validate phone numbers before sending. Returns numbers grouped as valid (OK), format error (ER), or no route (NR).

## Important Notes

- Phone numbers must be in international format, digits only (for example `96598765432`). No `+` prefix, no spaces, no dashes.
- Sender ID is case sensitive. `KWT-SMS` is for testing only, register a private sender ID for production use.
- English messages: 160 characters per page. Arabic messages: 70 characters per page.
- Messages must not contain emojis or HTML tags.
- Maximum 200 numbers per Send SMS request. For larger lists, split into multiple requests.
- The `unix-timestamp` in responses uses GMT+3 (Asia/Kuwait) server time, not UTC.
- Set test mode to 1 during development. Messages are queued but not delivered, and credits can be recovered by deleting from the sending queue in your kwtSMS dashboard.

## Known Issues and Limitations

- Delivery reports (DLR) are not available for Kuwait numbers, only for international numbers.
- The default `KWT-SMS` sender ID may experience delays and is blocked on some carriers. Use a private sender ID for production.
- There is a 15-second minimum between messages to the same phone number (ERR028).
