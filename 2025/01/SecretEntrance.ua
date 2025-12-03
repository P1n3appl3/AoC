&fras "input"
⊜□⊸≠@\n      # split into lines
L ← ±-@Q⊢    # convert "L"/"R" to -1/1
≡(×⊓L⋕°⊂°□)  # multiply ^ and the number on each row
\+⊂50        # prepend 50 and get prefix sums
Z ← /+=0◿100 # count how many %100 == 0
&s⊸Z
▽≠0◿100⊸∘ :   # keep nonzero elements
?⌊÷100 -1     # divide by 100 and floor
&s /+⧈(⍜-⇡) 2 # sum differences along a sliding window
