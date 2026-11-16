# Changelog

## [Unreleased]

### Fixed
- 2026-11-16 15:12 +03: Sign-in now works. The connection asks for the API username and password (Basic authentication) and a small script puts them into each request, as the kwtSMS API expects. The earlier connection settings never reached the API (every action returned ERR003 in Power Automate).
- 2026-11-16 15:12 +03: Test mode is sent as "1", the value the API accepts.

### Changed
- 2026-11-16 15:12 +03: Sender ID is now chosen in the Send SMS action, from the Sender IDs on your account, instead of in the connection. Existing connections must be created again.

### Added
- Integration name and version sent with requests.
- certification/ folder for the Microsoft verified publisher submission: intro.md and icon.png (230x230, white logo on brand color #FFA200).

### Changed
- 2026-11-16 09:07 +03: apiDefinition.swagger.json prepared for certification rules: descriptions end with punctuation, `default` error responses no longer carry an exact schema, body parameters have a summary and description. (JSON has no comments, so the dated note lives here.)
- 2026-11-16 09:07 +03: icon.png replaced with the 230x230 brand-color icon (non-white background, logo under 70 percent).

## [1.0.0] - 2026-03-27

### Added
- Initial release: send SMS (single and bulk), check balance, list sender IDs, check coverage, validate numbers, test mode.
