import pysubs2

def is_chinese(text):
    # A simple check to identify if the text contains Chinese characters
    return any('\u4e00' <= char <= '\u9fff' for char in text)

def convert_srt_to_ass_with_styles_and_custom_text(srt_file, ass_file):
    # Load the SRT file
    subs = pysubs2.load(srt_file)

    # Define styles
    subs.styles["English"] = pysubs2.SSAStyle(fontname="Arial", fontsize=10, outlinecolor="&H00A08B8C", primarycolor="&HFFFFFF", alignment=2, outline=0.5)
    subs.styles["Chinese"] = pysubs2.SSAStyle(fontname="Arial", fontsize=18, outlinecolor="&H00A08B8C", backcolor="&H000000", primarycolor="&HFFFFFF", alignment=2, outline=1, bold=True)
    # Define a custom style for the translator note
    subs.styles["Translator"] = pysubs2.SSAStyle(fontname="Arial", fontsize=16, outlinecolor="&H000000", backcolor="&H000000", primarycolor="&HFFFFFF", alignment=2)

    # Apply styles based on the content of each line
    for line in subs:
        if is_chinese(line.text):
            line.style = "Chinese"
        else:
            line.style = "English"

    # Add a custom subtitle for the translator note
    # Note: pysubs2 uses milliseconds for timing
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
