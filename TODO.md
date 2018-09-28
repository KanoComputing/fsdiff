# TODO

This is a TODO list for features that are currently WIP.

- Finish implementation for image mounting using sys/mount.h and offsets
- Add the option to run the recursive content file comparison (current) or a sha256 
- Save the report summary in a log file
- Add tests
- Add an extra verbosity option (-vvv) to display modified files 

# Limitations

Currently the verbose option doesn't discover empty directories that differ 
between two filesystem locations. Additionaly, it doesn't perform byte to byte
comparison between each file, so it doesn't display modified files between two
locations. This is to be added in a coming version.
