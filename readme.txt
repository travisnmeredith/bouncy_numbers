readme.txt

when ran, finds solution to https://projecteuler.net/problem=112
can enter cli arguments. first argument is target proportion, second is limiter proportion. 
program stops and returns when target proportion equals the proportion of bouncy numbers to tested numbers
program stops and fails (giving return for fail time) when limiter proportion is smaller than the currrent proportion
is_bouncy determines if a number is bouncy or not
int_to_iter converts a int into something is_bouncy can use (list of ints foreach didgit)

made to learn branching. functions are not useful (list_matches even exists as a built-in I think).