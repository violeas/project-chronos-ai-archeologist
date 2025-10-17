def generate_report(original, reconstructed, sources):
    report = "--- RECONSTRUCTION REPORT ---\n\n"
    report += "[Original Fragment]\n> " + original + "\n\n"
    report += "[AI-Reconstructed Text]\n> " + reconstructed + "\n\n"
    report += "[Contextual Sources]\n"
    for url in sources:
        report += f"* {url}\n"
    return report
