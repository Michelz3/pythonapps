```python
import streamlit as st
import random

HASHTAG_POOL = ["#knitting", "#wool", "#yarn", "#knitstagram", "#knittersofinstagram", "#handknit", "#knittingaddict", "#knit", "#knittinglove", "#knittinginspiration"]

def generate_hashtags():
    return random.sample(HASHTAG_POOL, min(5, len(HASHTAG_POOL)))

def main():
    st.title("Wool Hashtag Generator")
    if st.button("Generate Hashtags"):
        hashtags = generate_hashtags()
        st.write(hashtags)

if __name__ == "__main__":
    main()
```
