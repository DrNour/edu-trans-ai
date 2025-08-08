# EduTransAI Assessment Tool

## 🎯 Purpose
This tool helps students evaluate their English-to-Arabic translations by comparing them with a reference translation. It computes a similarity score and provides feedback using human-defined error criteria.

## 📂 How to Use

1. Download the [CSV Template](link-to-template) and fill in:
   - `Student Translation`
   - `Reference Translation`
   - (Optional) `Error Type`, `Error Severity`, and `Error Description`
2. Upload your filled CSV file into the app.
3. Click **Evaluate**.
4. Review the results:
   - Similarity Score (%)
   - Errors listed by type and severity
   - Suggestions (if any)

## 🧠 Definitions

| Term               | Definition |
|--------------------|------------|
| **Similarity Score** | Percentage match between student and reference translation, based on `difflib` sequence matcher. |
| **Error Type**       | Type of error, e.g., lexical, grammatical, stylistic, cultural. |
| **Severity**         | Level of seriousness: Minor, Major, Critical. |
| **Error Description** | Explanation or notes for the error. |

## 📸 Example

You can see how the results look with a sample file [here](link-to-screenshot).

## 👨‍🏫 Developer/Instructor

Dr. Nour El Din Abdelaal  
[Contact](mailto:nourabdelal@yahoo.com) | [GitHub](https://github.com/yourusername)
