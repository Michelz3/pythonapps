
import streamlit as st
import random

HASHTAG_POOL = [
    "#knitting", "#knittersofinstagram", "#yarn", "#handdyed", "#wool", "#knitstagram", "#handknit",
    "#knitwear", "#knit", "#yarnaddict", "#knittingaddict", "#knittinglove", "#knitlife", "#knitspiration",
    "#knittingproject", "#knitpicks", "#handmade", "#knitting_inspiration", "#yarnlove", "#knittersoftheworld",
    "#woollove", "#knitknitknit", "#knittingfun", "#knittingdaily", "#knittingislove", "#wooladdict",
    "#knittingtime", "#knittingmakesmehappy", "#woolyarn", "#knittingpattern", "#knittingjoy", "#knittingtherapy",
    "#knittingcommunity", "#knittingstudio", "#knittingaddiction", "#knittingprocess", "#wooladdiction",
    "#knittinglifestyle", "#knittingideas", "#knittinggoals", "#knittinghappiness"
]

def generate_hashtags(count=30):
    return random.sample(HASHTAG_POOL, min(count, len(HASHTAG_POOL)))

def format_hashtags(hashtags):
    return ' '.join(hashtags)

def add_one_hashtag(current_list):
    available = HASHTAG_POOL - set(current_list)
    if available:
        selected = random.choice(list(available))
        current_list.append(selected)
        return selected
    else:
        return None

def main():
    st.title("Wool Hashtag Generator")
    if 'hashtags' not in st.session_state:
        st.session_state.hashtags = []

    if st.button("Generate 30 Hashtags"):
        st.session_state.hashtags = generate_hashtags()

    if st.session_state.hashtags:
        st.write("### Click a hashtag to delete and replace it:")
        cols = st.columns(5)
        for i, hashtag in enumerate(st.session_state.hashtags):
            if cols[i % 5].button(hashtag, key=f"del_{i}"):
                available = list(set(HASHTAG_POOL) - set(st.session_state.hashtags))
                if available:
                    new_tag = random.choice(available)
                    st.session_state.hashtags[i] = new_tag
                else:
                    st.warning("No more unique hashtags to add.")
        formatted = format_hashtags(st.session_state.hashtags)
        st.text_area("Your hashtags (copy without quotes or commas):", formatted, height=150)

if __name__ == "__main__":
    main()
