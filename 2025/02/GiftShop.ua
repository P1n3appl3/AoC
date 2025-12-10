↘¯1&fras "input"
⊜□⊸≠@,                 # split
P ← ∩⋕°$"_-_"          # parse
▽⊸>₉/◇⊂⍚(⍜-⇡⊙+₁P)      # generate and join ranges
C ← =⊃◿(⌊÷)ₑ₁₀÷₂⌈⊸°ₑ₁₀ # check invalidity
&s /+▽⊸⊸C              # sum invalid
Check    ← ≍⊸↻₁⧈⌞∘     # chunks all equal
Divisors ← ▽⤚(=₀◿)+₁⇡⌊⊸÷₂
# try all groupings that divide evenly
Any ← /↥≡⌟Check Divisors⊸⧻
&s/+×≡◇Any⊸⍚⊥₁₀
