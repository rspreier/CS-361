1. To request data, call writeJournalEntry(string), where the string represents the mood that the user is experiencing
2. To recieve data, call getJournalEntry(string), where string represents either the date in the format of mm/dd/yyyy or a mood. This function returns an array of strings that show the date, time and mood the user experienced based on the search result. If there was no entry for the specified date or mood, the function returns an empty array.
![Untitled](https://user-images.githubusercontent.com/22330103/180856107-dc6a20ca-810a-4ff7-8ab0-99ac60822a77.jpg)
