&fras "input"
⊜□⊸≠@\n        # partition by newlines
LR ← +₁×₋₂=@L⊢ # convert "L"/"R" to -1/1
≡(×⊃LR(⋕↘₁)°□) # multiply ^ and the number on each row
⊂50            # prepend 50
/+ =0 ◿100 \+  # count how many prefix sums %100 == 0
