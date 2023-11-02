# Design Document
## Function: hide
- Initialize an empty string `new_sentence` to store the result.
- Initialize an empty dictionary `seen` to track the characters that have been encountered.
- Iterate over each character in the input sentence.
- If a character is found in `seen`, append * to `new_sentence`.
- If a character is not in `seen`, append the character to `new_sentence` and mark it as seen in `seen`.
- Return `new_sentence`.

## Function: `reduce_adjacent`
- Initialize an empty list `new_lst` to store the result.
- Iterate over `num_lst` using enumerate to have access to both the index and the value.
- Add the first integer to `new_lst`.
- For subsequent integers, compare with the previous integer.
- If the current integer is different from the previous one, append it to `new_lst`.
- Return `new_lst`.

## Function: reverse
- Initialize an empty string `new_word` to store the result.
- Find the length of the input word and start from the last index.
- Use a while loop to iterate over word in reverse order.
- Append each character to `new_word` during iteration.
- Decrement the index in each iteration until the first character is reached.
- Return `new_word`.
