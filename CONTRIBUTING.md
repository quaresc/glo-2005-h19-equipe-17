# How to contribute

In order to contribute to the current project, the potential contributor must comply with the following rules otherwise its proposed changes may be denied and result in lost of time for everyone.

1. Commit messages have to respect the following template:

  ```{bash}
  [{label}] #{no_issue} - {reason for changes}
  ```

  - As we can see above, every commit must be related to an issue.
  - There are several kinds of labels. Each label have a special meaning and is designed for a specific purpose.
      - feature
        : changing code base to implement a new feature
      - fix
        : fixing a bug integrated by another issue that is already merged and thereby a different issue than the one under development
      - doc
        : editing files that are not part of the code base directly and hence by cannot have a direct impact on the quality of the actual application
      - release
        : commits related to the delivery of a new release (mostly used when working with protected branches)
      - test
        : when changes made only affect the tests
      - config
        : to be used for everything related to the configuration of the project
      - refactor
        : changing code base to modify a design decision
  - The commit message must also include a reason for the changes to be necessary which is simply to explain what are the modification brought by this commit and why/how these modifications are useful to the development of the application. Simply citing an acception criteria or desired feature along with a general statement about what have changed is considered like good enough.
1. This repository follow the git-flow workflow described by [Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow).
    - Using this workflow, the repository will mainly use 4 different types of branches
        - master
          : production level - should never commit directly on this branch.
        - release
          : stable + integrated, pre-production level - ensure that everything will be deployed properly.
        - develop
          : stable, but may suffer from integration problem when combining different feature branches together.
        - feature
          : unstable, some commits may generate error on build - will be used by developers to create new features and resolve issues.
        ![](https://wac-cdn.atlassian.com/dam/jcr:a9cea7b7-23c3-41a7-a4e0-affa053d9ea7/04%20(1).svg?cdnVersion=jx)
1. The core team members engage to review every pull requests with 2 workable days (48h).
1. Pull request can be opened at any time during the development of a given feature. If a pull request is opened, but it is not yet still ready to be reviewed, the name of the pull request should be suffixed with (WIP). Once ready for review, the creator of the pull request will simply have to remove this suffix.
1. For a pull request to be accepted, at least 1 core developers must accept the pull request.
1. Once a branch is merged, it should be immediately deleted.
1. Once a branch is created, it should be merged within one week with develop.
1. The feature branches should be named as ``feature/{feature_name}``.
