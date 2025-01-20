import typer
from rich import print
from .word_counter import word_counter
from .llm import analyze_transcript

app = typer.Typer()

@app.command()
def analyze_transcript(path_to_script_text_file: str, min_count_threshold: int = 10):
    """
    Analyze a transcript text file, count word frequencies, run analysis, and print results.

    Usage:
        uv run main analyze-transcript <path-to-script-text-file> --min-count-threshold <threshold>
    """
    # Read the transcript file
    with open(path_to_script_text_file, 'r') as file:
        transcript = file.read()

    # Count word frequencies
    word_counts = word_counter(transcript, min_count_threshold)

    # Run analysis
    analysis = analyze_transcript(transcript, word_counts.count_to_word_map)

    # Print results
    print("[bold]Word Frequencies:[/bold]")
    for word, count in word_counts.count_to_word_map.items():
        print(f"{word}: {count}")

    print("\n[bold]Transcript Analysis:[/bold]")
    print(f"Quick Summary: {analysis.quick_summary}")
    print("Bullet Point Highlights:")
    for highlight in analysis.bullet_point_highlights:
        print(f"- {highlight}")
    print(f"Sentiment Analysis: {analysis.sentiment_analysis}")
    print("Keywords:")
    for keyword in analysis.keywords:
        print(f"- {keyword}")

if __name__ == "__main__":
    app()
