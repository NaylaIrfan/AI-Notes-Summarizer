
import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="AI Notes Summarizer",
    page_icon="📚",
    layout="centered"
)


@st.cache_resource
def load_model():
    return pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6"
    )


st.title("📚 AI Notes Summarizer")
st.write(
    "Convert your long study notes into short, "
    "easy-to-understand summaries using AI."
)

st.info(
    "This project uses a pretrained deep learning "
    "language model. The model downloads automatically "
    "the first time you generate a summary."
)

notes = st.text_area(
    "Paste your notes here:",
    height=250,
    placeholder="Enter your study notes here..."
)

summary_length = st.select_slider(
    "Choose summary length",
    options=["Short", "Medium", "Long"],
    value="Medium"
)

if st.button("Generate Summary", type="primary"):
    if len(notes.strip()) < 100:
        st.warning(
            "Please enter at least 100 characters "
            "so the AI can summarize your notes."
        )

    elif len(notes) > 10000:
        st.warning(
            "Please keep your notes under 10,000 characters."
        )

    else:
        try:
            with st.spinner(
                "AI is reading your notes and generating a summary..."
            ):
                summarizer = load_model()

                word_count = len(notes.split())

                length_settings = {
                    "Short": (20, 60),
                    "Medium": (40, 100),
                    "Long": (60, 140)
                }

                min_length, max_length = length_settings[
                    summary_length
                ]

                # Adjust the summary length for shorter notes.
                max_length = min(
                    max_length,
                    max(10, int(word_count * 0.8))
                )

                min_length = min(
                    min_length,
                    max(5, max_length - 5)
                )

                result = summarizer(
                    notes,
                    max_length=max_length,
                    min_length=min_length,
                    do_sample=False,
                    truncation=True
                )

                summary = result[0]["summary_text"]

            st.subheader("✨ Your Summary")
            st.write(summary)

            original_words = len(notes.split())
            summary_words = len(summary.split())

            col1, col2 = st.columns(2)

            col1.metric("Original Words", original_words)
            col2.metric("Summary Words", summary_words)

            if original_words > 0:
                reduction = (
                    (original_words - summary_words)
                    / original_words
                ) * 100

                st.write(
                    f"**Word reduction:** {max(0, reduction):.1f}%"
                )

            st.download_button(
                label="Download Summary",
                data=summary,
                file_name="ai_summary.txt",
                mime="text/plain"
            )

        except Exception as error:
            st.error(
                "Something went wrong while generating "
                "the summary. Please check your internet "
                "connection and try again."
            )
            st.caption(f"Technical details: {error}")

st.divider()
st.caption(
    "AI Notes Summarizer | Beginner Deep Learning Project"
)
