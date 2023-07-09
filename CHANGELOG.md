# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [10.0.3] - 2023-06-08
### Fixed
* Save cron config for fully qualified table name to allow different targets on the same source to have different cron configs.
### Changed
* Increased CLI_WAIT_IN_SECONDS default to `30` seconds (was `5`). See [EGDL-4499](https://jira.expedia.biz/browse/EGDL-4499).

## [10.0.2] - 2023-05-31
### Fixed
* Add check for cron trigger in case the target table does not have cron enabled.

## [10.0.1] - 2023-05-31
### Added
* Cron based job trigger. [EGDL-4151](https://jira.expedia.biz/browse/EGDL-4151).
### Removed
* Skip based job trigger.

## [10.0.0] - FAILED

## [9.4.1] - 2023-05-19
### Changed
* Making touched partitions validation flag based, so that we can control it per environment.
### Added
* [EGDL-4460](https://jira.expedia.biz/browse/EGDL-4460) - Cloverleaf: provide table properties as part of DDL to be compliant with tags enforcement

## [9.4.0] - 2023-05-16
### Added
* [EGDL-3902](https://jira.expedia.biz/browse/EGDL-3902) - Store in-memory queue in K8S config map periodically.
### Changed
* `withTtlSecondsAfterFinished` for Cloverleaf K8S jobs is set to 6 hours (was 1 hour).
* Updated EMR5 base image version to `2.0.2` (was `2.0.1`) to fix log4j configuration.
