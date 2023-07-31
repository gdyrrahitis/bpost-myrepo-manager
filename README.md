MyRepo Manager
--------------
[![MyRepo Manager CI](https://github.com/gdyrrahitis/bpost-myrepo-manager/actions/workflows/myrepo-manager-ci.yml/badge.svg)](https://github.com/gdyrrahitis/bpost-myrepo-manager/actions/workflows/myrepo-manager-ci.yml)

### In brief
Python app that clones a git repo, appends to a text file, stages it, commits and pushes.

The repo that this app manages can be found [here](https://github.com/gdyrrahitis/bpost-myrepo). It is added as submodule in this package, see `lib` directory.

App is containerized, for development use the git-server container.

### Prerequisites
- install python3
- install docker for desktop

Once all above installed, clone repo and run
```
$ pip install .
```

Before running the app or the integration test run the setup script, which creates a dev directory, with the submodule repo and SSH keys copied to `git-server` volume directory. This will be used as volume for the git server container.

```
$ ./bin/setup_myrepo.sh
```

### Local run

Run app locally

```
$ ./bin/run_local.sh 
```

### Integration test local run

```
$ ./bin/run_integ.sh 
```

### Other commands
Run linter
```
$ ./bin/lint.sh 
```

Format code
```
$ ./bin/format.sh 
```
