# Changelog

## [Unreleased]

### Added
- Integration name and version sent with requests.
- certification/ folder for the Microsoft verified publisher submission: intro.md and icon.png (230x230, white logo on brand color #FFA200).

### Changed
- 2026-11-16 09:07 +03: apiDefinition.swagger.json prepared for certification rules: descriptions end with punctuation, `default` error responses no longer carry an exact schema, body parameters have a summary and description. (JSON has no comments, so the dated note lives here.)
- 2026-11-16 09:07 +03: icon.png replaced with the 230x230 brand-color icon (non-white background, logo under 70 percent).

## [1.0.0] - 2026-03-27

### Added
- Initial release: send SMS (single and bulk), check balance, list sender IDs, check coverage, validate numbers, test mode.
