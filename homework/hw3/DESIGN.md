# UnorderedList

## `append`
- Creates a new `Node` with the given `item`.
- If the list is empty, sets this node as both `head` and `tail`.
- If not, sets it as the `next` of the current `tail` and updates `previous` of the new node.
- Updates `tail` to be this new node.
- Increments `size`.

## `pop`
- Returns `None` if the list is empty.
- Saves the data of the current `tail`.
- Updates `tail` to its `previous` node, if available.
- If there's only one item, sets both `head` and `tail` to `None`.
- Decrements `size`.
- Returns the saved data of the original `tail`.

## `remove`
- Iterates through the list lookng for a node with a matching `item`.
- If found, adjusts `next` and `previous` references of adjacent nodes
- If the item is at `head` or `tail`, updates them accordingly.
- Decrements `size`.
- Returns the data of the removed node, or `None` if it was not found.
