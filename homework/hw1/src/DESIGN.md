# Design
## count function
- create accumulator variable
- loop through each element in the for loop
- check if current element in for loop is equal to `num` at each iteration
- if it is, add one to the accumulator variable

## extend function
- create accumulator variable (empty list)
- loop through each of the two lists and append each element in each list to the accumulator

## remove function
- create accumulator variable (empty list)
- loop through each value in the input list and append it to the accumulator if it is NOT equal to the `num` value

## index function
- loop through each value in the input list, keeping track of the current index as well
- if the current element in the list is equal to `num`, return the current index.
- outside the loop return None
