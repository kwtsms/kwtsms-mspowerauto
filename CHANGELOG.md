# Changelog

## [Unreleased]

### Added
- Requests to kwtSMS carry the integration name and version (no personal data) so kwtSMS can see which integrations are in use.

### Changed
- Docs and examples use the placeholder 965XXXXXXXX instead of a sample mobile number.

### Docs
- ERR028: duplicate SMS protection is opt-in per account with a configurable window (10 seconds by default), not a fixed 15 seconds

## [1.0.0] - 2026-03-27

### Added
- Initial release
- Send SMS action (single and bulk)
- Check Balance action
- List Sender IDs action
- Check Coverage action
- Validate Numbers action
- Connection parameters: username, password, sender ID
- Test mode support on Send SMS
