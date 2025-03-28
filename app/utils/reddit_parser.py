#app/utils/reddit_parser.py
import aiohttp
import os
from datetime import datetime
from app.core.config import settings


async def parse_reddit(url: str) -> str:
    json_url = str(url).rstrip("/") + ".json"

    async with aiohttp.ClientSession() as session:
        async with session.get(json_url, headers={"User-Agent": settings.USER_AGENT}) as response:
            if response.status != 200:
                raise Exception(f"Failed to fetch Reddit page: {response.status}")
            data = await response.json()

            post_title = data[0]["data"]["children"][0]["data"]["title"]
            post_body = data[0]["data"]["children"][0]["data"].get("selftext", "")
            comments = data[1]["data"]["children"]
            comment_texts = [comment["data"]["body"] for comment in comments if "body" in comment["data"]]

            full_text = f"{post_title}\n{post_body}\n" + "\n".join(comment_texts)
            truncated_text = full_text[:settings.MAX_TEXT_LENGTH]

            os.makedirs("reddit_parsed_text", exist_ok=True)
            post_id = str(url).split("/comments/")[1].split("/")[0]
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"reddit_parsed_text/{post_id}_{timestamp}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(full_text)

            return truncated_text