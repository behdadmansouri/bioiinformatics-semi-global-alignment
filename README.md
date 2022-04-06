Using the Needleman-Wunsch Algorithm to calculate the semi-global alignment of two protein sequences 
using only the forward pass 


- pandas or numpy were not used. Therefore, addressing the matrices is sort of reversed
- direction matrix is not used, so it should have better performance
- pytests are written

TODO
- supports if a branch diverges, but not if two branches merge
- customizable gap penalty
- support for multi-path (missing in [here guy's](https://github.com/murk3000/Semi-Global-Allignment/blob/master/semi_glob_allign.py))
- support for global and local alignment:
  - for p in seq1:
  -       sc = sc # add gp for global assignment
  - sc = 0 
- lines like     # --- this for explaining each function

## FAQs
### How to use?
> Simply go to the user input section, enter sequences and gap penalty, and run the python code!
What the algorithm does?
> It creates a 2D matrix that shows the maximum score possible for the pairwise alignment of two proteins.
Ideally, in a semi-global alignment you would compute forward and backward passes to get the best possible allignment.
In this you only go through a forward pass of the proteins.
With some basic understanding of the code, one could easily modify this to do so.

### Can local or global alignment be done with this?
> Yes! By following the comments you can insert pieces of code that would do so!