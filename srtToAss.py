import pysubs2

def is_chinese(text):
    # A simple check to identify if the text contains Chinese characters
    return any('\u4e00' <= char <= '\u9fff' for char in text)

def convert_srt_to_ass_with_styles_and_custom_text(srt_file, ass_file):
    # Load the SRT file
    subs = pysubs2.load(srt_file)

    # Loop through each subtitle
    for line in subs:
        # Check if the line contains the special newline marker for splitting languages
        if "\\N" in line.text:
            # Split the text at the newline marker
            parts = line.text.split("\\N", 1)
            chinese_part = parts[0]
            english_part = parts[1]

            # Apply inline style overrides for each part
            # Note: You'll need to adjust these style codes to fit your needs
            chinese_style = "{\\c&HFFFFFF&\\3c&H6D6D97&\\fnAdobe Heiti Std\\fs30\\bord1.1\\shad1}"
            # chinese_style = "{\\3c&H6F6F9C&\\3a&H40\\shad0.1\\fnAdobe Heiti Std\\fs40}"
            english_style = "{\\3c&H6F6F9C&\\shad0.1\\bord0.5\\fnAdobe Heiti Std\\fs20}"

            # Reconstruct the line with style overrides
            line.text = f"{chinese_style}{chinese_part}\\N{english_style}{english_part}"

    # Add a custom subtitle for the translator note
    # Note: pysubs2 uses milliseconds for timing
    # Define a custom style for the translator note
    subs.styles["Translator"] = pysubs2.SSAStyle(fontname="Arial", fontsize=16, outlinecolor="&H000000", backcolor="&H000000", primarycolor="&HFFFFFF", alignment=2)
    translator_note = pysubs2.SSAEvent(start=90000, end=91000, text="translated by John", style="Translator")
    subs.append(translator_note)

    # Sort the subtitles by their start times to ensure correct ordering
    subs.sort()

    # Save the ASS file
    subs.save(ass_file)

# Example usage
srt_file = "test-srt.srt"
ass_file = "out-ass.ass"
convert_srt_to_ass_with_styles_and_custom_text(srt_file, ass_file)
