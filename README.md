# 🎌 MAL to Notion: Sync Your "Plan to Watch" Anime List with Community Ratings

This Python script lets you import your **"Plan to Watch"** anime list from **MyAnimeList (MAL)** and automatically add each anime along with its **community rating** into a **Notion database** of your choice.

It’s perfect for tracking anime you plan to watch, rated by the global anime community.

---

## 📌 What It Does

1. Parses your exported `animelist.xml` file from MyAnimeList
2. Filters for anime with status `"Plan to Watch"`
3. Fetches the community score for each anime using the [Jikan API](https://jikan.moe/)
4. Adds the title and score to your private Notion database

---

## 🧾 How to Use

### 1. 🔁 Export Your Anime List from MyAnimeList

1. Go to your MAL profile  
   Example: `https://myanimelist.net/profile/YOUR_USERNAME`
2. Click the 3 dots → **Export** or go directly to:  
   [`https://myanimelist.net/panel.php?go=export`](https://myanimelist.net/panel.php?go=export)
3. Download your anime list — it will be named something like `animelist.xml`

Place this file in the root directory of the script.

---

### 2. 🔐 Create a Notion Integration

1. Go to [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Click **"New Integration"**
3. Name it (e.g. `MAL Importer`)
4. Select your workspace
5. Copy the **Internal Integration Token**

---

### 3. 🧱 Set Up Your Notion Database

1. Create a new **Notion database** (table-style)
2. Make sure it has **two properties**:
   - `Name of title` → type: Title
   - `Rating (1-10)` → type: Number
3. Click the 3-dots menu on the table → **Open as full page**
4. Copy the **Database ID** from the URL.  
   Example URL: https://www.notion.so/workspace-name/Anime-99999eb8e012345d95b5fbaa287578d2
Your database ID is: `99999eb8e012345d95b5fbaa287578d2`

5. Go to **Share > Add Connections**, and **share the database with your integration**

---

### 4. ⚙️ Set Environment Variables

Create a `.env` file in the same folder as your script:

```env
NOTION_TOKEN=secret_your_notion_token_here
DATABASE_ID=your_notion_database_id_here
```

5. 🚀 Run the Script

Install dependencies:

```bash
pip install python-dotenv
```

or use the requirements.txt file

```bash
pip install -r requirements.txt
```

Then run:

```bash
python main.py
```

🔧 Customization

    To filter by another MAL status (like “Watching”), change the check in the script:

```python
if status == 'Watching':
```

To include MAL score threshold (e.g. only 7+):
    ```python
    if score and score >= 7:
    ```
    
## 📂 Example Output in Notion

| Name of title              | Rating (1–10) |
|---------------------------|---------------|
| Akudama Drive             | 7.57          |
| Akagami no Shirayuki-hime | 7.61          |


🤝 Credits

    Community ratings powered by Jikan API

    Built with ✨ ChatGPT guidance + vibe coding
