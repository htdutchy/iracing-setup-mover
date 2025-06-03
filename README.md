# iRacing setup mover
Moves your iracing setup files from your downloads folder to the mapped car based a simple yaml configuration.

Requires `pyyaml`, `pip install pyyaml`.  
When new files for a car are detected, all previous files are moved to a subdirectory called `old`.  
Otherwise, does what it says on the packaging.

## Configuration
Included configuration file is an example based on setups downloaded from VRS.  

Example base config:
```yaml
default_glob: "*.sto"

mappings:
  "MX5": "mx5 mx52016"
```

`default_glob`: the basic search pattern to use for setup files.  
`mappings`: key, value pairing of the pattern to look for in the file followed by the value as the target folder in your setups directory.

See https://support.iracing.com/support/solutions/articles/31000172625-filepath-for-active-iracing-cars for a list of all paths.
