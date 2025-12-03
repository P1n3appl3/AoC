&fras "input"
⊜□⊸≠@\n      # split into lines
L ← ±-@Q⊢    # convert "L"/"R" to -1/1
≡(×⊓L⋕°⊂°□)  # multiply ^ and the number on each row
\+⊂50        # prepend 50 and get prefix sums
Z ← /+=0◿100 # count how many %100 == 0
&s⊸Z
&s/+⧈(Z⍜(⌵-)⇡₁⊃⊢⊣) 2
