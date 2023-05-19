# Teams Transcript Cleaner

This script takes transcripts from Teams meetings and cleans them up by (1) removing all timestamps and (2) replacing speaker names with alternate labels. The latter is helpful for removing PII.

Note: Some PII may remain in your transcript. For example, if a speaker notes their title and company, this may still be linkable to them even without their name. Use caution.


## Requirements
1. Python 
2. Transcript files in txt format (not vtt)

## How to use
1. Add your transcripts (txt format) to the 'input' folder
2. In transcript-cleaner.py, add the names you wish to replace in the transcript in the **name_mapping** dictionary. Note that the names must match the transcript EXACTLY. For example, if the transcript says "Irina Smoke (guest)," then list "Irina Smoke (guest)", not "Irina" or "Irina Smoke"
3. Run transcript-cleaner.py.
4. Watch the command line to enter any new names not already covered in name_mapping when prompted (if applicable)
5. See your cleaned up txt files in the 'output' folder.
