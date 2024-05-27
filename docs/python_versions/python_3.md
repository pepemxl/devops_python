# Python 2 to Python 3 

Migrating from python 2 to python 3 is not very easy, but it can be exacerbated by needing to port a large codebase modified frequently by many different developers. Our codebase was nearly 4 million lines of code modified dozens of times a day by hundreds of total developers. It is also business critical, containing a large portion of our most important code and data. We used several tools, techniques, and patterns to achieve the migration without disrupting day-to-day development and keeping regressions a minimum. In this talk, we’ll detail our migration steps, our usage of pre-commit hooks to reduce regressions to fixes, our usage of a reverse proxy to allow granular, low risk rollout for a webapp, and our migration of pickle to rollforward safe json for caching.

- [Yelp](https://www.youtube.com/watch?v=d6QAPcOX5OM)


- 20-30 changes per day
- 800 developers
- ~700 python package dependencies
- 100K tests (35hrs to run serially)



## Phases and timeline

1. Parsabililty
    - Tried to parse files
    - Filed tickets for handful of broken files
2. Importability
    - Imported all files and grouped by "root cause" import failure
    - Filed tickets periodically by root cause
3. Functiona parity
    - Ran tests
    - Our tooling groups by traceback
    - Filed tickets periodically by root cause
4. Rollout
    - Parallel python 2 and 3
    - Reverse proxy configured by URL path prefix to send to different instances
        - Allows for granular rollback when errors are detected
            - Some errroes not caught by tests
        - Ownership spreadsheet for 800 endpoint prefixes across 6 sites
        - Batches migrated individually

1.25 years!!!


### Outcomes

- Very long tail
    - Initial progress on tests was faster than expected, but slowed down
- Type annotations would have been useful
- Rollout took lonmger then expected
    - Blacked by teams doing verification
        - Could have notified earlier

- 15-20% speedup
- 26% less memory

## The future

- Automating minor python versions bumps, leveraging existing tooling to bump packages
    - Uses pip-tools to target upgrades and run tests to ensure functional parity



## Pinterest Case

- [Pycon 2019](https://www.youtube.com/watch?v=e1vqfBEAkNA)

- 250 MAUs
- 2.6 million LOC(Lines of Code)
- 10 years 1000 authors
- Dynamic ~3500 changes monthly
- Multi-Stakeholder
- Tighly Coupled


Shared Code Base with different goals and objectives

Coupliong situation code base is suboptimal for this kind of problem


Metrics-informed (Not metrics driven)


- Start at bottom of dependency graph
- caniusepython3 (version classifier troves)
- unmaintained dependencies


