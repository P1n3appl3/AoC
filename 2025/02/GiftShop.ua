↘¯1&fras "input"
# "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
⊜□⊸≠@,                 # split
P ← ∩⋕°$"_-_"          # parse
/◇⊂⍚(⍜-⇡⊙+₁P)          # generate and join ranges
C ← =⊃◿(⌊÷)ₑ₁₀÷₂⌈⊸°ₑ₁₀ # check invalidity
&s /+▽⊸⊸C              # sum invalid
# check invalidity for a given group size
D ← /↧⧈(=⊃⊢⊣)2⧈□¤¤
# tries all groupings in [1,÷₂⧻]
C ← /↥≡⌟D▽⤚(=₀◿)+₁⇡⌊⊸÷₂⊸⧻
&s /+⋕▽⊸≡◇C⍚°⋕
